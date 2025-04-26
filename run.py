#!/usr/bin/env python3
"""
Medical AI Assistant Launcher
This script allows users to choose between voice mode and text mode.
"""

import os
import sys
import importlib.util

def check_module(module_name):
    """Check if a Python module is installed"""
    return importlib.util.find_spec(module_name) is not None

def main():
    print("=" * 80)
    print("Medical AI Assistant")
    print("=" * 80)
    print("This application helps diagnose basic medical issues, suggests remedies,")
    print("and simulates booking doctor appointments.")
    print("-" * 80)
    
    while True:
        print("\nPlease select a mode:")
        print("1. Voice Mode (Speak to the assistant)")
        print("2. Text Mode (Type to the assistant)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            # Check for voice mode dependencies
            missing_deps = []
            for module in ['azure.cognitiveservices.speech', 'pyttsx3']:
                if not check_module(module):
                    missing_deps.append(module)
            
            if missing_deps:
                print("\nSome required packages are missing for voice mode:")
                print(", ".join(missing_deps))
                print("\nPlease install them using:")
                print("pip install -r requirements.txt")
                print("\nFalling back to text mode...\n")
                import text_mode
                text_mode.main()
            else:
                import medical_assistant
                medical_assistant.main()
                
        elif choice == "2":
            import text_mode
            text_mode.main()
            
        elif choice == "3":
            print("\nThank you for using the Medical AI Assistant. Goodbye!")
            sys.exit(0)
            
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main() 