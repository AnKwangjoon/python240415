import os
import shutil

# 다운로드된 폴더 경로
download_folder = "c:\\Users\\student\\Downloads"

# 목적지 폴더들
dest_folders = {
    "images": "c:\\Users\\student\\Downloads\\images",
    "data": "c:\\Users\\student\\Downloads\\data",
    "docs": "c:\\Users\\student\\Downloads\\docs",
    "archive": "c:\\Users\\student\\Downloads\\archive"
}

# 폴더가 없으면 생성
for folder in dest_folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# 이동할 파일 확장자별로 정의
file_types = {
    "images": [".jpg", ".jpeg"],
    "data": [".csv", ".xlsx"],
    "docs": [".txt", ".doc", ".pdf"],
    "archive": [".zip"]
}

# 파일 이동
for folder_name, extensions in file_types.items():
    destination = dest_folders[folder_name]
    for file in os.listdir(download_folder):
        for ext in extensions:
            if file.lower().endswith(ext):
                file_path = os.path.join(download_folder, file)
                shutil.move(file_path, destination)
                print(f"Moved {file} to {destination}")
