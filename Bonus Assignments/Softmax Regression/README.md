# Assignment: Implementing Mini-Batch Gradient Descent for Training Softmax Regression for IRIS Flower Classification

Problem Description
In this assignment, you will implement the mini-batch gradient descent algorithm to train a simple softmax regression for multi-class classification. The goal is to classify the Iris dataset into its three species (Setosa, Versicolor, and Virginica). The Iris dataset is a well-known dataset in machine learning, containing 150 samples of iris flowers, each described by four features (sepal length, sepal width, petal length, and petal width) and corresponding to one of the three species.

Role of Mini-Batch Gradient Descent in Neural Networks:
Mini-batch gradient descent improves the efficiency of model training by dividing the training dataset into smaller batches. This allows the model to update its weights more frequently than batch gradient descent and more stably than stochastic gradient descent. It leads to faster convergence and reduced computation time, especially for large datasets.


Explanation of Mini-Batch Gradient Descent:

Initialize weights and biases: Start with random values using Xavier initialization.
Forward pass: Compute the output of the neural network for each mini-batch using the softmax activation function.
Compute loss: Calculate the cross-entropy loss between the predicted and actual values.
Backward pass: Compute the gradients of the loss with respect to the weights and biases.
Update parameters: Adjust the weights and biases using the gradients and a learning rate.
Repeat steps 2-5 for a specified number of epochs or until convergence.


Input:

Training data (features and labels) from the Iris dataset.
Neural network parameters: number of epochs, batch size, learning rate.

Output:

Trained weights and biases.
Loss values over epochs to show the training progress.
Confusion matrix and classification report to evaluate the model performance.
