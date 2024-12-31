# PageRank

The **PageRank** project implements an AI to rank web pages by their importance using the **PageRank algorithm**, originally developed by Google's co-founders. The algorithm evaluates the significance of web pages based on the structure of links between them, simulating the behavior of a "random surfer" who navigates the web by clicking on links.

This project calculates PageRank using two approaches: **sampling** (based on the random surfer model) and **iteration** (using a recursive mathematical formula).

## Features
- **Random Surfer Model**: Simulates a user randomly navigating through web pages, with a damping factor to account for random jumps.
- **Iterative Algorithm**: Calculates PageRank values recursively until they converge within a small threshold.
- **Customizable Corpus**: Accepts a directory of HTML files as input and parses their link structure to build a graph representation of the web.
- **Two Calculation Methods**:
  - **Sampling**: Estimates PageRank by simulating a random surfer's behavior over multiple samples.
  - **Iteration**: Computes PageRank values mathematically based on link structure and convergence criteria.

## Technologies Used
- **Python 3.12**
- Graph representation of web pages
- Probability distributions for transition models
- Recursive algorithms for iterative calculations

## How It Works
1. The program parses a corpus of web pages to create a dictionary representing links between pages.
2. The AI calculates PageRank using two methods:
   - **Sampling**:
     - Starts with a random page.
     - Simulates transitions between pages based on their links and the damping factor.
     - Tracks visit frequencies to estimate PageRank values.
   - **Iteration**:
     - Initializes all pages with equal rank.
     - Repeatedly updates ranks based on the PageRank formula until values converge.
3. Outputs the PageRank for each page as probabilities that sum to 1.

## Key Functions in `pagerank.py`
- `transition_model(corpus, page, damping_factor)`: Generates a probability distribution for the next page based on the current page's links and damping factor.
- `sample_pagerank(corpus, damping_factor, n)`: Estimates PageRank by sampling transitions over `n` iterations.
- `iterate_pagerank(corpus, damping_factor)`: Computes PageRank iteratively using the recursive formula until values converge.

## Learning Outcomes
This project demonstrates:
- The application of Markov Chains and probability distributions in ranking systems.
- How search engines like Google rank web pages based on link structures.
- The implementation of two distinct approaches (sampling vs iteration) for solving real-world problems.

## Example Usage
```bash
$ python pagerank.py corpus0
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307
