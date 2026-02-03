"""
Entry point to run the Streamlit web application.
This script launches the Streamlit server for the MectureLate web interface.
"""
import os
import sys
import subprocess


def main():
    """Launch the Streamlit web application."""
    # Get the directory where app.py is located
    app_dir = os.path.dirname(__file__)
    app_path = os.path.join(app_dir, "app.py")
    
    # Run streamlit with the app.py file
    subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])


if __name__ == "__main__":
    main()
