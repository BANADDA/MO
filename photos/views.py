import traceback
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Photo, PredictedClass
from .serializers import PhotoSerializer
import os
import tempfile

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def create(self, request, *args, **kwargs):
        try:
            image_file = request.data['image']
            timestamp = request.data.get('timestamp')

            # Save the uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(image_file.read())
                temp_file_path = temp_file.name

            # Load the model
            model = load_model("models/mobile_net.h5", compile=False)

            # Load the labels
            class_names = open("models/labels.txt", "r").readlines()

            # Create the array of the right shape to feed into the keras model
            # The 'length' or number of images you can put into the array is
            # determined by the first position in the shape tuple, in this case 1
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            # Load and preprocess the image
            image = Image.open(temp_file_path).convert("RGB")
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
            image_array = np.asarray(image)
            normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
            data[0] = normalized_image_array

            # Perform the prediction
            prediction = model.predict(data)
            top_predictions = np.argsort(prediction)[0][::-1][:4]
            predicted_classes = [
                {
                    'label': class_names[index].strip(),
                    'probability': prediction[0][index]
                }
                for index in top_predictions
            ]

            # Create a new Photo instance with the processed data
            photo = Photo(image=image_file, timestamp=timestamp)
            photo.save()

            # Update the predicted labels for the Photo instance
            for predicted_class in predicted_classes:
                PredictedClass.objects.create(
                    label=predicted_class['label'],
                    probability=predicted_class['probability'],
                    photo=photo
                )

            # Serialize the created Photo instance and predicted classes
            serializer = self.get_serializer(photo)
            response_data = serializer.data
            response_data['predicted_classes'] = predicted_classes

            # Find the class with the highest probability
            highest_probability_class = max(predicted_classes, key=lambda x: x['probability'])

            # Format the output as a list of one dictionary
            output = [{'msg': f"{highest_probability_class['label']} {highest_probability_class['probability']}"}]

            # Delete the temporary file
            os.remove(temp_file_path)

            return Response(output)

        except Exception as e:
            traceback.print_exc()
            # Get the exception name
            exception_name = type(e).__name__

            message = f"Sorry, an error: '{exception_name}' occurred"

            return Response([{'msg': message}], status=status.HTTP_500_INTERNAL_SERVER_ERROR)

