#!/usr/bin/env python3
"""
IBM Quantum Connection Setup Script

This script helps you easily set up your IBM Quantum account connection.
Run this script once to save your API token for future use.

Usage:
    python setup_ibm_quantum.py

You'll be prompted to enter your IBM Quantum API token.
"""

import sys
from qiskit_ibm_runtime import QiskitRuntimeService

def setup_ibm_quantum():
    """Set up IBM Quantum connection with user's API token."""
    
    print("=" * 60)
    print("IBM Quantum Connection Setup")
    print("=" * 60)
    print()
    print("To get your API token:")
    print("1. Go to https://quantum-computing.ibm.com/")
    print("2. Sign in to your IBM Quantum account")
    print("3. Click on your profile (top right)")
    print("4. Go to 'Account settings'")
    print("5. Copy your API token")
    print()
    
    # Get token from user
    token = input("Enter your IBM Quantum API token: ").strip()
    
    if not token:
        print("No token provided. Exiting.")
        sys.exit(1)
    
    try:
        # Save the account
        QiskitRuntimeService.save_account(
            channel="ibm_quantum_platform", 
            token=token, 
            overwrite=True
        )
        
        print("IBM Quantum account saved successfully!")
        print()
        print("You can now use IBM Quantum services in your code with:")
        print("    from qiskit_ibm_runtime import QiskitRuntimeService")
        print("    service = QiskitRuntimeService()")
        print()
        
        # Test the connection
        print("Testing connection...")
        service = QiskitRuntimeService()
        backends = service.backends()
        print(f"Connection successful! Found {len(backends)} available backends.")
        
    except Exception as e:
        print(f" Error setting up IBM Quantum connection: {e}")
        print("Please check your token and try again.")
        sys.exit(1)

if __name__ == "__main__":
    setup_ibm_quantum()
