filesnames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filesnames:
    filename = filename.replace('.', '-', 1)
    print(filename)