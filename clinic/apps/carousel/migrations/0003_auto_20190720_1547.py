# Generated by Django 2.2.3 on 2019-07-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0002_slide_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slide',
            options={'ordering': ['priority'], 'verbose_name': 'Slide', 'verbose_name_plural': 'Slides'},
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='carousels_slides'),
        ),
    ]