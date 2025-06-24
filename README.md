# Professional File Manager

A Python-based professional file manager with a graphical user interface (GUI) built using Tkinter. This application allows users to manage files and folders visually with features like preview, open, copy, paste, rename, delete, move, and file properties.

## Features

- 🗂️ Directory navigation
- 📄 File and folder listing with icons
- 🖼️ Image preview (JPG, JPEG, PNG)
- 📁 Folder and document icons for unsupported previews (PDF, DOCX, etc.)
- 📂 Create folders
- 📋 Copy and paste files
- ✂️ Move and rename files
- ❌ Delete files
- ℹ️ File properties (size, type, timestamps)
- 🖥️ Open files with default applications

## Technologies Used

- Python 3.x
- Tkinter (GUI framework)
- Pillow (PIL) for image handling
- OS, shutil, platform, datetime (standard libraries)

## File Structure

- `main.py`: Launches the application.
- `file_manager_app.py`: Main GUI layout and logic.
- `file_actions.py`: Handles file actions like copy, move, rename, etc.
- `file_ops.py`: Low-level OS operations (open, delete, list).
- `previewer.py`: Controls the preview panel for images, folders, and icons.
- `styles.py`: Custom theme setup.

## How to Run

1. Install dependencies:
```
pip install pillow
```

2. Run the application:
```
python main.py
```

## Team Members and Roles

- **Member 1**: Designed the main GUI in `file_manager_app.py`
- **Member 2**: Implemented file operations in `file_actions.py`
- **Member 3**: Developed helper functions in `file_ops.py`
- **Member 4**: Created the preview logic in `previewer.py`

## Notes

- Only JPG, JPEG, PNG are previewed.
- PDF, DOCX, folders show representative icons.
- Ensure `Pillow` is installed for image preview.

## License

This is a student-level project created for learning and demonstration purposes.
