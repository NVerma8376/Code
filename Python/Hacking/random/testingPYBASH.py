import os

for i in range(10):
    pref = str(i)
    comm = "echo hello > Python/Hacking/random/.txt"
    index = comm.find(".txt")
    outComm = comm[:index] + pref + comm[index:]
    
    os.system(outComm)