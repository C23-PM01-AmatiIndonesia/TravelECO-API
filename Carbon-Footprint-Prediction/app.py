from flask import Flask, request, jsonify, render_template
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import tensorflow as tf
import numpy as np

app = Flask(__name__)

geolocator = GoogleV3(api_key="AIzaSyD7h_1uMayp4FXcdaMGXVmrihLun5YOQnE")

model = tf.keras.models.load_model('model.h5')

@app.route('/')
def home():
    return "Server Connected"

@app.route('/predict_emission', methods=['POST'])
def predict_emission():
    start_address = request.form['start_address']

    try:
        start_location = geolocator.geocode(start_address)
        start_coordinates = (start_location.latitude, start_location.longitude)
        print("User Coordinate: ", start_coordinates)

        end_coordinates = (-8.3731286, 115.286756)
        print("Destination Coordinate: ", end_coordinates)

        distance = geodesic(start_coordinates, end_coordinates).kilometers
        print("Jarak perjalanan (km):", distance)

        new_data = np.array([[distance]])
        predicted_emission = model.predict(new_data)

        predicted_emission = float(predicted_emission[0][0])
        print("Prediksi Emisi Karbon: ", predicted_emission, "(kgCo2)")

        return jsonify({'predicted_emission': predicted_emission})

    except AttributeError:
        return jsonify({'error': 'Tidak dapat menemukan koordinat untuk alamat yang diberikan.'})

if __name__ == '__main__':
    app.run()
