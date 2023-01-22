import os
# Description: Create a symbolic link
while True:
    inp = input("Path = ")
    data = inp.replace("/", "\\")
    data = data.replace("\"", "")

    comm = "mklink " + "\"A:\\" + data.split("\\")[-1] + "\" \"" + data + "\"" + " /j"

    os.system(comm)
    print(comm + "\n")