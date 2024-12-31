# Heredity AI

The **Heredity AI** project models genetic inheritance and traits using a **Bayesian Network**. This program calculates the likelihood of individuals in a family having a specific genetic trait (e.g., hearing impairment caused by the GJB2 gene) based on probabilistic relationships between genes, traits, and inheritance rules. By leveraging probabilities and evidence, the AI infers the distribution of genes and traits for each person in a dataset.

## Features
- **Bayesian Network Representation**: Models genetic inheritance and trait expression based on probabilistic dependencies:
  - Each person inherits one gene from each parent, with probabilities affected by mutations.
  - Traits are determined based on the number of mutated genes.
- **Joint Probability Calculation**: Computes the likelihood of a specific combination of gene counts and traits across an entire family.
- **Evidence-Based Inference**: Updates probability distributions based on observed evidence (e.g., known traits).
- **Normalization**: Ensures all probability distributions sum to 1.

## Technologies Used
- **Python 3.12**
- Bayesian networks for probabilistic reasoning
- Recursive algorithms for joint probability computation

## How It Works
1. The program reads family data from a CSV file, including parent-child relationships and observed traits.
2. It calculates probabilities for:
   - The number of mutated genes each person has (0, 1, or 2).
   - Whether each person exhibits the trait based on their genes.
3. Three key functions power the AI:
   - `joint_probability`: Computes the joint probability of all events (genes and traits) in the family.
   - `update`: Updates probability distributions with new joint probabilities.
   - `normalize`: Adjusts distributions so probabilities sum to 1.

## Key Functions in `heredity.py`
### `joint_probability`
- Computes the combined likelihood of all people having specific gene counts and traits based on inheritance rules, mutation probabilities, and observed evidence.

### `update`
- Adds computed joint probabilities to existing distributions for each person’s gene count and trait status.

### `normalize`
- Ensures all probability distributions sum to one while maintaining relative proportions.

## Learning Outcomes
This project demonstrates:
- How **Bayesian Networks** model real-world probabilistic relationships.
- The use of conditional probabilities in genetic inheritance modeling.
- Techniques for normalizing distributions to ensure valid probabilistic outputs.

## Example Usage
```bash
$ python heredity.py data/family0.csv
Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335
James:
  Gene:
    2: 0.1976
    1: 0.5106
    0: 0.2918
  Trait:
    True: 1.0000
    False: 0.0000
Lily:
  Gene:
    2: 0.0036
    1: 0.0136
    0: 0.9827
  Trait:
    True: 0.0000
    False: 1.0000
