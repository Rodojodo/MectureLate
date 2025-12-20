Here is a professional, comprehensive README.md for MectureLate. It covers everything from the initial clone to the API setup and the new CLI command you just built.
MectureLate 🎓

MectureLate is an AI-powered utility that transforms lecture slide PDFs into clean, structured Markdown study notes using the Google Gemini API.
🚀 Getting Started
1. Prerequisites

    Python 3.10 or higher

    Google Gemini API Key: Obtain a free key from Google AI Studio.

2. Installation

Clone the repository and set up your environment using the following steps:
Bash

# Clone the repository
git clone https://github.com/your-username/MectureLate.git
cd MectureLate

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install in editable mode
pip install -e .

3. Configuration

MectureLate looks for your API key in a .env file. Create one in the root directory:
Bash

touch .env

Open .env in your editor and add your key:
Plaintext

GEMINI_KEY="your_actual_api_key_here"

🛠 Usage
📂 File Organization

    Input: Place your lecture PDFs inside rsc/input_slides/.

    Output: Your generated notes will appear in the output/ folder.

📝 Running the Program

Thanks to the package configuration, you can run the tool from anywhere within your virtual environment using the custom command:
Bash

mecture

The program will:

    Detect all PDFs in your input folder.

    Check if notes already exist (and ask if you'd like to skip them).

    Generate new notes while respecting Google's API rate limits.