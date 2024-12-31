from nltk import *
download('punkt_tab')
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

# Complete the Nonterminals
NONTERMINALS = """
S -> NP VP
NP -> Det N | Det Adj N | Det Adj Adj N | N | NP PP
VP -> V | V NP | V NP PP | V PP | VP Conj VP
PP -> P NP | P NP PP
"""

grammar = CFG.fromstring(NONTERMINALS + TERMINALS)
parser = ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    wordList = []

    # word_tokenize(sentence) is used to tokenize the sentence into words
    # Example:
    # Input: "The little red hand arrived at my home."
    # Output: ['The', 'little', 'red', 'hand', 'arrived', 'at', 'my', 'home', '.']

    for word in word_tokenize(sentence):
        if word.isalpha():
            wordList.append(word.lower())
    
    return wordList

def np_chunk(tree): # Input is a nltk.tree object
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    np_chunks = [] 

    # contains_nested_np is used to check if the noun phrase contains any nested noun phrases.
    # If a noun phrase contains any nested noun phrases, it is not added to the list of noun phrase chunks.
    # This is done to avoid adding nested noun phrases to the list of noun phrase chunks.


    for subtree in tree.subtrees():  # Iterate over all subtrees
        if subtree.label() == "NP":  # Check if the subtree is a noun phrase
            contains_nested_np = False  # Flag to check for nested noun phrases

            for child in subtree.subtrees():  # Iterate over subtrees of the current subtree
                if child != subtree and child.label() == "NP":  # Check for nested noun phrases
                    contains_nested_np = True  # Set flag if nested noun phrase is found
                    break  # Exit loop if nested noun phrase is found

            if not contains_nested_np:  # If no nested noun phrases
                np_chunks.append(subtree)  # Add the noun phrase chunk to the list
                
    return np_chunks  # Return the list of noun phrase chunks
    


if __name__ == "__main__":
    main()


# Test Sentences
# 1. The little red hand arrived at my home.
# 2. He smiled until she arrived.
# 3. Holmes chuckled and sat down.
# 4. I had never lit the pipe before.
# 5. We were here until Thursday.

