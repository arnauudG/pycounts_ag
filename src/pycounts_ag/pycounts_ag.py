from string import punctuation
from collections import Counter

def load_file(input_file: str)-> str:
    """Load text from a text file and return as a string."""
    with open(input_file, 'r') as file:
        text = file.read()
    return text
def clean_text(text: str) -> str:
    """Lowercase and remove punctuation from the string"""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text

def count_words(input_file: str) -> str:
    """Count unique words in a string."""
    text = load_file(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)