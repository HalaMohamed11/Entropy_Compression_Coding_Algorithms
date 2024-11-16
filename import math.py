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

#_____________________________________________________________________________________________________#

# Main function to perform compression and generate report
def perform_compression(file_path):
    text = read_file(file_path)
    probabilities = calculate_probabilities(text)
    entropy = compute_entropy(probabilities)
    fixed_bits, fixed_efficiency = fixed_length_encoding_metrics(entropy)
    
    with open('/Users/yousefsaeed/Downloads/compression_results.txt', 'w') as result_file:
        result_file.write("==== Compression Report ====\n")
        result_file.write(f"Entropy: {entropy:.4f} bits\n")
        result_file.write(f"Fixed Length Encoding - Bits per Symbol: {fixed_bits}, Efficiency: {fixed_efficiency:.2f}%\n")


        result_file.write("\nSymbol Probabilities:\n")
        for char, prob in probabilities.items():
            result_file.write(f"  '{char}': {prob:.4f}\n")

file_path = '/Users/yousefsaeed/Downloads/Test_text_file.txt'
perform_compression(file_path)
