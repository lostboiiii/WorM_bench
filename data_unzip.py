import zipfile
import os
from tqdm import tqdm

curr_path = os.path.abspath(os.path.dirname(__file__))
zip_file = "wm_bench_data.zip"

# 创建解压目录
extract_folder = os.path.join(curr_path, os.path.splitext(zip_file)[0])

# 确保目标解压目录存在
os.makedirs(extract_folder, exist_ok=True)

# 解压文件并显示进度
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    # 使用 tqdm 包装 zip_ref.infolist() 以显示进度条
    for file in tqdm(zip_ref.infolist(), desc="解压进度", unit="file"):
        zip_ref.extract(file, extract_folder)

print(f"已解压 {zip_file} 到 {extract_folder}/")
