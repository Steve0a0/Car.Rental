# Generated by Django 4.1.7 on 2023-03-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_location_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='registeration_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]