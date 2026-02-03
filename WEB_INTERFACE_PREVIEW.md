# MectureLate Web Interface Preview

## What You'll See When Running the Application

### Application Launch
When you run `./run_web.sh` or `streamlit run src/mecture_late/app.py`, Streamlit will:
1. Start a local web server (usually on port 8501)
2. Open your default browser automatically
3. Display the MectureLate web interface

### Main Interface Layout

```
╔═══════════════════════════════════════════════════════════════════╗
║  Lecture Notes                                      [Streamlit Logo]║
╠═══════════════╦═══════════════════════════════════════════════════╣
║               ║                                                    ║
║  SIDEBAR      ║              MAIN CONTENT AREA                     ║
║  ═══════      ║                                                    ║
║               ║                                                    ║
║ Navigation:   ║  When "Read Notes" is selected:                   ║
║ ○ Read Notes  ║  ┌─────────────────────────────────────────────┐  ║
║ ○ Admin Upload║  │ Notes for CS101                             │  ║
║               ║  │                                             │  ║
║ Select Course:║  │ ▼ Lecture 1: Introduction to Python        │  ║
║ [CS101    ▼]  ║  │   # Introduction to Python                  │  ║
║               ║  │   This lecture covers...                    │  ║
║               ║  │   [Edit]                                    │  ║
║               ║  │                                             │  ║
║               ║  │ ▼ Lecture 2: Variables and Data Types      │  ║
║               ║  │   # Variables and Data Types                │  ║
║               ║  │   In this lecture we learn...               │  ║
║               ║  │   [Edit]                                    │  ║
║               ║  └─────────────────────────────────────────────┘  ║
║               ║                                                    ║
║               ║  When "Admin Upload" is selected:                 ║
║               ║  ┌─────────────────────────────────────────────┐  ║
║               ║  │ 🚀 AI Note Generator                        │  ║
║               ║  │                                             │  ║
║               ║  │ 1. Target Course                            │  ║
║               ║  │ Course Code: [CS101___]                     │  ║
║               ║  │ ✅ Found: Intro to Computer Science         │  ║
║               ║  │                                             │  ║
║               ║  │ 2. Upload Slides                            │  ║
║               ║  │ [📁 Browse Files...]                        │  ║
║               ║  │ ☐ Overwrite existing notes?                 │  ║
║               ║  │                                             │  ║
║               ║  │         [Generate & Save]                   │  ║
║               ║  └─────────────────────────────────────────────┘  ║
╚═══════════════╩═══════════════════════════════════════════════════╝
```

## Features Demonstration

### 1. Browsing Lecture Notes
- **Left Sidebar**: Select any course from the dropdown
- **Main Area**: See all lectures for that course
- **Expandable Sections**: Click to expand/collapse individual lectures
- **Markdown Rendering**: Notes are beautifully formatted with headers, lists, code blocks, etc.
- **Edit Mode**: Click "Edit" button to modify any lecture note inline

### 2. Uploading PDFs and Generating Notes
- **Course Selection**: Type a course code; if it doesn't exist, you can create it on the spot
- **File Upload**: Drag and drop or browse for multiple PDF files
- **Batch Processing**: Process multiple lectures at once
- **Progress Tracking**: Live status updates as each PDF is processed
- **AI Generation**: Automatically converts PDF slides to formatted Markdown

### 3. Course Management
- **Create New Courses**: Add courses with code and name
- **View All Courses**: Browse through all available courses
- **Filter by Course**: Quickly switch between different courses

## Example User Flow

### Scenario 1: Student Reading Notes
1. Open the web interface
2. Select course from dropdown (e.g., "CS101 - Intro to CS")
3. Click "Read Notes" in sidebar
4. Expand any lecture to view notes
5. Optionally edit notes if you spot an error

### Scenario 2: Administrator Uploading New Lectures
1. Open the web interface
2. Click "Admin Upload" in sidebar
3. Enter course code "CS101"
4. Upload PDF files (e.g., "Lecture_03_Loops.pdf", "Lecture_04_Functions.pdf")
5. Check "Overwrite existing notes" if updating
6. Click "Generate & Save"
7. Wait for AI processing
8. See success messages for each lecture

## Technical Notes

### Performance
- The database manager uses Streamlit's `@st.cache_resource` to maintain a single database connection
- This prevents reconnecting on every interaction, making the app fast and responsive

### Safety
- The app checks for existing lectures before creating new ones
- You can choose to overwrite or skip existing notes
- All database operations have error handling

### Accessibility
- Clean, simple interface
- Keyboard navigation supported
- Mobile-responsive layout
- Clear status messages and feedback
