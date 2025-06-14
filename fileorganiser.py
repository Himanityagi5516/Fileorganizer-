import os
import shutil

def organize_directory_by_extension(folder_path):
    # Map common file extensions to folder names
    extension_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Music': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mov', '.avi']
    }

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in extension_map.items():
                if file_ext in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    moved = True
                    break
            if not moved:
                # Move files with unknown extensions to "Others"
                target_folder = os.path.join(folder_path, "Others")
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))

if __name__ == "__main__":
    path = input("Enter the path to the directory you wish to organize: ")
    if os.path.isdir(path):
        organize_directory_by_extension(path)
        print("Directory organized successfully!")
    else:
        print("Invalid directory path.")