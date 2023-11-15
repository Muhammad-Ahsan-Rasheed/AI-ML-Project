# **Project Title: Handwritten Digits Classifier with PyTorch**

**Project Summary:**
As a machine learning engineer, you'll showcase your deep learning skills by developing a prototype system for optical character recognition (OCR) on handwritten digits. This proof of concept will be demonstrated using the MNIST database, a classic dataset for digit recognition. Your goal is to preprocess the data, build a neural network using PyTorch, and train and tune the model to achieve accurate predictions.

**Project Overview:**
1. **Data Loading and Preprocessing:**
   - Load the MNIST dataset from torchvision.datasets.
   - Utilize transforms or other PyTorch methods to convert data to tensors, normalize, and flatten the data.
   - Create a DataLoader for efficient handling of the dataset.

2. **Dataset Visualization:**
   - Visualize the dataset using the provided function.
   - Explore the transformed training data loader, inverting any normalization and flattening.
   - Examine a second DataLoader without normalization or flattening to understand the natural and transformed shapes of the data.
   - Provide a brief justification for any preprocessing steps undertaken or explain why no preprocessing is needed.

3. **Neural Network Construction:**
   - Use PyTorch to construct a neural network capable of predicting the class of each input image.
   - Implement an optimizer to update the network's weights.
   - Train the neural network using the training DataLoader.

4. **Model Evaluation:**
   - Assess the accuracy of your neural network on the test set.
   - Fine-tune model hyperparameters and network architecture to enhance test set accuracy.
   - Aim to achieve a minimum accuracy of 90% on the test set.

5. **Model Saving:**
   - Employ `torch.save` to save your trained model.

**Submission Instructions:**
Save your trained model in the workspace or upload a single file for review.

**Instructions Summary:**
1. **Step 1 - Data Loading and Preprocessing:**
   - Load MNIST dataset.
   - Transform data to tensors, normalize, and flatten.
   - Create a DataLoader.

2. **Step 2 - Dataset Visualization:**
   - Visualize the dataset.
   - Explore transformed and untransformed DataLoader outputs.
   - Justify preprocessing steps.

3. **Step 3 - Neural Network Construction:**
   - Build a PyTorch neural network.
   - Create an optimizer.
   - Train the neural network.

4. **Step 4 - Model Evaluation:**
   - Evaluate accuracy on the test set.
   - Tune hyperparameters and architecture for improved accuracy.

5. **Step 5 - Model Saving:**
   - Use `torch.save` to save the trained model.

Embark on this hands-on project to demonstrate your proficiency in deep learning and contribute to the development of an optical character recognition system. 