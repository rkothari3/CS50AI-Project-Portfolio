# Traffic Sign Recognition AI

The **Traffic Sign Recognition AI** project develops a convolutional neural network (CNN) to classify images of traffic signs using the **German Traffic Sign Recognition Benchmark (GTSRB)** dataset. This project demonstrates the application of deep learning in computer vision, specifically for tasks like autonomous driving, where recognizing road signs is critical.

## Features
- **Neural Network Implementation**:
  - Builds a CNN using **TensorFlow** and **Keras**.
  - Includes convolutional, pooling, and dense layers for feature extraction and classification.
- **Dataset Handling**:
  - Processes the GTSRB dataset containing images of 43 types of traffic signs.
  - Resizes all images to a uniform size for input into the neural network.
- **Training and Evaluation**:
  - Splits data into training and testing sets.
  - Trains the model over multiple epochs and evaluates its accuracy on unseen data.
- **Model Saving**:
  - Allows saving the trained model for future use.

## Technologies Used
- **Python 3.12**
- **TensorFlow/Keras** for building and training the neural network
- **OpenCV (cv2)** for image processing
- **Scikit-learn** for data splitting and evaluation

## How It Works
1. **Data Preparation**:
   - Reads images from subdirectories corresponding to each category (0–42).
   - Resizes images to a fixed size (e.g., \(30 \times 30\) pixels) and converts them into NumPy arrays.
   - Labels each image based on its directory name.
2. **Model Architecture**:
   - Input layer accepts images of shape \((IMG\_WIDTH, IMG\_HEIGHT, 3)\).
   - Convolutional layers extract spatial features from the images.
   - Pooling layers reduce dimensionality while retaining important features.
   - Fully connected layers classify the features into one of 43 categories.
3. **Training**:
   - The model is trained using a labeled dataset with a loss function like categorical cross-entropy and an optimizer like Adam.
4. **Evaluation**:
   - The trained model is evaluated on a test set to measure accuracy.

## Key Functions in `traffic.py`
### `load_data(data_dir)`
- Loads and preprocesses all images from the dataset.
- Resizes images to \(30 \times 30 \) pixels using OpenCV and returns them as NumPy arrays along with their labels.

### `get_model()`
- Builds and compiles a CNN with:
  - Convolutional layers for feature extraction.
  - Pooling layers for dimensionality reduction.
  - Dense layers for classification.

### `main()`
- Loads data, splits it into training/testing sets, trains the model, evaluates performance, and optionally saves the trained model.

## Learning Outcomes
This project demonstrates:
- The use of convolutional neural networks (CNNs) for image classification tasks.
- How to preprocess large datasets for machine learning models.
- The importance of hyperparameter tuning (e.g., number of layers, filters, epochs) in improving model performance.

## Example Usage:
**Note:** Due to the large file of the database, please download it here: https://benchmark.ini.rub.de/
```bash
$ python traffic.py gtsrb
Epoch 1/10
500/500 [==============================] - 5s 9ms/step - loss: 3.7139 - accuracy: 0.1545
Epoch 2/10
500/500 [==============================] - 6s 11ms/step - loss: 2.0086 - accuracy: 0.4082
Epoch 3/10
500/500 [==============================] - 6s 12ms/step - loss: 1.3055 - accuracy: 0.5917
Epoch 4/10
500/500 [==============================] - 5s 11ms/step - loss: 0.9181 - accuracy: 0.7171
Epoch 5/10
500/500 [==============================] - 7s 13ms/step - loss: 0.6560 - accuracy: 0.7974
Epoch 6/10
500/500 [==============================] - 9s 18ms/step - loss: 0.5078 - accuracy: 0.8470
Epoch 7/10
500/500 [==============================] - 9s 18ms/step - loss: 0.4216 - accuracy: 0.8754
Epoch 8/10
500/500 [==============================] - 10s 20ms/step - loss: 0.3526 - accuracy: 0.8946
Epoch 9/10
500/500 [==============================] - 10s 21ms/step - loss: 0.3016 - accuracy: 0.9086
Epoch 10/10
500/500 [==============================] - 10s 20ms/step - loss: 0.2497 - accuracy: 0.9256
333/333 - 5s - loss: 0.1616 - accuracy: 0.9535
