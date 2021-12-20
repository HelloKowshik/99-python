from deque import Deque

def palindrome(word):
    dq = Deque()
    if len(word) > 1:
        for char in word:
            dq.add_rear(char)

        equal = True
    
        while dq.size() > 1 and equal:
            char1 = dq.remove_front()
            char2 = dq.remove_rear()
            if char1 == char2:
                equal = True
            else:
                equal = False
        return equal

    else:
        return 'The word should consist of at least two chars.'            



if __name__ == '__main__':
    while True:
        print('Please, input the word to check:')
        print(palindrome(input()))           

