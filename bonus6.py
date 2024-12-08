contents = ["All carrots are to be sliced",
            "The carrots were reportedly sliced",
            "The carrots have been presented as sliced"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)