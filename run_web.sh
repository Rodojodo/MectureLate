#!/bin/bash
# Simple script to run the MectureLate web interface

echo "🚀 Starting MectureLate Web Interface..."
echo "Make sure you have set up your .env file with SUPABASE_URL and SUPABASE_KEY"
echo ""

# Navigate to the src directory and run streamlit
cd "$(dirname "$0")"
streamlit run src/mecture_late/app.py
