import requests

# Define the API endpoint
url = 'http://127.0.0.1:8000/photos/'

# Prepare the image file and other data
image_file = 'ovacado.jpg'  
latitude = 12.3456  
longitude = 78.9012  

# Create a multipart/form-data payload for the image file
files = {'image': open(image_file, 'rb')}
data = {'latitude': latitude, 'longitude': longitude}

# Send the POST request to the Django API
response = requests.post(url, data=data, files=files)

# Check the response status code and content
if response.status_code == 200:
    data = response.json()
    image_url = data.get('test4.png')
    predicted_classes = data.get('predicted_classes')
    print('Image uploaded successfully. URL:', image_url)
    print('Predicted classes:')
    for predicted_class in predicted_classes:
        label = predicted_class.get('label')
        probability = predicted_class.get('probability')
        print('Label:', label)
        print('Probability:', probability)
else:
    print('Error occurred:', response.status_code)
