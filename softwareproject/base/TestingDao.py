
def writingLine(str):
    print(str)
    file = open("testing.txt", "a")
    file.write(str)
    file.close()