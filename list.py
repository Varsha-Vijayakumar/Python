lis=[]
print ("Welcome to Linked List ")
def start():
    print("Enter your option")
    print("1.Insertion")
    print("2.Deletion")
    print("3.Search")
    print("4.Update")
    print("5.Display")
    print("6.Exit")
    n=int(input())
    if(n==1):
        insertion()
    elif(n==2):
        if(len(lis) is not  0):
            deletion()
        else:
            print("List is empty")
    elif(n==3):
        if(len(lis) is not  0):
            searching()
        else:
            print("List is empty")
    elif(n==4):
        if(len(lis) is not  0):
            updation()
        else:
            print("List is empty")
    elif(n==5):
        if(len(lis) is not  0):
            displaying()
        else:
            print("List is empty")
    elif(n==6):
        exit()
    else:
        print("Invalid input")
        start()

def insertion():
    print("1.Insert at first")
    print("2.Insert at last")
    print("3.Insert anywhere between first and last")
    inn=int(input())
    val=int(input())
    if(inn==1):
        lis.insert(0,val)
        start()
    elif(inn==2):
        lis.insert(len(lis),val)
        start()
    elif(inn==3):
        print("Enter the position where you want to insert")
        ii=int(input())
        lis.insert(ii-1,val)
        start()
    else:
        print("Invalid input")
        start()
def deletion():
    print("1.Delete the first value")
    print("2.Delete the last value")
    print("3.Delete anywhere between first and last")
    inn=int(input())
    if(inn==1):
        del lis[0]
        start()
    elif(inn==2):
        del lis[len(lis)-1]
        start()
    elif(inn==3):
        print("Enter the value to be deleted")
        ii=int(input())
        if(ii in lis):
            lis.remove(ii)
            start()
        else:
            print("Invalid value")
            start()
    else:
        print("Invalid input")
        start()
def searching():
    print("Enter the value to be found")
    ii=int(intput())
    if(ii in lis):
        print("Value is present in the list")
        start()
    else:
        print("value not present in the list")
        start()
def updation():
    print("Enter which value need to be updated")
    inn=int(input())
    print("Enter the new value")
    new=int(input())
    if(inn in lis):
        for i in range(0,len(lis)):
            if(lis[i]==inn):
                lis[i]=new
                start()
    else:
        print("Value need to be updated is not in the list")
        start()

def displaying():
    print(lis)
    start()



start()
