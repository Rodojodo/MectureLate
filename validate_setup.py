#!/usr/bin/env python3
"""
Script to validate the MectureLate web application setup.
This checks that all dependencies are installed and files are properly configured.
"""

import sys
from pathlib import Path

def check_dependencies():
    """Check if all required dependencies are installed."""
    print("🔍 Checking dependencies...")
    
    required_packages = {
        'streamlit': 'Streamlit (Web Framework)',
        'supabase': 'Supabase (Database Client)',
        'google.genai': 'Google Generative AI',
        'dotenv': 'Python Dotenv (Environment Variables)'
    }
    
    missing = []
    for package, name in required_packages.items():
        try:
            __import__(package)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name}")
            missing.append(name)
    
    return len(missing) == 0

def check_project_structure():
    """Check if the project structure is correct."""
    print("\n🔍 Checking project structure...")
    
    required_files = [
        'src/mecture_late/app.py',
        'src/mecture_late/database_manager.py',
        'src/mecture_late/admin_interface.py',
        'src/mecture_late/run_web.py',
        'run_web.sh',
        'pyproject.toml'
    ]
    
    # Use current working directory if running from project root
    project_root = Path.cwd()
    # Or use script location as fallback
    if not (project_root / 'pyproject.toml').exists():
        project_root = Path(__file__).parent
    
    missing = []
    
    for file_path in required_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path}")
            missing.append(file_path)
    
    return len(missing) == 0

def check_env_file():
    """Check if .env file exists."""
    print("\n🔍 Checking environment configuration...")
    
    # Use current working directory if running from project root
    project_root = Path.cwd()
    if not (project_root / 'pyproject.toml').exists():
        project_root = Path(__file__).parent
    
    env_file = project_root / '.env'
    env_example = project_root / '.env.example'
    
    if env_file.exists():
        print(f"  ✅ .env file found")
        return True
    else:
        print(f"  ⚠️  .env file not found")
        if env_example.exists():
            print(f"  ℹ️  Use .env.example as a template to create your .env file")
        return False

def main():
    """Run all validation checks."""
    print("=" * 60)
    print("MectureLate Web Application Setup Validator")
    print("=" * 60)
    
    deps_ok = check_dependencies()
    structure_ok = check_project_structure()
    env_ok = check_env_file()
    
    print("\n" + "=" * 60)
    if deps_ok and structure_ok:
        print("✅ Setup validation passed!")
        print("\nTo run the web application:")
        print("  ./run_web.sh")
        print("  OR")
        print("  streamlit run src/mecture_late/app.py")
        
        if not env_ok:
            print("\n⚠️  Remember to create a .env file with your credentials!")
        
        return 0
    else:
        print("❌ Setup validation failed!")
        print("\nPlease fix the issues above before running the application.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
