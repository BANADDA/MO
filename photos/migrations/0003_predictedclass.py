# Generated by Django 4.2.2 on 2023-06-07 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_predicted_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictedClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('probability', models.FloatField()),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predicted_classes', to='photos.photo')),
            ],
        ),
    ]
