import os
import shutil

foldExt = {
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".pages": "Documents",

    # Spreadsheets
    ".xlsx": "Documents",
    ".xls": "Documents",
    ".csv": "Documents",

    # Presentations
    ".pptx": "Documents",
    ".ppt": "Documents",
    ".key": "Documents",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".svg": "Images",
    ".webp": "Images",
    ".bmp": "Images",
    ".ico": "Images",

    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",

    # Audios
    ".mp3": "Audios",
    ".wav": "Audios",
    ".aac": "Audios",
    ".flac": "Audios",
    ".m4a": "Audios",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    # Executables / Installers
    ".exe": "Programs",
    ".msi": "Programs",
    ".dmg": "Programs",
    ".pkg": "Programs",

    # Code / Scripts
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".json": "Code"
}

while True:
    src = input("Give the source: ")

    if os.path.isdir(src):
        break
    else:
        print("Invalid path. Please enter a valid folder path.\n")

files = os.listdir(src)

with open(os.path.join(src, "changes.txt"), "w") as file:
    for f in files:
        if f == "changes.txt":
            continue
        if os.path.isfile(os.path.join(src, f)):
            ext = os.path.splitext(f)[1]
            folder = foldExt.get(ext, "Others")
            Tfile = os.path.join(src, f)
            target_folder_path = os.path.join(src, folder)

            if not os.path.exists(target_folder_path):
                os.mkdir(target_folder_path)

            shutil.move(Tfile, target_folder_path)

            file.write("The file " + f + " was moved to " + folder + "\n")



