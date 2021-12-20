class Deque:
    def __init__(self):
        self.deque = []

    def size(self):
        return len(self.deque)

    def is_empty(self):
        if self.size() > 0:
            return False
        else:
            return True
    
    def add_front(self, item):
        return self.deque.insert(0, item)  

    def add_rear(self, item):
        return self.deque.append(item)

    def remove_front(self):
        if self.is_empty():
            return 'Dequeue is EMPTY!'
        else:
            return self.deque.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return 'Dequeue is EMPTY!'
        else:
            return self.deque.pop()

def main():
    dq = Deque()
    while True:
        print("1. Add at front \n2. Add at rear \n3. Remove from front \n4. Remove from rear \n5. Show \n6. Quit")
        print("\nChoose your Option.")
        case = int(input())
        if case == 1:
            item = input('Input Item: ')
            dq.add_front(item)
            print('Item pushed At Front!')
        elif case == 2:
            item = input('Input Item: ')
            dq.add_rear(item)
            print('Item pushed At Rear!')    
        elif case == 3:
            print(dq.remove_front())
        elif case == 4:
            print(dq.remove_rear())    
        elif case == 5:
            if dq.is_empty():
                print('Stack is EMPTY!')
            else:
                print(dq.deque)
        elif case == 6:
            print('Exit from the Program!')
            quit()                           
        else:
            print('Wrong Choice!')
            main()    

if __name__ == '__main__':
    main()                                                
