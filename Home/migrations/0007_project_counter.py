# Generated by Django 4.1.5 on 2023-03-06 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_remove_project_image_project_image1_project_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='counter',
            field=models.IntegerField(default=1, verbose_name='Counter of the project'),
            preserve_default=False,
        ),
    ]
