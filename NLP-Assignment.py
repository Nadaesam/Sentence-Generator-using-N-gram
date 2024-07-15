import random
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
import string
 
def preprocess_sentence(sentence):
    # Tokenize sentence into words
    words = word_tokenize(' '.join(sentence))
    # Remove punctuation marks
    punctuation_marks = list(string.punctuation) + ['``'] + ['--']
    words_without_punctuation = [word for word in words if word not in punctuation_marks]
    # Convert to lowercase
    words_lowercase = [word.lower() for word in words_without_punctuation]
    return words_lowercase
 
def build_ngram_model(corpus, n):
    model = {}
    for sentence in corpus:
        for i in range(len(sentence) - n + 1):
            ngram = tuple(sentence[i:i + n - 1])
            next_token = sentence[i + n - 1]
            if ngram in model:
                model[ngram].append(next_token)
            else:
                model[ngram] = [next_token]
    return model
 
def generate_sentence(ngram_model, max_len, n):
    sentence = []
    # Choose a random starting n-1 gram
    ngram = random.choice(list(ngram_model.keys()))
    sentence.extend(list(ngram))
 
    while len(sentence) < max_len:
        # Check if the last n-1 words are in the model
        if ngram in ngram_model:
            # Randomly choose the next word
            next_word = random.choice(ngram_model[ngram])
            sentence.append(next_word)
            # Update the n-1 gram
            ngram = tuple(sentence[-(n-1):])
        else:
            break
 
    return ' '.join(sentence)
 
# Get user input for the number of sentences and max length
m = int(input("Enter the number of sentences to generate: "))
n = int(input("Enter the value of n for the n-gram model: "))
max_len = int(input("Enter the maximum length of each sentence: "))
 
# Get sentences from Brown Corpus
corpus = brown.sents()
# Preprocess corpus
preprocessed_corpus = []
for sentence in corpus:
    preprocessed_sentence = preprocess_sentence(sentence)
    preprocessed_corpus.append(preprocessed_sentence)
# Build n-gram model
ngram_model = build_ngram_model(preprocessed_corpus, n)
 
# Generate sentences
generated_sentences = []
for _ in range(m):
    sentence = generate_sentence(ngram_model, max_len, n)
    generated_sentences.append(sentence)
 
# Print generated sentences
for i, sentence in enumerate(generated_sentences, 1):
    print(f"Sentence {i}: {sentence}")