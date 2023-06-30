from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    timestamp = models.DateTimeField(auto_now_add=True)
    predicted_label = models.CharField(max_length=255)  # Add this field

    def __str__(self):
        return f"Photo {self.id}"

class PredictedClass(models.Model):
    label = models.CharField(max_length=100)
    probability = models.FloatField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='predicted_classes')

    def __str__(self):
        return f"{self.label}: {self.probability}"