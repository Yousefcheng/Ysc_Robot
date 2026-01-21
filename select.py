import os
import shutil

def copy_jpg_files_from_txt(txt_file, source_folder, destination_folder):
    # 读取存储文件名的文本文件
    with open(txt_file, 'r') as file:
        file_names = file.readlines()
    
    for file_name in file_names:
        file_name = file_name.strip()  # 去除换行符

        # 构建JPG文件的完整路径
        jpg_file_path = os.path.join(source_folder, file_name + '.jpg')

        # 检查JPG文件是否存在
        if os.path.exists(jpg_file_path):
            # 构建目标文件夹中的目标路径
            destination_path = os.path.join(destination_folder, os.path.basename(jpg_file_path))

            # 复制JPG文件到目标文件夹
            shutil.copy(jpg_file_path, destination_path)
            print(f"已复制文件: {jpg_file_path} 到 {destination_path}")

if __name__ == "__main__":
    # 请将以下路径替换为包含文件名的文本文件的路径
    txt_file = "/path/to/your/file.txt"

    # 请将以下路径替换为JPG文件所在的文件夹路径
    source_folder = "/path/to/source/folder"

    # 请将以下路径替换为目标文件夹路径
    destination_folder = "/path/to/destination/folder"

    copy_jpg_files_from_txt(txt_file, source_folder, destination_folder)