# Generated by Django 4.0 on 2022-01-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0017_alter_myselfmodel_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myselfmodel',
            name='profile_pic',
            field=models.ImageField(default='me1.jpg', upload_to='media/images/'),
        ),
    ]
