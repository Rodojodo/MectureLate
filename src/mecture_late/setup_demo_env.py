"""
Demo script to test the web interface without real Supabase credentials.
This creates a mock .env file for testing purposes.
"""

import os
from pathlib import Path

# Create a demo .env file
env_content = """# Demo environment variables for testing
GEMINI_API_KEY=your_gemini_api_key_here
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your_supabase_anon_key_here
"""

env_path = Path(__file__).parent.parent.parent / ".env"

if not env_path.exists():
    with open(env_path, "w") as f:
        f.write(env_content)
    print(f"✅ Created demo .env file at {env_path}")
    print("⚠️  Note: This is a demo configuration and won't connect to a real database.")
    print("To use a real database, replace the values in .env with your actual Supabase credentials.")
else:
    print(f"ℹ️  .env file already exists at {env_path}")
    print("Using existing configuration.")
