

import os
import shutil
from pathlib import Path

source_dir = Path(r"C:\Users\Acer\Desktop\input")
output_dir = Path(r"C:\Users\Acer\Desktop\output")

# Buat folder input kalau belum ada
if not source_dir.exists():
    source_dir.mkdir(parents=True, exist_ok=True)
    print(f"Folder input dibuat: {source_dir}")
    print("Masukkan file ke folder tersebut lalu jalankan lagi.")

# Buat folder output kalau belum ada
output_dir.mkdir(parents=True, exist_ok=True)

# Cek apakah folder input punya file
if source_dir.exists():
    for file in source_dir.iterdir():
        if file.is_file():
            new_name = file.name.lower().replace(" ", "_")
            target = output_dir / new_name
            counter = 1

            while target.exists():
                name, ext = os.path.splitext(new_name)
                target = output_dir / f"{name}_{counter}{ext}"
                counter += 1

            shutil.move(str(file), str(target))
            print(f"Dipindahkan: {file.name} -> {target.name}")

    print("Proses selesai.")
