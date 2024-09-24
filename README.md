# CODXO
Welcome to the CODXO repository! This repository contains a collection of projects completed during my internship at CodXo in the field of Artificial Intelligence. <br/>
<br/>

# 1. Shah GPT Chatbot
Shah GPT is a conversational AI chatbot powered by the Google Gemini API. This chatbot can answer a wide range of questions, making it a useful tool for users to interact with. <br/>
<br/>

### Key Features:
* Supports Google Gemini API for generating responses.
* Users can ask any question, and the chatbot provides relevant answers.
* Built using Flask for the backend.
* A simple, elegant design using HTML, CSS (style.css), and JavaScript (scripts.js) for the frontend. <br/>
<br/>

### File Structure:
* app.py: The main Flask application.
* configure.py: Stores the API key and configurations.
* templates/index.html: Frontend HTML file for the chatbot interface.
* static/style.css: CSS file for styling the chatbot interface.
* static/scripts.js: JavaScript file for chatbot interaction. <br/>
<br/>

### How to Run:
1. Clone the repository:

   ```bash
   git clone https://github.com/Shah114/CODXO.git
   ```

2. Navigate to the chatbot directory:

   ```bash
   cd src/chatbot
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```
<br/>

# 2. Gender Classification
The Gender Classification project is a web app that classifies the gender of a person based on an uploaded image. It uses a pretrained model from rizvandwiki/gender-classification available in the transformers library. <br/>
<br/>

### Key Features:
* Uses Flask to serve the web app.
* Implements rizvandwiki/gender-classification for gender prediction.
* Simple and intuitive web interface for uploading and testing images.
* Styled using HTML and CSS (style.css) for the frontend.
* Uploads folder to store user-submitted images temporarily. <br/>
<br/>

### File Structure:
* app.py: The main Flask application for handling image uploads and classification.
* templates/index.html: Frontend HTML file for uploading images.
* static/style.css: CSS file for styling the web interface.
* static/uploads/: Directory where test images are stored. <br/>
<br/>

### How to Run:
1. Clone the repository:

   ```bash
   git clone https://github.com/Shah114/CODXO.git
   ```

2. Navigate to the gender classification directory:

   ```bash
   cd src/GenderClassification
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```
<br/>

# Syrup Bottle Detection
The Syrup Bottle Detection project is an object detection system trained using the YOLOv8n model. The model has been trained on a custom dataset to detect and count syrup bottles in images and videos. <br/>

### Key Features:
* YOLOv8n model from the ultralytics module for efficient object detection.
* Trained on a custom dataset of syrup bottles with separate directories for training, validation, and testing data.
* A config.yaml file that defines the dataset directory paths for training, validation, and testing.
* A sample video for testing the model’s performance.
* The project includes the output video generated after running the detection on the sample video. <br/>
<br/>

### File Structure:
* SyrupProject.ipynb: Contains the code for loading the YOLOv8n model and running inference on images or videos.
* config.yaml: Configuration file defining the directories for training, testing, and validation datasets.
* sample_video.mp4: A sample video for testing the model’s performance on syrup bottle detection.
* output_video.mp4: The output video showing the model's detection results. <br/>
<br/>

### How to Run:
1. Clone the repository:

   ```bash
   git clone https://github.com/Shah114/CODXO.git
   ```
2. Navigate to the syrup bottle detection directory:

   ```bash
   cd src/ObjectDetection
   ```
3. Run the model on the sample video.
4. The output will be saved as output_video.mp4 in the same directory. <br/>
<br/>

