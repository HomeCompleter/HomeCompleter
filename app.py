from flask import Flask, render_template,request, jsonify
import os

from chat import get_response

app = Flask(__name__)

# Create the folder for user images if it doesn't exist
user_images_folder = "user_images"
os.makedirs(user_images_folder, exist_ok=True)

def process_image_input(image_filename):
    # Your image processing logic (e.g., using a machine learning model)
    # For simplicity, let's just echo the image filename
    return f"Image received: {image_filename}"

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/process', methods=['POST'])
def process_input():
    if 'file' in request.files:
        image_file = request.files['file']
        if image_file.filename != '':
            image_filename = os.path.join(user_images_folder, image_file.filename)
            image_file.save(image_filename)
            response = process_image_input(image_filename)
            return jsonify({'image_filename': image_filename, 'response': response})

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
     text = request.get_json().get("message")
     # TODO: check if text is valid
     response = get_response(text)
     message = {"answer": response}
     return jsonify(message)

if __name__ == "__main__":
     app.run(debug=True)
