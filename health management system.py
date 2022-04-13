def getdate():
    import datetime
    return datetime.datetime.now()
def take(k):
    if k==1:
        print("Enter 1 for food and 2 for exercise ")
        b=int(input())
        if b==1:
            text=input("type here\n")
            with open ("Rohan1.txt","a") as s:
                s.write(str([str(getdate())])+":"+text+"\n")
            print("Written successfully")
        elif b==2:
            text=input("type here\n")
            with open ("Rohan2.txt","a") as s:
                s.write(str([str(getdate())])+":"+text+"\n")
            print("Written successfully")        

    elif k==2:
        print("Enter 1 for food and 2 for exercise ")
        b=int(input())
        if b==1:
            text=input("type here\n")
            with open ("Saksham1.txt","a") as s:
                s.write(str([str(getdate())])+":"+text+"\n")
            print("Written successfully")
        elif b==2:
            text=input("type here\n")
            with open ("Saksham2.txt","a") as s:
                s.write(str([str(getdate())])+":"+text+"\n")
            print("Written successfully") 

def retrieve(k):
    if k==1:
        print("Enter 1 for food and 2 for exercise ")
        b=int(input())
        if b==1:
            
            with open ("Rohan1.txt") as s:
                for i in s:
                    print(i)    
            
        elif b==2:
            
            with open ("Rohan2.txt") as s:
                for i in s:
                    print(i)

print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    c = int(input("Press 1 for Rohan 2 for Saksham "))
    take(c)
else:
    c = int(input("Press 1 for Rohan 2 for Saksham "))
    retrieve(c)



