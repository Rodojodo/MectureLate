MectureLate 🎓

MectureLate is an AI-powered utility that transforms lecture slide PDFs into clean, structured Markdown study notes using the Google Gemini API. It includes both a command-line interface and a web interface for managing and viewing your lecture notes.
🚀 Getting Started
1. Prerequisites

    Python 3.10 or higher

    Google Gemini API Key: Obtain a free key from Google AI Studio.

    Supabase Account: You'll need a Supabase project with a database set up for the web interface.

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

GEMINI_API_KEY=your_actual_api_key_here
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key

The Supabase credentials are required for the web interface to store and retrieve lecture notes.

🛠 Usage

## Option 1: Web Interface (Recommended) 🌐

The web interface provides an intuitive way to manage courses, upload PDFs, and view lecture notes.

**Starting the Web Application:**

Using the run script:
```bash
./run_web.sh
```

Or using the installed command:
```bash
mecture-web
```

Or directly with Streamlit:
```bash
streamlit run src/mecture_late/app.py
```

The web interface will open in your browser (usually at http://localhost:8501) and provides:

- **Read Notes**: Browse and view lecture notes organized by course
- **Admin Upload**: Upload PDF slides to automatically generate and store lecture notes
- Course management with the ability to create new courses
- Edit existing lecture notes directly in the browser

## Option 2: Command Line Interface 📝

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

## 🗄️ Database Setup

The web interface uses Supabase as its database backend. You'll need to create two tables in your Supabase project:

### Courses Table
```sql
CREATE TABLE courses (
  id BIGSERIAL PRIMARY KEY,
  course_code TEXT NOT NULL,
  course_name TEXT NOT NULL,
  year INTEGER,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### Lectures Table
```sql
CREATE TABLE lectures (
  id BIGSERIAL PRIMARY KEY,
  course_code TEXT NOT NULL,
  name TEXT NOT NULL,
  lecture_number INTEGER,
  content TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

After creating these tables, add your Supabase URL and anon key to the `.env` file as described in the Configuration section.