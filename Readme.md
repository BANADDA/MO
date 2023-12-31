# Maize Disease Diagnosis API Model Documentation

This API model allows you to upload a maize image and get predictions for the class labels of the image using a pre-trained model. It is built using Django and Keras.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Examples](#examples)
- [Authors](#Authors)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before getting started, make sure you have the following installed:

- [Python](https://www.python.org/downloads/) 3.x
- [Django](https://www.djangoproject.com/)
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>

## Usage

1. cd ModelAPI

2. pip install -r requirements.txt

3. python manage.py runserver

## Endpoints

The API provides the following endpoints:

### Upload Photo and Get Predictions

- **URL:** `/photos/`
- **Method:** `POST`
- **Parameters:**
  - `image` (file): The image file to be uploaded.
  - `timestamp` (optional): The timestamp associated with the image.
- **Response:**
  - `id` (integer): The ID of the uploaded photo.
  - `image_url` (string): The URL of the uploaded photo.
  - `predicted_classes` (array): An array of predicted class labels and their probabilities.
    - `label` (string): The predicted class label.
    - `probability` (float): The probability of the predicted class.

## Examples

You can use the provided `test.py` script to test the API. Make sure to update the necessary variables (API endpoint, image file path, latitude, longitude) in the script.

python test.py

## Authors
**Mubaraka Banadda**
Contact: [mubarakabanadda68@gmail.com](mubarakabanadda68@gmail.com)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE).
#   M o d e l A P I  
 #   M o d e l A P I _ C O D E  
 