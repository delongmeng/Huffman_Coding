

# =============================================================================
# # Problem 3: Huffman Coding
# # The Huffman algorithm works by assigning codes that correspond to the relative 
# # frequency of each character for each character. The Huffman code can be of any 
# # length and does not require a prefix; therefore, this binary code can be visualized 
# # on a binary tree with each encoded character being stored on leafs.
# =============================================================================

# Here is one type of pseudocode for this coding schema:

# Take a string and determine the relevant frequencies of the characters.
# Build and sort a list of tuples from lowest to highest frequencies.
# Build the Huffman Tree by assigning a binary code to each letter, using shorter 
# codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
# Trim the Huffman Tree (remove the frequencies from the previously built tree).
# Encode the text into its compressed form.
# Decode the text from its compressed form.

# You then will need to create encoding, decoding, and sizing schemas.

import sys

class Node(object):
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None


def huffman_encoding(data):
    
    if len(data) == 0:
        return None, None
       
    import heapq
        
    # generate an empty dictionary to store the unique characters and corresponding frequencies    
    frequencies = {}
    
    for character in data:
        if character not in frequencies:
            frequencies[character] = 1
        else:
            frequencies[character] += 1

    # convert the dictionary to a list of tuples and sort it according to the frequencies    
    frequencies_list = [(value,key) for key, value in frequencies.items()]
    frequencies_list.sort()

    # then for each character, we extand the 2-element tuple to 3-element tuple    
    # with the third element being a Node
    # we'll use this new list as a heap
    frequencies_heap = []
    
    for item in frequencies_list:
        node = Node(item[1])
        node = (item[0],item[1],node)
        frequencies_heap.append(node)
    
    # from this frequency heap, we run a loop to build the Huffman Tree
    # every time we extract the two units with smallest frequencies
    # generate a new root node and connect it to these two nodes
    # wrap it with a tuple and push back into the heap
    # until the heap has one last element, which is our final root of the whole Huffman Tree        
    if len(frequencies_heap)>1:
        
        while len(frequencies_heap)>1:
            
            smallest1 = heapq.heappop(frequencies_heap)
            smallest2 = heapq.heappop(frequencies_heap)
            root = Node()
            root.left = smallest1[2]
            root.right = smallest2[2]
            merged = (smallest1[0]+smallest2[0], smallest1[1]+smallest2[1],root)
            heapq.heappush(frequencies_heap, merged)

        # remove unnecessary variables
        del smallest1
        del smallest2
        del merged

    # if there's only one character in the frequency list, just put that as root's left child
    else:
        root = Node()
        root.left = frequencies_heap[0][2]

    # remove unnecessary variables
    del character
    del frequencies
    del frequencies_list
    del frequencies_heap
    del item
    del node


    # now we can encode our input data into output according to our tree
    # we call a helper function to recursively get the characters and paths (code) and store them in a dictionary
    coding_dict = get_codes(root)
    
    # translate the input data
    output = ''
    for character in data:
        output += coding_dict[character]
    
    return output, root


# get_codes is a helper function to traverase the tree and get the code
def get_codes(root):
    coding_dict = {}

    def traverse(node, path =''):
        
        if node:
        
            if node.left == None:
                coding_dict[node.value] = path
                return path[:-1]
            else: 
                # traverse left
                path = traverse(node.left, path + '0')   
                
                if node.right:
                    # traverse right
                    path = traverse(node.right, path + '1')
                
                return path[:-1]
            
    traverse(root)  
    return coding_dict


def huffman_decoding(data,tree):
    
    if data == '' or data == None or tree == None or tree.left == None:
        return None
    
    output = ''
    node = tree
    
    for s in data:
        if s == '0':
            node = node.left
        else: 
            node = node.right
            
        if node.left == None:
            output += node.value
            node = tree        
    
    if node != tree:
        output += '<...data impaired...>'
    
    return output



# =============================================================================
# TESTS
# =============================================================================


if __name__ == "__main__":
    codes = {}



# Test 1: a regular sentence

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 69
    
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 36
    
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: 1110000100011011101010100111111001001111101010001000110101101101001111    

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 69
    
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the word
    



# Test 2:  a regular sentence, but got accidentally truncated when calling the decoding program


    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 69
    
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 36
    
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: 1110000100011011101010100111111001001111101010001000110101101101001111    

    # What if the data got impaired during the transmission?
    encoded_data = encoded_data[:-1]
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 90
    
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the wor<...data impaired...>
    




# Test 3: Another string


    a_great_sentence = "Delong Meng"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 60
    
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: Delong Meng

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 32
    
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: 101111111011000100101011001110100 

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 60
    
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: Delong Meng





# Test 4: just two characters


    a_great_sentence = "DM"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 51
    
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: DM

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 28
    
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: 01

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 51
    
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: DM





# Test 5: just one character


    a_great_sentence = "D"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 58
    
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: D

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 24
    
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: 0

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 58
    
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: D





# Test 6: a string containing only one type of character


    a_great_sentence = "DDDDDDDDDD"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 59
    
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: DDDDDDDDDD

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 24
    
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: 0000000000

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 59
    
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: DDDDDDDDDD





# Test 7: an empty string


    a_great_sentence = ''

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 49
    
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: 

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: The content of the encoded data is: None

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 16
    
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: None




