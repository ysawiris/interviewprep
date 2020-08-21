# racecar
# mom

# ASk clarfying questions
# time and space complexity 
# walk them through your logic 


# self.held -> r -> a -> c 
from linked_list import LinkedList

def is_palindrome(ll):
    # define
    ll2 = ll.head
    stack = []
    
    # loop through LL and add all items to stack 
    while ll.head is not None:
        stack.append(ll.head.data)
        ll.head = ll.head.next 

    ll.head = ll2
    # print(ll)
    
    while ll.head is not None:
        current_value = stack.pop()
        if ll.head.data == current_value:
            print(ll.head)
            print(current_value)
            ll.head = ll.head.next 
        else:
            return False
            
    return True



if __name__ == "__main__":
    ll = LinkedList()
    word = 'racecar'
    for char in word:
        ll.append(char)
    # print(ll)
    print(is_palindrome(ll))
