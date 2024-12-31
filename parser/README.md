# Sentence Parser AI

The **Sentence Parser AI** project is a natural language processing tool that parses sentences and extracts **noun phrase chunks** using **context-free grammars (CFGs)**. By analyzing the syntactic structure of sentences, the AI identifies meaningful noun phrases, enabling deeper understanding and information extraction from text.

## Features
- **Context-Free Grammar Parsing**:
  - Defines a set of CFG rules to parse English sentences.
  - Supports complex sentence structures, including nested noun phrases, prepositional phrases, and conjunctions.
- **Noun Phrase Chunking**:
  - Identifies and extracts noun phrase chunks, defined as the smallest subtrees labeled `NP` that do not contain other `NP` subtrees.
- **Preprocessing**:
  - Converts input sentences into lowercase and tokenizes them into words.
  - Filters out non-alphabetic tokens (e.g., punctuation or numbers).

## Technologies Used
- **Python 3.12**
- **NLTK (Natural Language Toolkit)** for parsing and tree manipulation
- Context-free grammars for syntactic analysis

## How It Works
1. **Preprocessing**:
   - The input sentence is preprocessed to ensure uniformity:
     - Converted to lowercase.
     - Tokenized into words using `nltk.word_tokenize`.
     - Non-alphabetic tokens are removed.
2. **Parsing**:
   - The preprocessed sentence is parsed using a context-free grammar defined in the `NONTERMINALS` and `TERMINALS` variables.
   - The grammar includes rules for constructing sentences (`S`), noun phrases (`NP`), verb phrases (`VP`), and more.
3. **Noun Phrase Chunking**:
   - The program traverses the parse tree to extract noun phrase chunks.
   - A noun phrase chunk is a subtree labeled `NP` that does not contain other `NP` subtrees.

## Key Functions in `parser.py`
### `preprocess(sentence)`
- Preprocesses the input sentence by:
  - Lowercasing all words.
  - Tokenizing the sentence using `nltk.word_tokenize`.
  - Filtering out tokens without alphabetic characters.

### `np_chunk(tree)`
- Extracts all noun phrase chunks from a given parse tree.
- Returns a list of `nltk.tree.Tree` objects labeled as `NP` that do not contain other `NP` subtrees.

### Context-Free Grammar Rules (`NONTERMINALS`)
- Defines rules for constructing sentences.

## Learning Outcomes
This project demonstrates:
- How to use **context-free grammars (CFGs)** for syntactic parsing of natural language.
- Techniques for extracting specific linguistic structures (e.g., noun phrases) from parse trees.
- Practical applications of NLP in information extraction and syntactic analysis.

## Example Usage
```bash
$ python parser.py
Sentence: The little red hand arrived at my home.
                S
       _________|________________
      |                          VP
      |                 _________|___
      |                |             PP
      |                |      _______|___        
      NP               |     |           NP     
  ____|_________       |     |        ___|___    
Det  Adj   Adj  N      V     P      Det      N  
 |    |     |   |      |     |       |       |   
the little red hand arrived  at      my     home

Noun Phrase Chunks
the little red hand
my home
