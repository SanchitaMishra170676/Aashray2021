# Generated by Django 3.1.5 on 2021-04-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aashray', '0006_auto_20210428_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasma',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('All', 'All'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3),
        ),
    ]