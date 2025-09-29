// GIACONVERT Vue.js Application
const { createApp } = Vue;

const GiaconvertApp = {
    data() {
        return {
            // Application state
            currentStep: 'welcome', // 'welcome', 'fileSelection', 'settings', 'progress'
            serverStatus: 'checking',
            
            // File selection
            selectedFiles: [],
            
            // Conversion settings
            conversionModes: {},
            selectedMode: 'enhanced',
            outputOption: 'beside',
            destinationPath: '',
            
            // Conversion progress
            conversionId: null,
            conversionProgress: 0,
            currentFile: null,
            completedFiles: 0,
            totalFiles: 0,
            conversionResults: [],
            conversionErrors: [],
            conversionComplete: false,
            
            // Polling
            statusPollingInterval: null,
            
            // API base URL
            apiBaseUrl: window.location.origin + '/api'
        }
    },
    
    computed: {
        serverStatusClass() {
            return {
                'text-success': this.serverStatus === 'online',
                'text-error': this.serverStatus === 'offline',
                'text-warning': this.serverStatus === 'checking'
            };
        },
        
        docxFiles() {
            const filtered = this.selectedFiles.filter(file => {
                const name = file.name.toLowerCase();
                return (name.endsWith('.docx') || name.endsWith('.doc')) && 
                       !file.name.startsWith('~$') &&
                       !file.name.startsWith('.');
            });
            console.log('Computed docxFiles:', filtered.length, 'out of', this.selectedFiles.length, 'total files');
            return filtered;
        },
        
        canStartConversion() {
            const hasFiles = this.docxFiles.length > 0;
            const hasMode = this.selectedMode;
            const hasValidOutput = this.outputOption === 'beside' || 
                                 (this.destinationPath && this.destinationPath.trim());
            
            return hasFiles && hasMode && hasValidOutput;
        }
    },
    
    mounted() {
        this.checkServerHealth();
        this.loadConversionModes();
        this.loadUserSettings();
    },
    
    beforeUnmount() {
        this.stopStatusPolling();
    },
    
    methods: {
        // Server communication
        async checkServerHealth() {
            try {
                const response = await fetch(`${this.apiBaseUrl}/health`);
                if (response.ok) {
                    this.serverStatus = 'online';
                } else {
                    this.serverStatus = 'offline';
                }
            } catch (error) {
                this.serverStatus = 'offline';
                console.error('Server health check failed:', error);
            }
        },
        
        async loadConversionModes() {
            try {
                const response = await fetch(`${this.apiBaseUrl}/modes`);
                if (response.ok) {
                    const data = await response.json();
                    this.conversionModes = data.modes;
                }
            } catch (error) {
                console.error('Failed to load conversion modes:', error);
                // Fallback to default modes
                this.conversionModes = {
                    basic: {
                        name: 'Basic',
                        description: 'Convert text and tables only',
                        features: ['Text formatting', 'Tables', 'Fast conversion']
                    },
                    enhanced: {
                        name: 'Enhanced',
                        description: 'Includes images with optimization',
                        features: ['Text formatting', 'Tables', 'Images', 'Image optimization']
                    },
                    complete: {
                        name: 'Complete',
                        description: 'Full document with headers and footers',
                        features: ['Text formatting', 'Tables', 'Images', 'Headers/Footers', 'Page layout']
                    }
                };
            }
        },
        
        // Navigation
        startConversion() {
            this.currentStep = 'fileSelection';
        },
        
        goBack() {
            if (this.currentStep === 'fileSelection') {
                this.currentStep = 'welcome';
            } else if (this.currentStep === 'settings') {
                this.currentStep = 'fileSelection';
            } else if (this.currentStep === 'progress') {
                this.currentStep = 'settings';
            }
        },
        
        proceedToSettings() {
            if (this.docxFiles.length > 0) {
                this.currentStep = 'settings';
            } else {
                this.showError('Please select at least one Word document (.docx)');
            }
        },
        
        startNewConversion() {
            this.resetConversionState();
            this.currentStep = 'welcome';
        },
        
        // File handling
        handleFileSelection(event) {
            const files = Array.from(event.target.files);
            console.log('Individual file selection - Total files found:', files.length);
            console.log('Files:', files.map(f => ({ name: f.name, size: f.size })));
            
            // Filter for .doc/.docx files only and exclude temp files
            const docFiles = files.filter(file => {
                const name = file.name.toLowerCase();
                return (name.endsWith('.docx') || name.endsWith('.doc')) && 
                       !file.name.startsWith('~$') &&
                       !file.name.startsWith('.');
            });
            
            console.log('Filtered .doc/.docx files:', docFiles.length);
            
            // Add to existing files (don't replace)
            this.selectedFiles = [...this.selectedFiles, ...docFiles];
            this.saveUserSettings();
            
            // Show user feedback
            if (docFiles.length === 0) {
                this.showError('Please select only .doc or .docx files.');
            } else {
                this.showSuccess(`Successfully added ${docFiles.length} Word documents`);
                console.log(`Successfully added ${docFiles.length} Word documents`);
            }
        },
        
        handleFolderSelection(event) {
            const files = Array.from(event.target.files);
            console.log('Folder selection - Total files found:', files.length);
            console.log('Files:', files.map(f => ({ name: f.name, size: f.size, path: f.webkitRelativePath })));
            
            // Filter for .doc/.docx files only and exclude temp files
            const docFiles = files.filter(file => {
                const name = file.name.toLowerCase();
                return (name.endsWith('.docx') || name.endsWith('.doc')) && 
                       !file.name.startsWith('~$') &&
                       !file.name.startsWith('.');
            });
            
            console.log('Filtered .doc/.docx files:', docFiles.length);
            console.log('DOC files:', docFiles.map(f => ({ name: f.name, size: f.size, path: f.webkitRelativePath })));
            
            this.selectedFiles = docFiles;
            this.saveUserSettings();
            
            // Show user feedback
            if (docFiles.length === 0) {
                this.showError('No .doc or .docx files found in the selected folder.');
            } else {
                // Show success message briefly
                this.showSuccess(`Successfully loaded ${docFiles.length} Word documents from folder`);
                console.log(`Successfully loaded ${docFiles.length} Word documents from folder`);
            }
        },
        
        clearFiles() {
            this.selectedFiles = [];
            if (this.$refs.fileInput) {
                this.$refs.fileInput.value = '';
            }
            if (this.$refs.folderInput) {
                this.$refs.folderInput.value = '';
            }
            console.log('All files cleared');
        },
        
        // Conversion process
        async startDocumentConversion() {
            if (!this.canStartConversion) {
                return;
            }
            
            try {
                this.currentStep = 'progress';
                this.resetConversionProgress();
                
                // Upload files first
                const uploadedFiles = await this.uploadFiles();
                
                if (uploadedFiles.length === 0) {
                    this.showError('No files were uploaded successfully');
                    return;
                }
                
                // Start conversion
                const conversionRequest = {
                    files: uploadedFiles.map(f => f.path),
                    mode: this.selectedMode,
                    output_option: this.outputOption,
                    destination_path: this.destinationPath || null
                };
                
                const response = await fetch(`${this.apiBaseUrl}/convert`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(conversionRequest)
                });
                
                if (response.ok) {
                    const result = await response.json();
                    this.conversionId = result.conversion_id;
                    this.startStatusPolling();
                } else {
                    const error = await response.json();
                    this.showError(`Failed to start conversion: ${error.error?.message || 'Unknown error'}`);
                }
                
            } catch (error) {
                console.error('Conversion error:', error);
                this.showError('Failed to start conversion. Please try again.');
            }
        },
        
        async uploadFiles() {
            const formData = new FormData();
            
            // Add all selected .docx files
            this.docxFiles.forEach(file => {
                formData.append('files', file);
            });
            
            try {
                const response = await fetch(`${this.apiBaseUrl}/upload`, {
                    method: 'POST',
                    body: formData
                });
                
                if (response.ok) {
                    return await response.json();
                } else {
                    const error = await response.json();
                    this.showError(`Upload failed: ${error.error?.message || 'Unknown error'}`);
                    return [];
                }
            } catch (error) {
                console.error('Upload error:', error);
                this.showError('Failed to upload files. Please check your connection.');
                return [];
            }
        },
        
        // Status polling
        startStatusPolling() {
            this.statusPollingInterval = setInterval(async () => {
                await this.checkConversionStatus();
            }, 1000); // Poll every second
        },
        
        stopStatusPolling() {
            if (this.statusPollingInterval) {
                clearInterval(this.statusPollingInterval);
                this.statusPollingInterval = null;
            }
        },
        
        async checkConversionStatus() {
            if (!this.conversionId) return;
            
            try {
                const response = await fetch(`${this.apiBaseUrl}/status/${this.conversionId}`);
                
                if (response.ok) {
                    const status = await response.json();
                    
                    this.conversionProgress = status.progress;
                    this.currentFile = status.current_file;
                    this.completedFiles = status.completed_files;
                    this.totalFiles = status.total_files;
                    this.conversionResults = status.results || [];
                    this.conversionErrors = status.errors || [];
                    
                    if (status.status === 'completed' || status.status === 'completed_with_errors' || status.status === 'failed') {
                        this.conversionComplete = true;
                        this.stopStatusPolling();
                        
                        if (status.status === 'failed') {
                            this.showError('Conversion failed. Please check the error messages above.');
                        }
                    }
                } else {
                    console.error('Failed to get conversion status');
                }
            } catch (error) {
                console.error('Status check error:', error);
            }
        },
        
        // Helper methods
        resetConversionState() {
            this.conversionId = null;
            this.resetConversionProgress();
            this.stopStatusPolling();
        },
        
        resetConversionProgress() {
            this.conversionProgress = 0;
            this.currentFile = null;
            this.completedFiles = 0;
            this.totalFiles = 0;
            this.conversionResults = [];
            this.conversionErrors = [];
            this.conversionComplete = false;
        },
        
        formatFileSize(bytes) {
            if (bytes === 0) return '0 Bytes';
            
            const k = 1024;
            const sizes = ['Bytes', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            
            return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
        },
        
        getFileName(filePath) {
            return filePath.split('/').pop().split('\\').pop();
        },
        
        showError(message) {
            // Simple error display - in a real app, you might use a toast library
            alert('❌ ' + message);
        },
        
        showSuccess(message) {
            // Simple success display - in a real app, you might use a toast library
            alert('✅ ' + message);
        },
        
        downloadResults() {
            // Placeholder for download functionality
            alert('Download functionality will be implemented in the next iteration');
        },
        
        // User settings persistence
        loadUserSettings() {
            try {
                const settings = localStorage.getItem('giaconvert_settings');
                if (settings) {
                    const parsed = JSON.parse(settings);
                    this.selectedMode = parsed.selectedMode || 'enhanced';
                    this.outputOption = parsed.outputOption || 'beside';
                    this.destinationPath = parsed.destinationPath || '';
                }
            } catch (error) {
                console.error('Failed to load user settings:', error);
            }
        },
        
        saveUserSettings() {
            try {
                const settings = {
                    selectedMode: this.selectedMode,
                    outputOption: this.outputOption,
                    destinationPath: this.destinationPath
                };
                localStorage.setItem('giaconvert_settings', JSON.stringify(settings));
            } catch (error) {
                console.error('Failed to save user settings:', error);
            }
        }
    },
    
    watch: {
        selectedMode() {
            this.saveUserSettings();
        },
        
        outputOption() {
            this.saveUserSettings();
        },
        
        destinationPath() {
            this.saveUserSettings();
        }
    }
};

// Create and mount the Vue application
createApp(GiaconvertApp).mount('#app');