def enqueue(Q):
    a=input("Enter the number to be enqueued: ")
    Q.append(a)

def dequeue(Q):
    if len(Q)==0:
        print("The queue is empty.")
    else:
        Q.pop(0)

def queuerear(Q):
    if len(Q)==0:
        print("The queue is empty.")
    else:
        print(f"The last element is { Q[len(Q)-1] }")

def queuefront(Q):
    if len(Q)==0:
        print("The queue is empty")
    else:
        print(f"The first element is { Q[0] }")

def display(Q):
    if len(Q)==0:
        print("The queue is empty")
    else:
        for i in Q:
            print(i)

def main():
    
    Q=[]
    while True:
        
        print("1.Enqueue\n2.Dequeue\n3.QueueRear\n4.QueueFront\n5.Display\n6.Exit")
        num=int(input("Enter the operation to be performed: "))
        if num==1:
            enqueue(Q)
        elif num==2:
            dequeue(Q)
        elif num==3:
            queuerear(Q)
        elif num==4:
            queuefront(Q)
        elif num==5:
            display(Q)
        else:
            break

if __name__=="__main__":
    main()