#importing spacy for natural language processing to remove stop words from the text
#importing couner to count the occurrences of elements in a collection (list)
import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

# Function to remove stop words from the text
def remove_stop_words(text):
    doc = nlp(text)
    filtered_words = [token.text.lower() for token in doc if not token.is_stop and token.is_alpha]
    return filtered_words

# Function to count the frequency of each single word
def count_word_frequency(words):
    word_counts = Counter(words)
    return word_counts

# Function to display each word's frequency 
def print_word_frequency(word_counts):
    for word, count in word_counts.items():
        print(f"{word} : {count}")


#open the file that contains the text
with open(r"random_paragraphs.txt", "r") as file:
    text = file.read()
    

#The following lines use the previous functions to remove stop words from the text in the file and then displaying the frequency of the rest of the words 
chunk_size = 100000
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

filtered_words = []

for chunk in chunks:
    filtered_words.extend(remove_stop_words(chunk))

word_counts = count_word_frequency(filtered_words)

print_word_frequency(word_counts)


