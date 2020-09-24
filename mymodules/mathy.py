responses=["welcome, my name is Elsa and i am here for helping you","my name is krk","Thanks","Sorry, this is beyond my ability",
           "hello, what can i do for you","yes, he developed me and i am very happy and thanksfull for him"]
def extract_number_from_text(text):
    l=[]
    for t in text.split(" "):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def end():
    print(responses[2])
    input("press enter to exit")
    exit()
def myname():
    print(responses[1])
def hello():
    print(responses[4])
def sorry():
    print(responses[3])
def know():
    print(responses[5])
operations = {"ADD":add,"ADDITION":add,"SUBTRACTION":sub,"MINUS":sub,"SUBTRACT":sub,"MULTIPLY":multiply,
              "MULTIPLICATION":multiply,"PRODUCT":multiply,"DIVISION":division,"DIVIDE":division,"HCF":hcf,"LCM":lcm}
commands = {"NAME":myname,"END":end,"CLOSE":end,"EXIT":end,"HELLO":hello,"HII":hello,"HI":hello,"HEY":hello,
            "HEYY":hello,"KALIMUDDIN":know,"KALIM":know}
