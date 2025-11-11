import os
from PIL import Image
import shutil
from tqdm import tqdm

def convert_images(source_dir, target_dir):
    """
    将源目录中的0000.jpg, 0001.jpg, ..., 0999.jpg文件
    转换为目标目录中的0.png, 1.png, ..., 999.png格式
    """
    # 创建目标目录（如果不存在）
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 处理0000.jpg到0999.jpg
    for i in tqdm(range(1000)):
        # 源文件名（带前导零）
        source_filename = f"{i:04d}.jpg"
        source_path = os.path.join(source_dir, source_filename)
        
        # 目标文件名（不带前导零）
        target_filename = f"{i}.png"
        target_path = os.path.join(target_dir, target_filename)
        
        # 检查源文件是否存在
        if not os.path.exists(source_path):
            print(f"Warning: {source_path} doesn't exist. Skipped.")
            continue
        
        try:
            # 打开图片并转换为PNG格式
            with Image.open(source_path) as img:
                # 转换为RGB模式（确保兼容性）
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                # 保存为PNG格式
                img.save(target_path, 'PNG')
            
        except Exception as e:
            print(f"Error when processing {source_path} :{str(e)}")

# 使用方法
if __name__ == "__main__":
    # 设置源目录和目标目录
    source_directory = 'images'  # 修改为您的原始图片目录
    target_directory = 'caption/test_images'  # 与示例代码相同的目标目录
    
    print("Transforming...")
    convert_images(source_directory, target_directory)
    print("Completed.")