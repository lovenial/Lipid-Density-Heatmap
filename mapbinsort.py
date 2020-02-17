import csv

firstFrame = input("Starting Frame: ")
frameCount = input("Number of Frames: ")
binsize = input("Bin Size: ")
molecules = 128

coordsFile = open("y50coords", "r")
csvFile = open("y50hist.csv", "w")
coordsArray = []

#collects all coordinates being used into one array
lines = coordsFile.read().splitlines()
for frame in range(firstFrame-1,(frameCount+firstFrame-1)):
    for coord in range(0+frame*molecules+frame,molecules+frame*molecules+frame):
        coordsArray.append(float(lines[coord]))

#finds shift for negatives
min = 0
for coord in coordsArray:
    if(coord<min):
        min = coord
shift = min*(-1)

#modifies for negatives, applies shift to data
shiftedArray = []
for coord in coordsArray:
    shiftedArray.append(float(coord)+shift)

#calculates bin for each value
binArray = []
for coord in shiftedArray:
    binArray.append(int(coord/binsize))

#gets maximum bin for density array size
max = 1
for coord in binArray:
    if(coord>max):
        max = coord
print("\nMax: " +str(max))

#generates an array of lists to hold all data
matrixArray = []
for i in range(0,max+1):
    matrixArray.append([i])

#adds new column to matrix array
for f in range(0, frameCount):
    for i in range(0,max+1):
        matrixArray[i].append(0)


#sorts bin values into matrix array and counts density
frame = 1
coordcount = 0
for b in binArray:
    if(coordcount<molecules):
        matrixArray[b][frame] += 1
        coordcount += 1
    else:
        frame += 1
        matrixArray[b][frame] += 1
        coordcount = 1

print("\nMatrix array: ")
print(matrixArray)

#exports matrixArray into CSV file to be graphed
for frame in range(0, frameCount):
    csvFile.write(", ")
csvFile.write("\n")
with csvFile as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(matrixArray)
