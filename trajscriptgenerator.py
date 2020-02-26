numEquilRuns = input("Number of equil run segments: ")
numRuns = input("Number of simulation run segments: ")
outputFileName = "fullwithequil.in"

newInputFile = open("fullwithequil.in", "w")

newInputFile.write("parm /scratch/lil34/POPE_8ILS/cho_ger.parm7\n")

for equilRun in range(1,numEquilRuns+1):
    newInputFile.write("trajin /scratch/lil34/POPE_8ILS/8-ILs/equil1/"+str(equilRun)+".run/mdcrd\n")

for run in range(2,numRuns+1):
    newInputFile.write("trajin /scratch/lil34/POPE_8ILS/8-ILs/"+str(run)+".run/mdcrd\n")

newInputFile.write("strip !(@P31)\ntrajout "+outputFileName+"\ngo\nquit")
