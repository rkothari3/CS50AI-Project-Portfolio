# Shopping AI

The **Shopping AI** project builds a machine learning model to predict whether an online shopping customer will complete a purchase based on their browsing behavior and session data. By analyzing features such as the number of pages visited, time spent on pages, and user-specific attributes, the AI classifies user intent with measurable accuracy, sensitivity, and specificity.

## Features
- **Data Preprocessing**:
  - Converts raw session data from a CSV file into numerical evidence and labels for machine learning.
  - Encodes categorical variables like `Month`, `VisitorType`, and `Weekend` into numerical formats.
- **k-Nearest Neighbors (k-NN) Classifier**:
  - Implements a **k-NN classifier** (with \( k = 1 \)) using **scikit-learn** to predict purchase intent.
- **Performance Metrics**:
  - Evaluates the model using:
    - **Sensitivity (True Positive Rate)**: Proportion of actual purchases correctly identified.
    - **Specificity (True Negative Rate)**: Proportion of non-purchases correctly identified.

## Technologies Used
- **Python 3.12**
- **scikit-learn** for machine learning
- Data preprocessing with Python’s standard libraries

## How It Works
1. **Data Loading**:
   - Reads session data from a CSV file containing features like page visits, durations, bounce rates, exit rates, and special day proximity.
   - Encodes categorical features (`Month`, `VisitorType`, `Weekend`) into numerical values.
   - Splits data into evidence (features) and labels (purchase intent).
2. **Model Training**:
   - Trains a **k-Nearest Neighbors (k-NN)** classifier on the training dataset.
3. **Prediction and Evaluation**:
   - Uses the trained model to predict purchase intent on the test dataset.
   - Calculates sensitivity and specificity to evaluate performance.
   
## Learning Outcomes
This project demonstrates:
- How to preprocess real-world data for use in machine learning models.
- The implementation of a **k-NN classifier** for binary classification tasks.
- The importance of sensitivity and specificity in evaluating models for imbalanced datasets.

## Example Usage
```bash
$ python shopping.py shopping.csv
Correct: 4088
Incorrect: 844
True Positive Rate: 41.02%
True Negative Rate: 90.55%
