# Generated by Django 3.1.5 on 2021-04-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aashray', '0005_other_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpline',
            name='contact',
            field=models.CharField(max_length=13),
        ),
    ]
