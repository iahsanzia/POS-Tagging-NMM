import time
import nltk
from nltk.tag import hmm
from nltk.tag.util import untag

# Function to load data from a directory
def load_data(data_path):
    with open(data_path, "r", encoding="utf-8") as file:
        data = file.read().splitlines()
    return [nltk.pos_tag(nltk.word_tokenize(sentence)) for sentence in data]

# Function to train the HMM tagger
def train_hmm_tagger(train_data):
    trainer = hmm.HiddenMarkovModelTrainer()
    tagger = trainer.train(train_data)
    return tagger

# Function to evaluate the tagger
def evaluate_tagger(tagger, test_data):
    start_time = time.time()
    tagged_sents = [tagger.tag(untag(sent)) for sent in test_data]
    end_time = time.time()
    
    # Flatten lists for accuracy calculation
    test_tags = [tag for sent in test_data for word, tag in sent]
    pred_tags = [tag for sent in tagged_sents for word, tag in sent]
    
    correct = sum(1 for test, pred in zip(test_tags, pred_tags) if test == pred)
    accuracy = correct / len(test_tags)
    
    time_taken = end_time - start_time
    return accuracy, time_taken

# Function to calculate the efficiency
def efficiency_function(train_data_path, test_data_path):
    train_data = load_data(train_data_path)
    test_data = load_data(test_data_path)
    
    # Train the HMM tagger
    tagger = train_hmm_tagger(train_data)
    
    # Evaluate the tagger
    accuracy, time_taken = evaluate_tagger(tagger, test_data)
    
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"Time Taken: {time_taken:.2f} seconds")

# Example usage
if __name__ == "__main__":
    train_data_path = r"C:\Users\Ahsan\Desktop\train.txt"
    test_data_path = r"C:\Users\Ahsan\Desktop\testdata.txt"
    efficiency_function(train_data_path, test_data_path)
