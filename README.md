 # Cloud Computing Path

Creating RESTful APIs and deploying to Google Cloud Platform using [Google Cloud Run](https//cloud.google.com/run) for communication between Machine Learning Model and Mobile Development. and we use [Firebase (https://console.firebase.google.com/) to store the entire database for users as well as the list of locations.

## Firebase Realtime Database

The features we use in firebase are [Login Authentication](https://firebase.google.com/docs/auth), [Cloud Storage](https://firebase.google.com/docs/storage), [Realtime Database](https://firebase.google.com/docs/database), and [App distribution](https://firebase.google.com/docs/app-distribution).

## RESTful APIs

In making the RESTful APIs we use [Flask](https://flask.palletsprojects.com/) with some other dependencies which are [geopy](https://pypi.org/project/geopy/), [tensorflow](https://www.tensorflow.org/), [numpy](https://numpy.org/). and we also use [PHP](https://www.php.net/) as a bridge to the payment gateway service from Midtrans.

## List APIs services

In this section there is a list of all APIs

1.  Carbon-Footprint-API
2.  Payment-Gateway-API

---

## **API Carbon Footprint**

In this section there is a Carbon Footprint API that can be used to calculate the estimated carbon footprint generated based on the distance traveled. The response from the URL is in JSON format. For further documentation can be seen in the following image.

**Base URL:**

> <https://carbon-footprint-emission-jl4gfhbdkq-uc.a.run.app>

**Method:**

> POST

- ** Show Prediction Result **

  > <https://carbon-footprint-emission-jl4gfhbdkq-uc.a.run.app/>**predict/emission**

  This API is actually the main feature of this application but for now it is still not perfect and needs further development due to time constraints and implementation which we feel is quite difficult.

 **Required:**

 - **Request Body:**

    | Key           | Value       |
    | ------------- | ----------- |
    | Start_address | {cityName}  |

  **Response:**

  ```JSON
  {
    "predicted_emission": 33.4874382019043
  }
  ```
