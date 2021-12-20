class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, item):
        return self.stack.append(item)    

    def is_empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def pop(self):
        if self.is_empty():
            return 'Stack is EMPTY!'
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return 'Stack is EMPTY!'
        else:
            return self.stack[self.size() - 1]                               

def main():
    s = Stack()
    while True:
        print("1. Push \n2. Pop \n3. Peek \n4. Show \n5. Quit")
        print("\nChoose your Option.")
        case = int(input())
        if case == 1:
            item = input('Input Item: ')
            s.push(item)
            print('Item pushed!')
        elif case == 2:
            print(s.pop())
        elif case == 3:
            print(s.peek())
        elif case == 4:
            if s.is_empty():
                print('Stack is EMPTY!')
            else:
                print(s.stack)
        elif case == 5:
            print('Exit from the Program!')
            quit()                           
        else:
            print('Wrong Choice!')
            main()    

if __name__ == '__main__':
    main()            
