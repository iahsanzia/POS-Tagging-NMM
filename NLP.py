import os
import nltk
from nltk.tag import hmm
from nltk.metrics import accuracy

# Ensure NLTK data is downloaded
nltk.download('treebank')
nltk.download('hmm')

# Function to load training data
def load_data(data_path):
    data = []
    with open(data_path, "r", encoding="utf-8") as file:
        sentences = file.readlines()
        for sentence in sentences:
            tagged_sentence = [tuple(word_tag.rsplit('/', 1)) for word_tag in sentence.strip().split()]
            data.append(tagged_sentence)
    return data

# Function to train the HMM POS tagger
def train_hmm_tagger(data_dir):
    train_data = load_data(data_dir)
    trainer = hmm.HiddenMarkovModelTrainer()
    tagger = trainer.train(train_data)
    return tagger

# Function to tag a sentence using the trained HMM tagger
def tag_sentence(tagger, sentence):
    tokens = sentence.split()
    tagged_sentence = tagger.tag(tokens)
    return tagged_sentence

# Function to evaluate the HMM tagger
def evaluate_tagger(tagger, test_data):
    test_data = load_data(test_data)
    true_tags = []
    pred_tags = []
    for sentence in test_data:
        words, tags = zip(*sentence)
        pred_tags.extend([tag for word, tag in tagger.tag(words)])
        true_tags.extend(tags)
    accuracy_score = accuracy(true_tags, pred_tags)
    return accuracy_score

# Example usage
if __name__ == "__main__":
    # Paths to the training and test data directories
    train_data_path = r"C:\Users\Ahsan\Desktop\train1.txt"
    test_data_path = r"C:\Users\Ahsan\Desktop\testdata1.txt"

    
    # Train the HMM tagger
    tagger = train_hmm_tagger(train_data_path)
    
    # Example sentence to tag
    sentence = "He said package of cocoa is big."
    tagged_sentence = tag_sentence(tagger, sentence)
    print("Tagged Sentence:", tagged_sentence)
    
    # Evaluate the HMM tagger
    accuracy_score = evaluate_tagger(tagger, test_data_path)
    print("HMM Tagger Accuracy:", accuracy_score)
