# Modules
from flask import Flask, render_template, request, redirect
from PIL import Image
import os
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification

# Creating app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'GenderClassification/static/uploads'

# Load the processor and the model
processor = AutoImageProcessor.from_pretrained("rizvandwiki/gender-classification")
model = AutoModelForImageClassification.from_pretrained("rizvandwiki/gender-classification")

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file and allowed_file(file.filename):
            # Save the file
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Load and process the image
            image = Image.open(filepath)
            inputs = processor(images=image, return_tensors="pt")

            # Perform inference
            with torch.no_grad():
                outputs = model(**inputs)
            logits = outputs.logits
            predicted_class_idx = logits.argmax(-1).item()

            # Gender classification labels
            classes = ["Female", "Male"]
            predicted_gender = classes[predicted_class_idx]

            # Pass the image filename and prediction to the template
            return render_template("index.html", prediction=predicted_gender, image_file=filename)

    return render_template("index.html", prediction=None, image_file=None)

# Main part 
if __name__ == "__main__":
    app.run(debug=True)
