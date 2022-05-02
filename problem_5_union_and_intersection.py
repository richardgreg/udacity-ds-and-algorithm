class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def make_set(linked_list):
    """
    Takes the values in a linked list and puts them into a set
    data structure
    """

    set_data = set()
    node = linked_list.head
    for _ in range(linked_list.size()):
        set_data.add(node.value)
        node = node.next

    return set_data

def union(llist_1, llist_2):

    united_ll = LinkedList()

    # return an empty linked list if both objects are empty
    if llist_1 is None and llist_2 is None:
        return united_ll


    # return the values of one linked list if the other is empty
    if llist_1 is None:
        ll = llist_2
    elif llist_2 is None:
        ll = llist_1

        set_data = make_set(ll)
        for element in set_data:
            united_ll.append(element)

        return united_ll


    ll_1_value = make_set(llist_1)
    ll_2_value = make_set(llist_2)

    combined_set = ll_1_value.union(ll_2_value)

    for value in combined_set:
        united_ll.append(value)

    return united_ll

def intersection(llist_1, llist_2):
    
    intersection_ll = LinkedList()
    intersection_set = set()


    # Retrieve the values in each Linked List and put into a set
    ll_1_set = make_set(llist_1)
    ll_2_set = make_set(llist_2)

    for element in ll_1_set:
        if element in ll_2_set:
            intersection_set.add(element)

    for element in ll_2_set:
        if element in ll_1_set:
            intersection_set.add(element)

    for element in intersection_set:
        intersection_ll.append(element)

    return intersection_ll

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_1,linked_list_2))
# 4 -> 21 -> 6 -> 

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


# Test Case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test Case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [None]
element_2 = [None]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))

