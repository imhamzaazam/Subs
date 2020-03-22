inputFile = "hole.txt"
outputFile = "download.bat"
stringToAPpend = "subliminal download -l en "

with open(inputFile, 'r') as inFile, open(outputFile, 'w') as outFile:
    for line in inFile:
        outFile.write(stringToAPpend+line)