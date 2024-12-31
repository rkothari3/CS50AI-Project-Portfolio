import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """

    # Intialize the two return lists
    images = []
    labels = []

    for i in range(NUM_CATEGORIES):
        # os.path.join() method in Python join one or more path components intelligently.
            # For instance os.path.join('usr', 'local', 'bin') 
            # On windows gives, 'usr\\local\\bin'
            # On Linux/MacOS gives, 'usr/local/bin'
        # Here, os.path.join(data_dir, str(i)) will give the path of the ith category
        path = os.path.join(data_dir, str(i))
        
        # Iterate over all the subdirectories in data_dir.
        # os.listdir() returns a list containing the names of the entries in the directory given by path.
        
        # For each image in the subdirectory, read the image and resize it to IMG_WIDTH x IMG_HEIGHT
        for image in os.listdir(path):
            # Read the image:
            # - Use cv2.imread() to load the image from your file system.
            # - To read an image using OpenCV, use cv2.imread(path, flag).
            # - 'path' can be obtained using os.path methods.
            # - 'flag' specifies the way in which the image should be read. Default is cv2.IMREAD_COLOR.
            img = cv2.imread(os.path.join(data_dir, str(i), image))

            # Resize the image:
            # - Use the cv2.resize() function.
            # - Pass the original image as the first argument.
            # - Pass the new dimensions as a tuple (new_width, new_height) as the second argument.
            # - Optionally, specify an interpolation method as the third argument. Common methods include:
            #   - cv2.INTER_AREA: For shrinking images.
            #   - cv2.INTER_LINEAR: For enlarging images (default).
            #   - cv2.INTER_CUBIC: For higher quality enlarging.
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))

            images.append(img)
            labels.append(i)

    return (images, labels)

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    # Create a convolutional neural network
    # Keras Sequential API: NN pattern with a sequence (one layer after another)
    model = tf.keras.models.Sequential([
        # Convolutional layer. Learn 32 filters using a 3x3 kernel matrix
        #   - Different kernels can achieve different tasks.
        tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),

        # Max-pooling layer, using 2x2 pool size.
        #   - (Max)pooling makes image convolution less expensive
        #   - Max-pooling, selected pixel value has the highest value in a region.
        tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
        
        # Convolution and pooling can be repeated to make very big images simple.
        # Ensuring that it's less expensive, more accurate, and having lower loss

        # Second convolation layer. 32 filters; 3x3 kernel
        #   - Note: second Conv2D doesn't need to specify input_shape
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),

        # Second pooling layer. 2x2 pool size.
        tf.keras.layers.MaxPooling2D(pool_size=(2,2)),

        # Flattening: Pooled images are fed to traditional, feed-forward, neural networks
        tf.keras.layers.Flatten(),

        # Dropping: helps ensure the NN isn't overfitted.
        # Adding it as a hidden layer
        tf.keras.layers.Dense(128, activation="relu"),
        # (0.2) -> Drops 1/5ths (or 2/10ths) of the nodes to avoid overfitting.
        tf.keras.layers.Dropout(0.2),

        # Add an output layer with output units for all 43 signs
        #   - softmax: takes output and turn it into a probability distribution.
        #              Note: Values add up to 1
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])
    
    # Train neural network
    # Using binary crossentropy loss for a multi-class problem.
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model


if __name__ == "__main__":
    main()
