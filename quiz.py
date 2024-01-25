print("welcome Rahim")

playing = input("are u want to play game? ")
# here lower function i used this if we write yes in any case it will consider it yes

if playing.lower() != "yes":
    quit()

print("ok lets play")  
Score = 0  

answer = input("psu stands for: ").lower()
if answer == "power supply":
    print("correct")
    Score += 1
else:
    print("incorrect")        

answer = input("gpu stands for: ").lower()
if answer == "Graphic processing unit":
    print("correct")
    Score += 1
else:
    print("incorrect")        

answer = input("cpu stands for: ").lower()
if answer == "centeral processing unit":
    print("correct")
    Score += 1
else:
    print("incorrect")        


print("you got" + str(Score) + " marks")
print("you got "+ str((Score/3)*100)+"%.")