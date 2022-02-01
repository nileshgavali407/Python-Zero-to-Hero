lottery  = "hello coders"
# 'h' or 'e' or 'o' or 'c' or 'd'

print("choose correct character of the word '",lottery,"' to win the lottery")
inputs = input(" ").lower()

if inputs == "h" or inputs == "e" or inputs == "o" or inputs == "c" or inputs == "d":
    print("congratulation,you win thwe lottery")
else:
    print("sorry, You didn't win the lottery")