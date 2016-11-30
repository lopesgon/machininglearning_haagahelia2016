
def writingLine(str):
    print(str)
    file = open("log.txt", "a")
    file.write(str)
    file.close()