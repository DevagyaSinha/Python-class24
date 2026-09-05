input("set a bit-or,turn the switch on")
print("5=",bin(5)[2:])
print("5|2=",bin(5|2)[2:])

input("set a bit-and,turn the switch on")
print("7=",bin(7)[2:])
print("7&5=",bin(7&5)[2:])

n=int(input("enter your number(try 4 or 6 )"))
guess=input("is your number power of 2 or not ")
input("power of 2 -then only 1 bit is on")
if n>0 and (n & (n - 1))==0:
    print(n,",binary",bin(n)[2:],"power of 2, your guess is right ", guess)
else:
    print(n,",binary",bin(n)[2:],"not a power of 2, your guess is wrong ", guess)