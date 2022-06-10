# this is a code question from the Math Olympiad
# By : Yara Elsakka

# Test Rnage Values
#numbers = range(1, 10)
#for data in numbers:
#    print(data)

start_num = 0
end_num = 100000
sum = 0
for n in range(start_num,end_num+1):
    sum = sum + int(n)
    #print(sum)
print("SUM of first ", n, "numbers is: ", sum )


# end of code