# Generated by Django 4.0 on 2022-01-05 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0009_expertise_creative_design_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertise',
            name='creative_default',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]