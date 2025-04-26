import os
import sys
import argparse
from medical_assistant import main as run_assistant
from text_mode import text_mode

def main():
    """Entry point for Dr. Maya Medical Assistant"""
    parser = argparse.ArgumentParser(description="Dr. Maya - Medical AI Assistant")
    parser.add_argument('--text', action='store_true', help='Run in text-only mode (no voice)')
    parser.add_argument('--test', action='store_true', help='Run test sequence')
    
    args = parser.parse_args()
    
    print("Starting Dr. Maya Medical Assistant...")
    print("======================================")
    
    if args.test:
        # Import and run test module
        try:
            from test_assistant import run_test
            run_test()
        except ImportError:
            print("Error: Test module not found.")
            sys.exit(1)
    elif args.text:
        # Run in text-only mode
        text_mode()
    else:
        # Run the voice-based assistant
        run_assistant()
        
if __name__ == "__main__":
    main() 