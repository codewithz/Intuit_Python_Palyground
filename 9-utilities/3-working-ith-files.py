from pathlib import  Path
from time import ctime
import  shutil

path=Path("mydata.txt")
print("Stats",path.stat())
print("Creation Time",ctime(path.stat().st_ctime))

# Reading Data from File

data_from_file=path.read_text()
print("Data from File is \n\n")
print(data_from_file)
print("------------------------------")

path_to_write=Path("some_file.txt")
path_to_write.write_text(data_from_file)
print("Done")

source=Path("cat.png")
target=Path("copy_cat.png")
shutil.copy(source,target)