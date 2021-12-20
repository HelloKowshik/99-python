class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            return 'Queue is Empty!'
        else:
            return self.queue.pop(0)

def main():
    q = Queue()
    while True:
        print("1. Enqueue \n2. Dequeue \n3. Show \n4. Quit")
        print("\nChoose your Option.")
        case = int(input())
        if case == 1:
            item = input('Input Item: ')
            q.enqueue(item)
            print('Item pushed!')
        elif case == 2:
            print(q.dequeue())
        elif case == 3:
            if q.is_empty():
                print('Stack is EMPTY!')
            else:
                print(q.queue)
        elif case == 4:
            print('Exit from the Program!')
            quit()                           
        else:
            print('Wrong Choice!')
            main()    

if __name__ == '__main__':
    main()                                                
