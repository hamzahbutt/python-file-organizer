# Python File Organizer

A simple Python script that automatically organizes files in a folder into subfolders based on their file extensions (e.g. images go into `Images/`, PDFs go into `Documents/`, etc.). It also keeps a log of every file it moves.

## Features

- Sorts files into categorized folders automatically
- Supports a wide range of file types (documents, images, videos, audio, archives, programs, and code files)
- Creates destination folders automatically if they don't exist
- Any file type it doesn't recognize goes into an `Others` folder
- Generates a `changes.txt` log file recording what was moved and where

## Technologies Used

- Python 3
- `os` (built-in)
- `shutil` (built-in)

No external dependencies — just Python itself.

## How to Run

1. Clone this repository (or just download `file_organizer.py`).
2. Run the script:

```bash
python file_organizer.py
```

3. When prompted, enter the full path to the folder you want to organize:

```
Give the source: C:\Users\YourName\Downloads
```

4. The script will sort the files in that folder and create a `changes.txt` file inside it listing every file that was moved.

## Supported File Types

| Category | Extensions |
|----------|------------|
| Documents | `.pdf` `.docx` `.doc` `.txt` `.rtf` `.pages` `.xlsx` `.xls` `.csv` `.pptx` `.ppt` `.key` |
| Images | `.jpg` `.jpeg` `.png` `.gif` `.svg` `.webp` `.bmp` `.ico` |
| Videos | `.mp4` `.mov` `.avi` `.mkv` `.wmv` |
| Audios | `.mp3` `.wav` `.aac` `.flac` `.m4a` |
| Archives | `.zip` `.rar` `.7z` `.tar` `.gz` |
| Programs | `.exe` `.msi` `.dmg` `.pkg` |
| Code | `.py` `.js` `.html` `.css` `.json` |
| Others | Any file type not listed above |

## Notes

- The script only moves files that are directly inside the folder you give it (it doesn't touch files already inside subfolders).
- Running it multiple times on the same folder is safe — already-sorted files won't be picked up again since they're no longer in the top-level folder.

## Possible Future Improvements

- Add a "undo" option using the `changes.txt` log
- Add a command-line argument for the folder path instead of an input prompt
- Let users customize the extension-to-folder mapping via a config file