# Casting_defect_detection_using_CNN
# Introduction
Casting is a manufacturing technique in which a liquid material is typically poured into a mold with a hollow cavity shaped to the desired form and allowed to solidify. A casting defect refers to an unwanted irregularity that occurs during the metal casting process.
# Dataset Structure
The dataset contains a total of 7348 image data with two classes Defective and Ok. These all are the size of 300*300 pixels grey-scaled images. It is collected from the Kaggle website.
# Train Folder
- def_front: 3758 images
- ok_front: 2875 images
# Test Folder
- def_front: 453 images
- ok_front: 262 images
# Libraries Used
The model leverages various Python libraries for image manipulation, model construction, and evaluation. These include TensorFlow, keras, matplotlib, and scikit-learn, among others.
# Data Loading
The paths to the training and test image directories are defined. The training images are split into training and validation sets in an 80:20 ratio, and the test images are processed separately. Data augmentation is applied to the training set to improve model generalization.
# Data Preprocessing
An ImageDataGenerator is used to apply rescaling and augmentation techniques such as horizontal/vertical shifts, zooming, and validation splitting, which helps enhance the model’s robustness. For the test set, images are normalized without augmentation. The images are resized to 64 X 64 with a batch size of 32.
# Sample Images Visualization
A few sample images from the training set are displayed to help you understand class distribution and image quality.
# CNN Architecture
- Designed a Convolutional Neural Network (CNN) with 3 convolutional layers (32, 64, 128 filters) for feature extraction.
- Utilized MaxPooling layers to reduce spatial dimensions and improve computational efficiency.
- Flattened the output of convolutional layers for feeding into fully connected layers.
- Implemented a fully connected Dense layer with 256 neurons and ReLU activation for feature learning.
- Added a Dropout layer (33%) to prevent overfitting.
- Used a sigmoid activation function in the output layer for binary classification tasks (0 or 1).
![Screenshot 2024-11-22 122434](https://github.com/user-attachments/assets/82dd6978-3324-4040-9e6d-9e5d8c9dab17)
# Model Visualisation
![Screenshot 2024-11-17 224421](https://github.com/user-attachments/assets/db7a4b01-1390-419f-9b91-6e4bae0d61c5)
# Training vs Validation (monitoring accuracy and loss)
![Screenshot 2024-11-22 122508](https://github.com/user-attachments/assets/52c8b21c-e99b-456c-b261-9b9a5b394c1b)
# Model Evaluation
# Accuracy:92% 
- The model correctly classified 92% of instances.
# Precision/Recall/F1-Score:
- def_front: Precision = 1.00, Recall = 0.87, F1 = 0.93 — The model perfectly identified def_front instances but missed some.
- ok_front: Precision = 0.82, Recall = 1.00, F1 = 0.90 — The model perfectly identified ok_front instances with some false positives.
# Confusion Matrix:
The model correctly classified 395 def_front and 262 ok_front samples, with 58 false positives for def_front.
# Sample predictions from the test set
![Screenshot 2024-11-22 122536](https://github.com/user-attachments/assets/233515ec-56d2-4592-b7e6-48f46cefc32f)
# Model deployment
https://castingdefectdetectionusingcnn-dv7oqpa4bbxopr2mdfdbug.streamlit.app/

