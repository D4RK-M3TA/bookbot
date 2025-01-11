from collections import Counter

def count_words(text):
    """
    Counts the number of words in the given text.
    """
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Counts the frequency of each character in the given text.
    """
    text = text.lower()
    character_counts = Counter(text)
    return character_counts

def generate_report(path_to_file, word_count, character_count):
    """
    Generates a formatted report of the text analysis.
    """
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    
    # Filter only alphabetic characters and sort by frequency in descending order
    sorted_characters = sorted(
        [(char, count) for char, count in character_count.items() if char.isalpha()],
        key=lambda x: x[1],
        reverse=True
    )
    
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def main():
    # Define the path to the file
    path_to_file = "books/frankenstein.txt"
    
    # Open the file and read its contents
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    
    # Count the words in the text
    word_count = count_words(file_contents)
    
    # Count the character frequencies in the text
    character_count = count_characters(file_contents)
    
    # Generate and print the report
    generate_report(path_to_file, word_count, character_count)

if __name__ == "__main__":
    main()
