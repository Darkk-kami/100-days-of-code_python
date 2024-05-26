print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = name1 + name2
name = name.lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

l = name.count("l")
o = name.count("o")
v = name.count("v")

true = (t + r + u + e)
love = (l + o + v + e)

love_check = str(true) + str(love)
love_check = int(love_check)

if love_check < 10 or love_check > 90:
    print (f"Your score is {love_check}, you go together like coke and mentos.")

elif love_check > 40 and love_check < 50:
    print(f"Your score is {love_check}, you are alright together.")

else:
    print(f"Your score is {love_check}.")

