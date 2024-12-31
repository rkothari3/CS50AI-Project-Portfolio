import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages

def transition_model(corpus, page, damping_factor):
    """
    Return a dictionary representing the probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Intialize
    transDict = {}
    for page_name in corpus:
        transDict[page_name] = 0

    # If a page has no links, we can pretend it has links to all pages in the corpus, including itself.
    if page in transDict and len(corpus[page]) == 0:
        for pageName in transDict:
            transDict[pageName] = 1 / len(corpus)
        return transDict
    
    # Prob of picking any page from the corpus at random
    random_prob = (1 - damping_factor) / len(corpus)
    
    # Prob of picking any linked page from the given page
    link_prob = (damping_factor) / len(corpus[page])
    
    # Add probabilites to the distribution
    for pageName in transDict:
        transDict[pageName] += random_prob

        if pageName in corpus[page]:
            transDict[pageName] += link_prob

    # Round to 4 decimal places
    for pageName in transDict:
        transDict[pageName] = round(transDict[pageName], 4)
    return transDict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Intialize a dictionary
    srankDict = {}
    for pName in corpus:
        srankDict[pName] = 0

    # First randomized sample
    ## Randomly choose a page using the list of pages dervided from keys of corpus
    currPage = random.choice(list(corpus.keys())) 
    srankDict[currPage] += 1

    # For remaining n-1 samples, pick the page based on the transistion model:
    for i in range(n-1):
        currDist = transition_model(corpus, currPage, damping_factor)
        # Get the transition model for the current page
        probabilities = transition_model(corpus, currPage, damping_factor)
        
        # Choose the next page based on the probabilities
        nextPage = random.choices(
            population=list(probabilities.keys()),   # List of pages
            weights=list(probabilities.values()),    # Corresponding probabilities
            k=1                                      # Choose 1 page
        )[0]  # random.choices returns a list, so take the first element
            # Update the count for the chosen page
        srankDict[nextPage] += 1
        # Update the current page to the newly chosen page
        currPage = nextPage
    
    # Normalize the visit counts to calculate the PageRank
    for page_name in srankDict:
        srankDict[page_name] /= n
    
    return srankDict

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    irankDict = {}
    threshold = 0.001 # Convergence threshold for PageRank values
    N = len(corpus)
    converged = False

    # Intialize dict values to 0
    for pName in corpus:
        irankDict[pName] = 0
    # print(irankDict)

    # Intial page rank of 1/N
    for pName in irankDict:
        irankDict[pName] = 1/N
    # print(irankDict)

    while not converged:
        # Temporary dictionary to store updated PageRank values
        new_irankDict = {}
        
        for page in corpus:
            # Base rank (teleportation probability)
            base_rank = (1 - damping_factor) / N
            
            # Summation term: contributions from all pages linking to `page`
            link_sum = 0
            for other_page in corpus:
                if page in corpus[other_page]:
                    link_sum += irankDict[other_page] / len(corpus[other_page])
                elif len(corpus[other_page]) == 0:
                    # Handle "dangling links" (pages with no outgoing links)
                    link_sum += irankDict[other_page] / N
            
            # Update the PageRank for the current page
            new_irankDict[page] = base_rank + damping_factor * link_sum

        # Check for convergence: Compare old and new ranks
        converged = all(
            abs(new_irankDict[page] - irankDict[page]) < threshold
            for page in irankDict
        )
        
        # Update PageRank values for the next iteration
        irankDict = new_irankDict

    # Normalize the PageRank values to ensure they sum to 1
    total_rank = sum(irankDict.values())
    for page in irankDict:
        irankDict[page] /= total_rank

    # Round to 4 pages
    for pageName in irankDict:
        irankDict[pageName] = round(irankDict[pageName], 4)

    return irankDict

# Test Case
# corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
# page = "1.html"
# damping_factor = DAMPING
# n = SAMPLES
# print(transition_model(corpus, page, damping_factor))
# print(sample_pagerank(corpus, damping_factor, n))
# var = iterate_pagerank(corpus, damping_factor)
# print(var)
    
   

if __name__ == "__main__":
    main()
    

