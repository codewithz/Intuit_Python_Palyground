from pathlib import  Path

path=Path("../ecommerce")
test_path=Path("zartab")
# path.exists()
# test_path.mkdir()
# test_path.rmdir()
# test_path.rename("test")

print(path.iterdir())

for p in path.iterdir():
    print(p)

files=[p for p in path.iterdir()]
print(files)

directories=[p for p in path.iterdir() if p.is_dir()]
print(directories)