# Huffman Coding


Problem:

The Huffman algorithm works by assigning codes that correspond to the relative 
frequency of each character for each character. The Huffman code can be of any 
length and does not require a prefix; therefore, this binary code can be visualized 
on a binary tree with each encoded character being stored on leafs.



My Code Analysis:


Huffman coding is a lossless compressing technique. Instead of taking up the same amount of space, now we assign different length of code for each character according to their frequencies in a string. Characters with higher frequencies will get shorter code, thus saving more space. 

To implement the idea of Huffman tree, I take advantege of the heap structure. A min-heap is formed based on the frequencies of characters, and every time I can easily pop out two elements with lowest frequencies, combine them (add up their frequencies) and push back into the heap.

To build a tree, I simply use a Node class, where each node can have a value (not necessary for nodes other than the leaf nodes), a left child and a right child. In order to use the heap idea to build this binary Huffman tree, the element in the heap has to contain the frequency information, and the node. To do that, each unit in the heap is a tuple with 3 elements: [0]: frequency, so the heap can be maintained according to this information; [1]: the character name, because we may have tie (two different characters with the same frequency number), but they have different name so the heap can still be maintained in this case; [2]: a Node. Every time I pop out the two smallest units from the heap, I generate a new tuple, with the frequencies added up, the character names concatenated, and most importantly, the third element will be a newly generated node as the parent of the two nodes. Then I push this new tuple unit back to the heap.

Overall steps and complexity analysis:

A) Encoding:

A1) use a {character: frequency} dictionary to record all characters and frequencies
A2) convert the dictionary to a list of (frequency, character) tuples and sort it (so later we don't need to initialize the heap).
A3) generate a Node for each character, and wrap into a (frequency, character, Node) tuple.
A4) build the Huffman tree: treat the above list as a min-heap, use heapq functionalities to repeatedly take two smallest units out and link these two nodes, then push back to the heap.
A5) traverse the Huffman tree to record all paths (namely codes) and corresponding leaf nodes (characters), and put into a dictionary of {character: code}
A6) loop through the input string, and generate the output according to the coding dictionary

Time complexity: A1, O(n); A2, O(nlogn) (because of sorting); A3, O(n); A4, the loop is aroung n times, and each time the pop/push is log(n), so the total of tree building step is O(nlog(n)); A5, O(n); A6, O(n); overall: O(nlogn).

Space complexity: A1, O(n); A2, O(n); A3, O(n); A4, O(n); A5, O(n); A6, O(n); overall: O(n).

B) Decoding

B1) loop through the input (a '0'/'1' binary string) and travel through the tree accordingly until hit the leaf node, and accordingly collect the character on all leaf nodes. 

Time and Space complexity are both O(n), where n is the length of the input '0'/'1' string.


