# Generated by Django 4.0 on 2022-01-05 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0023_alter_myproject_project_ig_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myselfmodel',
            name='home_img',
            field=models.ImageField(default='home.jpg', upload_to='media/images/'),
        ),
    ]
