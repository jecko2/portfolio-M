# Generated by Django 4.0 on 2022-01-05 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0022_rename_project_yt_link_myproject_project_ig_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproject',
            name='project_iG_link',
            field=models.URLField(blank=True, default='https://www.instagram.com/pafiquinka/', null=True),
        ),
        migrations.AlterField(
            model_name='myproject',
            name='project_tw_link',
            field=models.URLField(blank=True, default='https://twitter.com/PQuinka', null=True),
        ),
    ]
