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


# Main function to perform compression and generate report
def perform_compression(file_path):
    text = read_file(file_path)
    probabilities = calculate_probabilities(text)
    
    with open('D:/Projects/-Entropy_Compression_Coding_Algorithms/Entropy_Compression_Coding_Algorithms/compression_results.txt', 'w') as result_file:
        result_file.write("==== Compression Report ====\n")
      
        result_file.write("\nSymbol Probabilities:\n")
        for char, prob in probabilities.items():
            result_file.write(f"  '{char}': {prob:.4f}\n")

file_path = 'D:/Projects/-Entropy_Compression_Coding_Algorithms/Entropy_Compression_Coding_Algorithms/Test_text_file.txt'
perform_compression(file_path)
