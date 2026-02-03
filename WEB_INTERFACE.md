# MectureLate Web Interface Documentation

## Overview

The MectureLate web interface provides a user-friendly way to manage lecture notes stored in a Supabase database. The application is built with Streamlit and offers two main pages:

## Features

### 1. Read Notes Page 📖

The "Read Notes" page allows you to:
- Browse all lecture notes organized by course
- Select a course from the sidebar dropdown
- View lecture notes in expandable sections (one per lecture)
- Edit existing lecture notes inline
- Notes are displayed in Markdown format for rich formatting

**How to use:**
1. Select a course from the sidebar dropdown
2. Click on any lecture expander to view its content
3. Click the "Edit" button to modify the content
4. Save your changes or cancel to go back

### 2. Admin Upload Page 🚀

The "Admin Upload" page is designed for administrators to:
- Create new courses in the database
- Upload PDF lecture slides
- Automatically generate AI-powered notes from PDFs using Google Gemini
- Batch process multiple PDF files at once
- Choose to overwrite existing notes or skip them

**How to use:**
1. Enter a course code (e.g., "CS101")
2. If the course doesn't exist, you'll be prompted to create it
3. Upload one or more PDF files
4. Choose whether to overwrite existing notes (if any)
5. Click "Generate & Save" to process the PDFs
6. The system will generate notes and save them to the database

## Database Structure

The application expects two tables in your Supabase database:

### Courses Table
- `id`: Primary key (auto-generated)
- `course_code`: Text (e.g., "CS101")
- `course_name`: Text (e.g., "Introduction to Computer Science")
- `year`: Integer (current year by default)
- `created_at`: Timestamp

### Lectures Table
- `id`: Primary key (auto-generated)
- `course_code`: Text (foreign reference to courses)
- `name`: Text (lecture name/topic)
- `lecture_number`: Integer (lecture sequence number)
- `content`: Text (Markdown-formatted lecture notes)
- `created_at`: Timestamp

## Configuration

Create a `.env` file in the project root with:

```env
GEMINI_API_KEY=your_gemini_api_key
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key
```

## Running the Application

Three ways to start the web interface:

1. **Using the run script (recommended):**
   ```bash
   ./run_web.sh
   ```

2. **Using the installed command:**
   ```bash
   mecture-web
   ```

3. **Directly with Streamlit:**
   ```bash
   streamlit run src/mecture_late/app.py
   ```

The application will open in your browser at `http://localhost:8501`.

## Technical Details

- **Framework**: Streamlit (Python web framework)
- **Database**: Supabase (PostgreSQL)
- **AI Model**: Google Gemini (for PDF to Markdown conversion)
- **Language**: Python 3.10+

## Troubleshooting

**Issue**: Cannot connect to database
- **Solution**: Check that your `.env` file has the correct `SUPABASE_URL` and `SUPABASE_KEY`

**Issue**: No courses appear in the dropdown
- **Solution**: Use the Admin Upload page to create your first course

**Issue**: PDF processing fails
- **Solution**: Ensure your `GEMINI_API_KEY` is valid and you haven't exceeded rate limits

**Issue**: Import errors when running the app
- **Solution**: Run `pip install -e .` to install all dependencies
