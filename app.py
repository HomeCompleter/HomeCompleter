from flask import Flask, render_template, request, jsonify, flash
import os
from chat import get_response
from _finding import *

# Allowed file formats (Image)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def Rename_Files(name):
    global user_images_folder
    count = 0
    # Iterate directory
    for path in os.listdir(user_images_folder):
        # check if current path is a file
        if os.path.isfile(os.path.join(user_images_folder, path)):
            count += 1
    return os.path.join(user_images_folder, f"Img_No_{count+1}.png")

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
        if image_file.filename != '' and allowed_file(image_file.filename):
            image_filename = Rename_Files(image_file.name)
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
    # response = get_response(text)
    response = Get_Input(text)
    message = {"answer": response}
    return jsonify(message)

# @app.route('/send_message', methods=['POST'])
# def send_message():
#     # Assume the client sends a JSON payload with the image URL and link
#     data = request.get_json()

#     # Extract image URL and link from the JSON payload
#     image_url = data.get('image_url')
#     link = data.get('link')

#     # Process the image and link as needed (e.g., save to a database, etc.)

#     # For simplicity, just echoing the received data back
#     response_data = {
#         'image_url': image_url,
#         'link': link
#     }

#     return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)