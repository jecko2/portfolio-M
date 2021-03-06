# Generated by Django 4.0 on 2022-01-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0008_teammember_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertise',
            name='creative_design',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teammember',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
