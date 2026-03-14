score = 0

print("welcome to quiz game")

print("\n 1. what is capital of india?")
print("1.mumbai")
print("2.delhi")
print("3.kolkata")
print("4.nagpur")

ans = int(input("Enter you answer:"))

if ans == 2:
    print("correct!")
    score += 1

else:
    print("wrong!") 

print("\n 2.captain of indian team when indian cricket team win their maiden Odi wc trophy?")
print("1.sunil gavaskar")
print("2.ravi shastri")
print("3.kapil dev")
print("4.amarnath")

ans = int(input("Enter your answer:"))

if ans ==3:
    print("correct!")

    score +=1
else:
    print("wrong!")

    print("\n 3.how many state present in india?")
print("1.32")
print("2.24")
print("3.27")
print("4.28")

ans = int(input("Enter your answer:"))

if ans ==4:
    print("correct!")

    score +=1
else:
    print("wrong!")


print("Final score",score)
    
