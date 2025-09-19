#!/usr/bin/env python3
"""
Recall Network Trading Agent - Main Application
A sophisticated AI-powered cryptocurrency trading agent built for Recall Network competitions.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_environment():
    """Check if environment is properly configured."""
    print("🔍 Checking environment configuration...")
    
    api_key = os.getenv("RECALL_API_KEY")
    environment = os.getenv("ENVIRONMENT", "sandbox")
    
    if api_key and api_key != "pk_live_your_api_key_here":
        print("✅ API key configured")
        print(f"🌍 Environment: {environment}")
        return True
    else:
        print("❌ API key not configured")
        print("📝 Please follow these steps:")
        print("   1. Copy .env.example to .env")
        print("   2. Get your API key from: https://register.recall.network/")
        print("   3. Add your API key to the .env file")
        return False

def main():
    """Main application entry point."""
    print("🤖 Recall Network AI Trading Agent")
    print("=" * 50)
    print("🏆 Competition-ready cryptocurrency trading agent")
    print("🎯 Features: Advanced strategies, risk management, portfolio tracking")
    print("")
    
    # Check environment configuration
    if check_environment():
        print("")
        print("🚀 Ready to start trading!")
        print("📊 Available commands:")
        print("   - Verify API connection")
        print("   - Start automated trading")
        print("   - Run strategy backtests")
        print("   - Monitor portfolio performance")
    else:
        print("")
        print("⚙️ Please configure your environment first.")
    
    print("")
    print("🔗 Useful links:")
    print("   - Recall Network: https://recall.network/")
    print("   - Documentation: https://docs.recall.network/")
    print("   - Get API Key: https://register.recall.network/")

if __name__ == "__main__":
    main()
