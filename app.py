from flask import Flask, request, jsonify, render_template
import os
import logging
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

# Set environment variables
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Core application class
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Initialize the app-level classifier
clApp = ClientApp()

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/ping", methods=['GET'])
@cross_origin()
def health_check():
    return jsonify({"status": "running"}), 200


@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    try:
        logging.info("Training started...")
        os.system("python main.py")  # Consider using subprocess for more control
        logging.info("Training completed successfully.")
        return jsonify({"message": "Training completed successfully!"})
    except Exception as e:
        logging.error(f"Training failed: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image_data = request.json.get('image')

        if image_data is None:
            return jsonify({"error": "No image data provided"}), 400

        decodeImage(image_data, clApp.filename)
        logging.info("Image decoded successfully.")

        result = clApp.classifier.predict()
        logging.info(f"Prediction result: {result}")

        return jsonify(result)

    except Exception as e:
        logging.error(f"Prediction failed: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  # For AWS or container deployment
