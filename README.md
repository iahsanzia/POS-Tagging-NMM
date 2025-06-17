# Part-of-Speech (POS) Tagging with Hidden Markov Models

A Natural Language Processing project that implements Part-of-Speech tagging using Hidden Markov Models (HMM) with the NLTK library. This project provides functionality to train, evaluate, and test POS taggers with performance analysis.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Data Format](#data-format)
- [Performance Evaluation](#performance-evaluation)
- [Example Output](#example-output)
- [Contributing](#contributing)

## 🔍 Overview

Part-of-Speech tagging is a fundamental task in Natural Language Processing that involves assigning grammatical categories (like noun, verb, adjective, etc.) to words in a sentence. This project implements an HMM-based POS tagger using the NLTK library, providing both training and evaluation capabilities.

The project includes:
- **HMM POS Tagger Training**: Train custom POS taggers using annotated datasets
- **Sentence Tagging**: Tag new sentences with the trained model
- **Performance Evaluation**: Measure accuracy and efficiency of the tagger
- **Efficiency Analysis**: Compare performance metrics including execution time

## ✨ Features

- 🤖 **Hidden Markov Model Implementation**: Uses NLTK's HMM trainer for robust POS tagging
- 📊 **Performance Metrics**: Calculates accuracy scores and execution time
- 🔄 **Custom Data Loading**: Supports custom training and test datasets
- 📈 **Efficiency Analysis**: Detailed performance evaluation with timing metrics
- 🎯 **Real-time Tagging**: Tag individual sentences or batches of text
- 📋 **Multiple Evaluation Methods**: Different approaches for accuracy calculation

## 📁 Project Structure

```
POS-Tagging/
├── NLP.py              # Main POS tagging implementation
├── Efficiency.py       # Performance evaluation and efficiency analysis
├── train1.txt          # Training dataset (Penn Treebank format)
├── testdata1.txt       # Test dataset for evaluation
└── README.md           # Project documentation
```

### File Descriptions

- **`NLP.py`**: Core implementation containing the HMM tagger training, sentence tagging, and evaluation functions
- **`Efficiency.py`**: Performance analysis module that measures accuracy and execution time
- **`train1.txt`**: Training dataset with 10,000 tagged sentences in Penn Treebank format
- **`testdata1.txt`**: Test dataset with 500 tagged sentences for evaluation

## 🛠️ Requirements

- Python 3.6+
- NLTK library
- Required NLTK data packages:
  - `treebank`
  - `hmm`

## 📦 Installation

1. **Clone or download the repository**:
   ```bash
   git clone <repository-url>
   cd POS-Tagging
   ```

2. **Install required packages**:
   ```bash
   pip install nltk
   ```

3. **Download NLTK data** (automatically handled in the code):
   ```python
   import nltk
   nltk.download('treebank')
   nltk.download('hmm')
   ```

## 🚀 Usage

### Basic POS Tagging

```python
from NLP import train_hmm_tagger, tag_sentence

# Train the HMM tagger
tagger = train_hmm_tagger("train1.txt")

# Tag a sentence
sentence = "He said package of cocoa is big."
tagged_sentence = tag_sentence(tagger, sentence)
print("Tagged Sentence:", tagged_sentence)
```

### Performance Evaluation

```python
from NLP import train_hmm_tagger, evaluate_tagger

# Train and evaluate
tagger = train_hmm_tagger("train1.txt")
accuracy = evaluate_tagger(tagger, "testdata1.txt")
print(f"Accuracy: {accuracy}")
```

### Efficiency Analysis

```python
from Efficiency import efficiency_function

# Analyze performance with timing
efficiency_function("train1.txt", "testdata1.txt")
```

### Running the Complete Example

Execute the main script:

```bash
python NLP.py
```

Or run the efficiency analysis:

```bash
python Efficiency.py
```

## 📄 Data Format

The training and test data should be in Penn Treebank format, where each line contains a sentence with words and their POS tags separated by '/':

```
Pierre/NP Vinken/NP ,/, 61/CD years/NNS old/JJ ,/, will/MD join/VB the/DT board/NN ./.
Mr./NP Vinken/NP is/VBZ chairman/NN of/IN Elsevier/NP N.V./NP ./.
```

### Common POS Tags

- **NP**: Proper noun
- **NN**: Noun, singular
- **NNS**: Noun, plural
- **VB**: Verb, base form
- **VBZ**: Verb, 3rd person singular present
- **DT**: Determiner
- **JJ**: Adjective
- **IN**: Preposition or subordinating conjunction
- **CD**: Cardinal number

## 📊 Performance Evaluation

The project provides two evaluation approaches:

### 1. Standard Accuracy (NLP.py)
- Uses NLTK's accuracy function
- Compares true tags with predicted tags
- Returns accuracy as a decimal value

### 2. Efficiency Analysis (Efficiency.py)
- Measures both accuracy and execution time
- Provides percentage accuracy
- Reports processing time in seconds
- Uses manual accuracy calculation for detailed analysis

## 📈 Example Output

```
Tagged Sentence: [('He', 'PP'), ('said', 'VBD'), ('package', 'NN'), ('of', 'IN'), ('cocoa', 'NN'), ('is', 'VBZ'), ('big', 'JJ'), ('.', '.')]

HMM Tagger Accuracy: 0.8524

Accuracy: 85.24%
Time Taken: 0.15 seconds
```

## 🔧 Configuration

To use your own datasets, update the file paths in the main execution blocks:

```python
# In NLP.py
train_data_path = r"path/to/your/train.txt"
test_data_path = r"path/to/your/test.txt"

# In Efficiency.py
train_data_path = r"path/to/your/train.txt"
test_data_path = r"path/to/your/test.txt"
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📚 References

- [NLTK Documentation](https://www.nltk.org/)
- [Penn Treebank POS Tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)
- [Hidden Markov Models for POS Tagging](https://web.stanford.edu/~jurafsky/slp3/8.pdf)

---

**Note**: This project is designed for educational and research purposes in Natural Language Processing and machine learning applications.
