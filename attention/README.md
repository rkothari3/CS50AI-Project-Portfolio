# Masked Language Model AI

The **Masked Language Model AI** project implements a tool that uses **BERT (Bidirectional Encoder Representations from Transformers)**, a transformer-based language model developed by Google, to predict masked words in a text sequence. The program also generates attention diagrams to visualize how BERT's attention heads process language, providing insights into the model's understanding of natural language.

## Features
- **Masked Word Prediction**:
  - Predicts the most likely replacements for a masked word (`[MASK]`) in a given sentence.
  - Uses **Hugging Face's Transformers library** to tokenize input text and process it with BERT.
- **Attention Visualization**:
  - Generates attention diagrams for each of BERT's 144 attention heads (12 layers, each with 12 heads).
  - Visualizes the attention scores between tokens, helping analyze how BERT interprets relationships between words.
- **Interactive Analysis**:
  - Allows users to input custom sentences and explore how BERT predicts masked words and processes language.

## Technologies Used
- **Python 3.12**
- Hugging Face's **Transformers library** for BERT
- TensorFlow for running the BERT model

## How It Works
1. **Input Processing**:
   - The user provides a sentence containing the `[MASK]` token (e.g., "We walked through a small [MASK].").
   - The sentence is tokenized using Hugging Face's `AutoTokenizer`, which splits the text into tokens and identifies the position of the `[MASK]` token.
2. **Masked Word Prediction**:
   - The tokenized input is passed to `TFBertForMaskedLM`, which predicts the top \( k \) most likely replacements for the masked word based on surrounding context.
   - The program outputs the original sentence with each predicted word replacing `[MASK]`.
3. **Attention Visualization**:
   - The program generates attention diagrams for all 144 attention heads.
   - Each diagram shows how strongly each token attends to every other token in the sentence, with lighter colors representing higher attention scores.
  
## Key Functions in `mask.py`
### `get_mask_token_index(inputs, mask_token_id)`
- Identifies the index of the `[MASK]` token in the input sequence of tokens.
- Returns `None` if no `[MASK]` token is found.

### `get_color_for_attention_score(score)`
- Converts an attention score (between 0 and 1) into an RGB color value.
- Maps lower scores to darker shades of gray and higher scores to lighter shades.

### `visualize_attentions(tokens, attentions)`
- Generates attention diagrams for all layers and heads.

## Learning Outcomes
This project demonstrates:
- How **masked language models** like BERT predict missing words based on context.
- The use of **transformer architectures** with multi-head self-attention mechanisms for natural language understanding.
- Techniques for visualizing and interpreting attention scores to understand what aspects of language BERT focuses on.
