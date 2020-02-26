script = open("propcalc.R", "w")
firstFrame = input("Starting frame: ")
frameCount = input("Number of frames: ")

script.write("data <- data.frame(read.csv(\"yhist.csv\"))\n")
script.write("sink(\"proportions.txt\")\n")

for i in range(firstFrame, frameCount+firstFrame):
    script.write("f"+ str(i) +" <- data[,"+str(i+1)+"]\n")
    script.write("cat("+str(i)+", sum( (f"+str(i)+"==0)/length(f"+str(i)+")), \"\\n\", sep = \" \")\n")

script.write("sink()")
