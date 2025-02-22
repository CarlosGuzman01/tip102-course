class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value.character, end=" -> " if current.next else "\n")
        current = current.next

        
def arr_to_ll(arr):
    pass

'''

#Understand

this is a linkedlist problem no extra data structs

#match

we need to use a linkedlist

#plan

we get an array

we convert the elements to a linkedlist 

we return the head of the linkedlist



'''

#implement

def arr_to_ll(arr):

    for x in arr:
        node = Node(x, )


