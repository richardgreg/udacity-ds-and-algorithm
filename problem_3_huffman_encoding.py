import sys

# create two nodes. one for 

class Node():
    """docstring for Node"""
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None


    def get_value(self):
        return self.value

    def set_value(self, value):
        "Set the value of a node"
        self.value = value
        
    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right
        
    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node


    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

class State():
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0

def huffman_encoding(data):
    """
    Encodes data
    """
    # For an empty case
    if len(data) == 0:
        return "", None

    # Create a frequency table
    frequency_table = dict() # A hashmap that will store the priority queue
    for char in data:
        if char not in frequency_table:
            frequency_table[char] = 1
        else:
            frequency_table[char]+=1

    if len(frequency_table) == 1:
        node = Node(data[0], frequency_table[data[0]])
        return data, node

    # 
    while len(frequency_table) > 1:
        # Get the lowest value from the table and make it a node
        min_freq = min(frequency_table, key=frequency_table.get)

        # if the key is a str object, make the char and freq a node
        if type(min_freq) is str:
            left_child = Node(min_freq, frequency_table[min_freq])

        # Else, left child is already node
        else:
            left_child = min_freq

        frequency_table.pop(min_freq) #remove from priorty queue

        # Do the same for the second lowest value
        min_freq = min(frequency_table, key=frequency_table.get)
        if type(min_freq) is str:
            right_child = Node(min_freq, frequency_table[min_freq])
        else:
            right_child = min_freq

        frequency_table.pop(min_freq)

        # Creat a new node from the two lowest frequencies
        node = Node(None, left_child.frequency + right_child.frequency)

        # Set the two lowest freq as its children
        node.set_left_child(left_child)
        node.set_right_child(right_child)

        # Append node to the priority queue
        frequency_table[node] = left_child.frequency + right_child.frequency

    huffman_tree = node

    encoded_table = dict() # A dict to store the encoded data
    bin_string = "" # A string to hold the binary codes as the trees as traversed
    state = State(node)
    stack = Stack()
    stack.push(state)

    # Traverse the huffman tree and create a table with char and bits
    while node:
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            bin_string+= '0'
            node = node.get_left_child()
            state = State(node)
            stack.push(state)
        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            bin_string+='1'
            node = node.get_right_child()
            state = State(node)
            stack.push(state)
        else:
            if node.character:
                encoded_table[node.character] = bin_string
            stack.pop()
            bin_string = bin_string[:-1]
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    encoded_data = ""
    for char in data:
        encoded_data+=encoded_table[char]
    
    return encoded_data, huffman_tree

def huffman_decoding(data,tree):
    # For an empty case
    if len(data) == 0 and tree == None:
        return ""

    # For a single character
    if '1' not in data and '0' not in data:
        return data

    decoded_str = ""
    node = tree

    for char in data:
        if char == '0':
            node = node.get_left_child()
        elif char == '1':
            node = node.get_right_child()

        if node.left is None and node.right is None:
            decoded_str+=node.character
            node = tree  

    return decoded_str


if __name__ == "__main__":
    # codes = {}

    # Test Case 0
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 1
    a_great_sentence = """
    In general, a data compression algorithm reduces the amount of memory (bits) required
    to represent a message (data). The compressed data, in turn, helps to reduce the
    transmission time from a sender to receiver. The sender encodes the data, and the
    receiver decodes the encoded data. As part of this problem, you have to implement the
    logic for both encoding and decoding. 
    """

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 2
    a_great_sentence = "aaaaaaaaaaaaaaaaa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 3
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))





    x,y = huffman_encoding('aaaan')
    z = huffman_decoding(x,y)

    print(z)
