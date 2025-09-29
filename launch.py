#!/usr/bin/env python3
"""
GIACONVERT Launcher
Double-click this file to start the GIACONVERT web application.
"""

import os
import sys
import time
import socket
import webbrowser
import subprocess
from pathlib import Path

def check_port_in_use(port):
    """Check if a port is already in use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('127.0.0.1', port))
            return False
        except OSError:
            return True

def wait_for_server(port, timeout=10):
    """Wait for server to start responding"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex(('127.0.0.1', port))
                if result == 0:
                    return True
        except:
            pass
        time.sleep(0.5)
    return False

def find_available_port(start_port=8000, max_port=8010):
    """Find an available port starting from start_port"""
    for port in range(start_port, max_port + 1):
        if not check_port_in_use(port):
            return port
    return None

def main():
    print("🚀 GIACONVERT Launcher")
    print("=" * 50)
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    app_file = script_dir / "app.py"
    venv_python = script_dir / ".venv" / "bin" / "python"
    
    # Check if app.py exists
    if not app_file.exists():
        print("❌ Error: app.py not found in the current directory")
        print(f"   Expected location: {app_file}")
        input("Press Enter to exit...")
        return 1
    
    # Check if virtual environment exists
    if not venv_python.exists():
        print("❌ Error: Virtual environment not found")
        print(f"   Expected location: {venv_python}")
        print("   Please run setup.sh first to create the virtual environment")
        input("Press Enter to exit...")
        return 1
    
    # Find available port
    port = find_available_port()
    if port is None:
        print("❌ Error: No available ports found (tried 8000-8010)")
        input("Press Enter to exit...")
        return 1
    
    # Check if server is already running on the port
    if check_port_in_use(port):
        print(f"✅ Server already running on port {port}")
        url = f"http://127.0.0.1:{port}"
        print(f"🌐 Opening browser: {url}")
        webbrowser.open(url)
        return 0
    
    print(f"🔍 Starting server on port {port}...")
    
    try:
        # Start the server
        env = os.environ.copy()
        env['PYTHONPATH'] = str(script_dir)
        
        server_process = subprocess.Popen([
            str(venv_python), 
            str(app_file)
        ], 
        cwd=str(script_dir),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
        )
        
        print("⏳ Waiting for server to start...")
        
        # Wait for server to start
        if wait_for_server(port):
            print("✅ Server started successfully!")
            url = f"http://127.0.0.1:{port}"
            print(f"🌐 Opening browser: {url}")
            webbrowser.open(url)
            
            print("\n" + "=" * 50)
            print("GIACONVERT is now running!")
            print(f"Web interface: {url}")
            print("Press Ctrl+C to stop the server")
            print("=" * 50)
            
            # Keep the process running and show output
            try:
                while True:
                    output = server_process.stdout.readline()
                    if output:
                        print(output.strip())
                    elif server_process.poll() is not None:
                        break
            except KeyboardInterrupt:
                print("\n🛑 Stopping server...")
                server_process.terminate()
                server_process.wait()
                print("✅ Server stopped")
                
        else:
            print("❌ Server failed to start within timeout period")
            server_process.terminate()
            return 1
            
    except FileNotFoundError:
        print(f"❌ Error: Python executable not found at {venv_python}")
        print("   Please ensure the virtual environment is properly set up")
        input("Press Enter to exit...")
        return 1
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        input("Press Enter to exit...")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())