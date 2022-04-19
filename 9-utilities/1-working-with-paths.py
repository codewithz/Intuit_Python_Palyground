from pathlib import  Path

path1=Path("D:\\Zartab\\Trainings")
print(path1)

current_path=Path()
print(current_path)

path2=Path("../ecommerce/__init__.py")
print(path2)

combined=Path()/Path("test")
print(combined)

print("Exists",path2.exists())
print("Exists",combined.exists())
print("Is FIle",path2.is_file())
print("Is Dir",path2.is_dir())

print(path2.name)
print(path2.stem)
print(path2.suffix)
print(path2.parent)
print(path2.absolute())