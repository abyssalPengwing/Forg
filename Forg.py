import os
import shutil
import tkinter as tk
from tkinter import filedialog

file_types = {
        "Documents": [".pdf", ".txt", ".docx", ".pptx", ".xlsx", ".csv", ".odt", ".rtf", ".tex", ".log"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".ico", ".heic"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".3gp", ".m4v"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".aiff", ".alac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".dmg"],
        "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".php", ".rb", ".go", ".ts", ".sh", ".bat"],
        "Executables": [".exe", ".msi", ".apk", ".bin", ".app", ".deb", ".rpm"],
        "Spreadsheets": [".xls", ".xlsx", ".ods"],
        "Presentations": [".ppt", ".pptx", ".key"],
        "Ebooks": [".epub", ".mobi", ".azw", ".azw3"],
        "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    }

def get_folder_path():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Folder to Organize")
    return folder_path

def organize_folder(path):
    misc_folder = os.path.join(path, "Miscellaneous")
    os.makedirs(misc_folder, exist_ok=True)

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if filename.endswith(tuple(extensions)):
                    folder_path = os.path.join(path, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved {filename} to {os.path.join(folder_path, filename)}")
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(misc_folder, filename))
                print(f"Moved {filename} to Miscellaneous")


folder_to_organize = get_folder_path()
if folder_to_organize:
    organize_folder(folder_to_organize)
else:
    print("No folder selected. Exiting...")
