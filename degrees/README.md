# Degrees of Separation

The **Degrees of Separation** project is inspired by the "Six Degrees of Kevin Bacon" game, which posits that any actor in the Hollywood film industry can be connected to Kevin Bacon through six or fewer shared movie roles. This program generalizes the concept, allowing users to determine the shortest path (in terms of shared movies) between any two actors in a dataset. By leveraging **graph search algorithms**, the program identifies the sequence of movies and actors that connect the two individuals.

## Features
- **Shortest Path Calculation**: Uses **Breadth-First Search (BFS) and Depth-First Search** to find the shortest connection between two actors.
- **Dynamic Input**: Users can input any two actor names, and the program will compute their degrees of separation.
- **Dataset Flexibility**: Supports both small and large datasets of actors and movies for testing and performance evaluation.
- **Error Handling**: Handles cases where no path exists between two actors or when multiple actors share the same name.

## How It Works
1. The program loads data from CSV files containing information about actors, movies, and their relationships.
2. Users input two actor names.
3. The program computes the shortest path between them by searching through shared movie connections.
4. The result is displayed as a sequence of movies and co-stars connecting the two actors.

## Key Files
- `degrees.py`: The main program file that implements the search logic.
- `util.py`: Contains helper classes for graph traversal, such as `Node`, `StackFrontier`, and `QueueFrontier`.
- `people.csv`, `movies.csv`, `stars.csv`: Datasets containing actor and movie information.

## Learning Outcomes
This project demonstrates how graph structures can model real-world relationships, such as connections in a social network or film industry. It also highlights the practical application of search algorithms like BFS to solve problems efficiently.

## Example Usage
```bash
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
