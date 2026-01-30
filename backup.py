import os, shutil

source = r"D:\ransom_test"
backup = "backup"

os.makedirs(backup, exist_ok=True)

for file in os.listdir(source):
    src_path = os.path.join(source, file)
    dst_path = os.path.join(backup, file)

    if os.path.isfile(src_path):
        shutil.copy(src_path, dst_path)
        print("Backed up:", file)

print("Backup completed.")
