# Generated by Django 3.0.8 on 2020-08-08 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default-profile-pic.jpg', null=True, upload_to=''),
        ),
    ]