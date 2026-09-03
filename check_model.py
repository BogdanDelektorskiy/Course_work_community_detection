import tarfile
from pathlib import Path

archive_path = "models/rubert-tiny2-custom.pth"
output_dir = Path("models")

files_to_extract = [
    "./epoch_64_encoder.pth",
    "./metrics.json",
]

with tarfile.open(archive_path, "r:*") as tar:
    for file_name in files_to_extract:
        print(f"Извлекаем: {file_name}")
        member = tar.getmember(file_name)
        
        with tar.extractfile(member) as source:
            output_path = output_dir / Path(file_name).name
            
            with open(output_path, "wb") as target:
                while chunk := source.read(8 * 1024 * 1024):
                    target.write(chunk)

print("\nГотово!")

for file_name in ["epoch_64_encoder.pth", "metrics.json"]:
    path = output_dir / file_name
    print(f"{path}: {path.stat().st_size / 1024 / 1024:.2f} MB")