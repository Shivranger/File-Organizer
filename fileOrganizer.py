import sys, os, shutil

n = len(sys.argv)
if n == 1:
    print("python fileOrganizer.py <keyword> <folder_name>")
    exit()

searchTerm = sys.argv[1]
folderName = sys.argv[2]

if not os.path.exists(folderName):
    os.mkdir(folderName)
else: 
    print("./" + folderName + " exists...")

for item in os.listdir():
    if searchTerm in item: 
        print("Moving " + item + "to" + folderName + "...")
        shutil.move(item, "./" + folderName)

print("Done!")