from time import sleep
p=lambda s:[(print(c,end='',flush=1),sleep(.01))for c in s]
ops={'+':lambda a,b:a+b,'-':lambda a,b:a-b,'/':lambda a,b:a/b if b else 0,'*':lambda a,b:a*b,'^':lambda a,b:a**b}

p("Ugh, Well someone obviously cant do math. Welcome to the Meh-culator... \n")
while 1:
    p("Enter the first number: ");a=input()
    p("Enter the second...: ");b=input()
    while not(a.isdigit() and b.isdigit()):
        p("You didn't give me a number, you bothered opening a calculator and didn't give me a number to calculate... Try that again and do it right this time and DONT TYPE OUT THE NUMBER.\n")
        p("Enter the first number: ");a=input()
        p("Enter the second...: ");b=input()
    a=int(a);b=int(b)
    while 1:
        p("What calculation are you making me do?(+, -, /, *, ^): ");c=input()
        if c in ops:
            r=ops[c](a,b)
            p(f"{a} {c} {b} is {r}, Happy?\n")
            break
        else:
            p("You didnt give me a valid calculation type, use the listed characters that I GAVE YOU and try again.\n")
    p("Do you want me to do more calculations for you (please dont), Yes(Y) or No(N): ")
    d=input().lower()
    if d in('y','yes'):continue
    elif d in('n','no'):break
    else:
        print("You didnt even answer the question how I asked you too, you cant even do a yes or no question correctly, seriously?")
        break
# 2678 --> 1364 characters 