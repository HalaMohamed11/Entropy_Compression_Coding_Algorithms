import math
from collections import Counter

# Reads content of a text file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Calculates probability of each character
def calculate_probabilities(text):
    char_count = Counter(text)
    total_chars = sum(char_count.values())
    return {char: count / total_chars for char, count in char_count.items()}

# Computes entropy based on character probabilities
def compute_entropy(probabilities):
    return -sum(prob * math.log2(prob) for prob in probabilities.values() if prob > 0)



# Returns bits per symbol and encoding efficiency for fixed-length encoding
def fixed_length_encoding_metrics(entropy, num_symbols=33):
    bits_per_symbol = math.ceil(math.log2(num_symbols))
    efficiency = (entropy / bits_per_symbol) * 100
    return bits_per_symbol, efficiency


# Builds a Huffman tree based on character frequencies
def create_huffman_tree(probabilities):
    nodes = [(char, freq) for char, freq in probabilities.items()]
    
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x[1])
        left = nodes.pop(0)
        right = nodes.pop(0)
        combined_freq = left[1] + right[1]
        nodes.append((None, combined_freq, left, right))

    return nodes[0]

# Generates Huffman codes from the tree
def generate_huffman_codes(node):
    codes = {}
    queue = [(node, "")]
    
    while queue:
        current_node, current_code = queue.pop(0)
        
        if len(current_node) == 2:
            codes[current_node[0]] = current_code
        else:
            if current_node[2]:
                queue.append((current_node[2], current_code + "0"))
            if current_node[3]:
                queue.append((current_node[3], current_code + "1"))
    
    return codes

# Encodes text using Huffman codes
def huffman_encode(text, codes):
    return ''.join(codes[char] for char in text)


#_____________________________________________________________________________________________________#

# Main function to perform compression and generate report
def perform_compression(file_path):
    text = read_file(file_path)
    probabilities = calculate_probabilities(text)
    entropy = compute_entropy(probabilities)
    fixed_bits, fixed_efficiency = fixed_length_encoding_metrics(entropy)

    huffman_tree_root = create_huffman_tree(probabilities)
    huffman_codes = generate_huffman_codes(huffman_tree_root)
    huffman_encoded = huffman_encode(text, huffman_codes)

    huffman_efficiency = (entropy / sum(len(huffman_codes[char]) * prob for char, prob in probabilities.items())) * 100

    
    with open('C:/Users/ASUS/Documents/compression_results.txt', 'w') as result_file:
        result_file.write("==== Compression Report ====\n")
        result_file.write(f"Entropy: {entropy:.4f} bits\n")
        result_file.write(f"Fixed Length Encoding - Bits per Symbol: {fixed_bits}, Efficiency: {fixed_efficiency:.2f}%\n")
        result_file.write(f"Huffman Encoding - Efficiency: {huffman_efficiency:.2f}%\n")


        result_file.write("\nSymbol Probabilities:\n")
        for char, prob in probabilities.items():
            result_file.write(f"  '{char}': {prob:.4f}\n")


        result_file.write("\nHuffman Encoding Codes:\n")
        for char, code in huffman_codes.items():
            result_file.write(f"  '{char}': {code}\n")


file_path = 'C:/Users/ASUS/Documents/Test_text_file.txt'
perform_compression(file_path)
