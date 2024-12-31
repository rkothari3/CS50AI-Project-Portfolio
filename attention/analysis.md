# Analysis

## Layer 2, Head 5
![The cat jumped over the [MASK].](image-3.png)
![he placed the glass on the [MASK].](image.png)

Explaination:
This attention indicates both that the model is taking into consideration the words itself alongside providing good information on their context. Particulalry, the models in both sentences indicate its ability to comprehend prepostion of place, which are used to indicate the position of something relative to another thing. 

Example Sentences:
- The cat jumped over the [MASK].
- She placed the glass on the [MASK].

## Layer 3, Head 1
![The cat jumped over the [MASK].](image-2.png)
![She placed the glass on the [MASK].](image-1.png)

Explaination:
The diagonal pattern in the attention matrix indicates that the model is paying attention to the word in the sentence rather than the context.Despite this, context is still taken into account. There is a visible connection in both sentences between the token "the" (before "[MASK]") and other instances of "the". This suggests that the model recognizes shared contextual or syntactic roles of these tokens. 

Example Sentences:
- The cat jumped over the [MASK].
- She placed the glass on the [MASK].

