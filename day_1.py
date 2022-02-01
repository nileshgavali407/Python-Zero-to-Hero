#Take Multiple Number As Input And Print The Sum

sum=0
while True:
   inputs = input()
   if inputs == "stop":
        break
   else:
        sum = sum+int(inputs)
print(sum)