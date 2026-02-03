# MectureLate System Architecture

## Web Application Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    MectureLate Web Interface                     │
│                         (Streamlit App)                          │
└─────────────────────────────────────────────────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
        ┌───────────▼──────────┐   ┌─────────▼──────────┐
        │   Read Notes Page    │   │  Admin Upload Page │
        │                      │   │                    │
        │  - Browse courses    │   │  - Create courses  │
        │  - View lectures     │   │  - Upload PDFs     │
        │  - Edit notes        │   │  - AI processing   │
        └───────────┬──────────┘   └─────────┬──────────┘
                    │                         │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │   Database Manager      │
                    │                         │
                    │  - create_course()      │
                    │  - create_lecture_note()│
                    │  - update_lecture_note()│
                    │  - check_lecture_exists()│
                    │  - list_all_entries()   │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │   Supabase Database     │
                    │                         │
                    │  ┌─────────────────┐   │
                    │  │  courses table  │   │
                    │  └─────────────────┘   │
                    │  ┌─────────────────┐   │
                    │  │ lectures table  │   │
                    │  └─────────────────┘   │
                    └─────────────────────────┘
```

## Data Flow for PDF Processing

```
1. User uploads PDF
         │
         ▼
2. File saved to temp directory
         │
         ▼
3. Extract metadata (lecture name, number)
         │
         ▼
4. Check if lecture exists in database
         │
         ├─── YES ──── Overwrite? ─── YES ──┐
         │                                   │
         └─── NO ──────────────────────────┐│
                                           ││
                                           ▼▼
5. Send PDF to Google Gemini API
   (AI generates Markdown notes)
         │
         ▼
6. Receive Markdown content
         │
         ├─── Existing lecture ──▶ Update in database
         │
         └─── New lecture ──────▶ Create in database
                                        │
                                        ▼
7. Optional: Save local backup to output/
         │
         ▼
8. Display success message to user
```

## Components

### Frontend (Streamlit)
- `app.py` - Main application entry point
- `admin_interface.py` - Admin page for uploading PDFs
- `run_web.py` - Script to launch the web server

### Backend
- `database_manager.py` - Database abstraction layer
- `utils.py` - Utility functions (PDF processing, AI calls)

### Infrastructure
- Supabase - PostgreSQL database hosting
- Google Gemini API - AI for PDF to Markdown conversion
- Streamlit - Web framework and UI rendering
