#!/usr/bin/env python3
"""
Dr. Maya Medical Assistant Launcher
This script provides a simple menu to run the medical assistant in different modes.
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if required Python packages are installed"""
    try:
        import openai
        import dotenv
        import requests
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        return False

def check_api_keys():
    """Check if API keys are configured"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        openai_key = os.getenv("OPENAI_API_KEY")
        if not openai_key:
            print("\nWarning: OPENAI_API_KEY not found in .env file.")
            print("Some features may be limited without this API key.")
        
        azure_key = os.getenv("AZURE_SPEECH_KEY")
        if not azure_key:
            print("\nWarning: AZURE_SPEECH_KEY not found in .env file.")
            print("Voice mode will use fallback text-to-speech with limited capabilities.")
        
        return True
    except Exception as e:
        print(f"Error checking API keys: {e}")
        return False

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main launcher function"""
    clear_screen()
    
    print("=" * 60)
    print("           Dr. Maya Medical Assistant Launcher")
    print("=" * 60)
    
    # Check dependencies
    print("\nChecking dependencies...")
    deps_ok = check_dependencies()
    if not deps_ok:
        print("\nSome dependencies are missing. Please run:")
        print("pip install -r requirements.txt")
        return
    
    # Check API keys
    print("\nChecking API configuration...")
    check_api_keys()
    
    # Display menu
    print("\nPlease select a mode:")
    print("1. Text Mode       - Text-only interaction (no voice)")
    print("2. Voice Mode      - Full voice interaction (requires Azure Speech API)")
    print("3. Test Mode       - Run test sequence")
    print("q. Quit")
    
    choice = input("\nEnter your choice (1-3, q): ").strip().lower()
    
    if choice == 'q':
        print("Exiting launcher. Goodbye!")
        return
    
    # Launch the appropriate mode
    if choice == '1':
        print("\nStarting Dr. Maya in text mode...")
        subprocess.run([sys.executable, "main.py", "--text"])
    elif choice == '2':
        print("\nStarting Dr. Maya in voice mode...")
        subprocess.run([sys.executable, "main.py"])
    elif choice == '3':
        print("\nRunning test sequence...")
        subprocess.run([sys.executable, "main.py", "--test"])
    else:
        print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 