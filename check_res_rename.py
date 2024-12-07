import os
import shutil
from PIL import Image

def remove_non_jpg_or_low_resolution_files(directory_path, min_width=500, min_height=500):
    files = os.listdir(directory_path)
    
    for filename in files:
        file_path = os.path.join(directory_path, filename)
        
        if not filename.lower().endswith('.jpg'):
            os.remove(file_path)
            print(f"Đã xóa {filename} vì không phải là tệp .jpg")
            continue
        
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                if width < min_width or height < min_height:
                    os.remove(file_path)
                    print(f"Đã xóa {filename} vì độ phân giải dưới {min_width}x{min_height}")
        except Exception as e:
            print(f"Không thể mở {filename}: {e}")

def rename_files_in_directory(directory_path):
    files = os.listdir(directory_path)
    
    files.sort()
    
    # Duyệt qua từng tệp và đổi tên
    for index, filename in enumerate(files, start=1):
        # Tạo đường dẫn đầy đủ cho tệp cũ và tệp mới
        old_file_path = os.path.join(directory_path, filename)
        
        # Đổi tên tạm thời để tránh xung đột
        temp_file_name = f"temp_{index}{os.path.splitext(filename)[1]}"
        temp_file_path = os.path.join(directory_path, temp_file_name)
        os.rename(old_file_path, temp_file_path)
    
    # Đổi tên từ tạm thời sang tên cuối cùng
    for index, temp_filename in enumerate(sorted(os.listdir(directory_path)), start=1):
        temp_file_path = os.path.join(directory_path, temp_filename)
        new_file_name = f"{index}{os.path.splitext(temp_filename)[1]}"
        new_file_path = os.path.join(directory_path, new_file_name)
        
        # Đổi tên tệp
        os.rename(temp_file_path, new_file_path)
        print(f"Đã đổi tên {temp_filename} thành {new_file_name}")
        
def create_and_split_data(directory_path):
    # Tạo thư mục data_book và các thư mục con train, test
    data_book_path = os.path.join(directory_path, 'data_book')
    train_path = os.path.join(data_book_path, 'train')
    test_path = os.path.join(data_book_path, 'test')
    
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(test_path, exist_ok=True)
    
    # Lấy danh sách các tệp .jpg
    files = [f for f in os.listdir(directory_path) if f.lower().endswith('.jpg')]
    files.sort()
    
    # Chia đôi danh sách tệp
    mid_index = len(files) // 2
    train_files = files[:mid_index]
    test_files = files[mid_index:]
    
    # Di chuyển và đổi tên tệp cho thư mục train
    for index, filename in enumerate(train_files, start=1):
        old_file_path = os.path.join(directory_path, filename)
        new_file_name = f"{index}{os.path.splitext(filename)[1]}"
        new_file_path = os.path.join(train_path, new_file_name)
        shutil.move(old_file_path, new_file_path)
        print(f"Đã di chuyển và đổi tên {filename} thành {new_file_name} trong thư mục train")
    
    # Di chuyển và đổi tên tệp cho thư mục test
    for index, filename in enumerate(test_files, start=1):
        old_file_path = os.path.join(directory_path, filename)
        new_file_name = f"{index}{os.path.splitext(filename)[1]}"
        new_file_path = os.path.join(test_path, new_file_name)
        shutil.move(old_file_path, new_file_path)
        print(f"Đã di chuyển và đổi tên {filename} thành {new_file_name} trong thư mục test")



# Đường dẫn tới thư mục cần đổi tên tệp
directory_path = 'download/electronic/1'
# remove_non_jpg_or_low_resolution_files(directory_path)
# rename_files_in_directory(directory_path)
create_and_split_data(directory_path)
