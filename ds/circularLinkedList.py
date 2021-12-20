class Node:
    def __init__(self, item=None, next_node=None):
        self.item = item
        self.next_node = next_node


class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head

    def appendleft(self, item):
        new_node = Node(item)
        new_node.next_node = self.head
        current = self.head
        if self.head is not None:
            while current.next_node is not self.head:
                current = current.next_node
            current.next_node = new_node
        else:
            new_node.next_node = new_node
        self.head = new_node

    def append(self, item):
        new_node = Node(item)
        current = self.head
        if current:
            while True:
                if current.next_node is self.head:
                    current.next_node = new_node
                    new_node.next_node = self.head
                    break
                else:
                    current = current.next_node
        else:
            self.head = new_node
            new_node.next_node = new_node  

    def insert(self, position, item):
        if position == 0:
            self.appendleft(item)
            print(item, "inserted to position", position)
        elif position == self.size():
            self.append(item)
            print(item, "inserted to position", position)
        elif position > self.size():
            print("Index out of range")
        else:
            current = self.head
            index = 0
            while current:
                if index != position:
                    previous = current
                    current = current.next_node
                    index += 1
                else:
                    new_node = Node(item, current)
                    previous.next_node = new_node
                    current = False
                    print(item, "inserted to position", position)              

    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            if current.next_node is self.head:
                current = False
            else:
                current = current.next_node
        return count

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.item == item:
                return index
            elif current.next_node is self.head:
                break
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
            elif current.next_node is self.head:
                current = False
            else:
                current = current.next_node
        if current is None:
            print("Item not found")
        return found

    def popleft(self):
        if self.is_empty():
            print("Empty list")
        else:
            current = self.head
            temp = current.item
            if current.next_node is self.head:
                self.head = None
            else:
                self.head = current.next_node
                next_node = self.head
                while next_node.next_node is not current:
                    next_node = next_node.next_node
                next_node.next_node = self.head
            del current
            return temp

    def pop(self):
        if self.is_empty():
            print("Empty list")
        else:
            current = self.head
            previous = None
            while current.next_node is not self.head:
                previous = current
                current = current.next_node
            if current == self.head:
                self.head = None
            else:
                previous.next_node = self.head
            temp = current.item
            del current
            return temp 

    def remove(self, item):
        if self.is_empty():
            print("Empty list")
        else:
            current = self.head
            previous = None
            found = False
            while current and not found:
                if current.item == item:
                    found = True
                elif current.next_node is self.head:
                    current = None
                else:
                    previous = current
                    current = current.next_node
            if current is None:
                print("Item not found")
            elif previous is None:
                self.popleft()
                print(item, "removed")
            else:
                temp = current.next_node
                del current
                print(item, "removed")
                previous.next_node = temp

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
    s_list = CircularLinkedList()
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
