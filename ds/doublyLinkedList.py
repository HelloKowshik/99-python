class Node:
    def __init__(self, item=None, previous_node=None, next_node=None):
        self.item = item
        self.previous_node = previous_node
        self.next_node = next_node

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def appendleft(self, item):
        new_node = Node(item)
        new_node.previous_node = None
        new_node.next_node = self.head
        if self.head is None:
            self.tail = new_node
        else:
            self.head.previous_node = new_node
        self.head = new_node
    
    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.previous_node = self.tail
            new_node.next_node = None
            self.tail.next_node = new_node
            self.tail = new_node

    def insert(self,position, item):
        if position == 0:
            self.appendleft(item)
            print(f'{item}, inserted at position: {position}')
        elif position == self.size():
            self.append(item)
            print(f'{item}, inserted at position: {position}')
        elif position > self.size():
            print('Out of Boundary!')
        else:
            current = self.head
            index = 0
            while current:
                if index != position:
                    previous = current
                    current = current.next_node
                    index += 1
                else:
                    new_node = Node(item, previous, current)
                    previous.next_node = new_node
                    current.previous_node = new_node
                    current = False
                    print(f'{item}, inserted at position: {position}')
    
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False                            
                
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count 
    
    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.item == item:
                return index
            else:
                current = current.next_node
                index += 1
        return None
    
    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.item == item:
                found = True
            else:
                current = current.next_node
        if current is None:
            print('Item not Found!')
        return found
    
    def popleft(self):
        if self.is_empty():
            print('Empty List!')
        else:
            current = self.head
            next_node = current.next_node
            if next_node is None:
                temp = current.item
                del current
                self.head = self.tail = None
                return temp
            else:
                temp = current.item
                del current
                next_node.previous_node = None
                self.head = next_node
                return temp

    def pop(self):
        if self.is_empty():
            print('Empty List!')
        else:
            current = self.tail
            previous = current.previous_node
            if previous is None:
                temp = current.item
                del current
                self.head = self.tail = None
                return temp
            else:
                temp = current.item
                del current
                previous.next_node = None
                self.tail = previous
                return temp

    def remove(self, item):
        if self.is_empty():
            print('Empty List!')
        else:
            current = self.head
            previous = None
            found = False
            while current and not found:
                if current.item == item:
                    found = true
                else:
                    previous = current
                    current = current.next_node
            if current is None:
                print('Item not Found!')
            elif previous is None:
                self.popleft()   
                print(item, ': Removed')
            else:
                temp = current.next_node
                del current
                print(item, ': Removed')
                previous.next_node = temp
                temp.previous_node = previous

    def printlist(self):
        if self.is_empty():
            print("Empty list")
        else:
            current = self.head
            print(current.item, end=',')
            while current.next_node:
                current = current.next_node
                if current is self.head:
                    break
                else:
                    print(current.item, end=',')
        print()            

def main():
    s_list = DoublyLinkedList()
    while True:
        print("1. Append to Left \n2. Append \n3. Insert \n4. Get Size \n5. Search \n6. Get Index \n7. Remove \n8. Pop from Left \n9. Pop \n10. Print List \n11. Quit")
        print("\nWhat do you wanna do now?")
        print('-----------------------------------')
        case = int(input())
        print('-----------------------------------')
        if case == 1:
            print("Input item, you wanna append to left of list:")
            item = input()
            s_list.appendleft(item)
            print("Congrats!", item, "has been added.")
        elif case == 2:
            print("Input item, you wanna append to list:")
            item = input()
            s_list.append(item)
            print("Congrats!", item, "has been appended.")
        elif case == 3:
            print("Input position:")
            position = int(input())
            print("Input item, you wanna push to list:")
            item = input()
            s_list.insert(position, item)
        elif case == 4:
            print("There are", s_list.size(), "items in the list.")
        elif case == 5:
            print("Input item, you wanna search in list:")
            item = input()
            print(s_list.search(item))
        elif case == 6:
            print("Input item, you wanna know its index:")
            item = input()
            index = s_list.index(item)
            print(item, "is in index number", index)
        elif case == 7:
            if s_list.is_empty():
                print("Empty list")
            else:
                print("Input item, you wanna remove:")
                item = input()
                s_list.remove(item)
        elif case == 8:
            if s_list.is_empty():
                print("Empty list")
            else:
                item = s_list.popleft()
                print(item, "removed")
        elif case == 9:
            if s_list.is_empty():
                print("Empty list")
            else:
                item = s_list.pop()
                print(item, "removed")
        elif case == 10:
            if s_list.is_empty():
                print("Empty list")
            else:
                s_list.printlist()
        elif case == 11:
            print("Programe exit.")
            quit()
        else:
            print("Wrong Choice.")
            main()

if __name__ == '__main__':
    main()
