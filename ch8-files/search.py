fname = input("Enter the file name:")

try:
    fhandle = open(fname)
except:
    print("File cannot be opened:",fname)
    exit()

count = 0
for line in fhandle:
    if line.startswith("Subject:"):
        count += 1

fhandle.close()
print("There were ", count, "subject lines in", fname)