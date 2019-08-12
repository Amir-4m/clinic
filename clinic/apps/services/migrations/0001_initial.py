# Generated by Django 2.2.3 on 2019-08-05 18:57
import os
import shutil

from django.core.files import File
from django.conf import settings
import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone
import fancy_imagefield.fields
import fancy_imagefield.validators


def initial_services_page(apps, schema_editor):
    Article = apps.get_model("services", "Article")
    DescriptionTab = apps.get_model("services", "DescriptionTab")
    db_alias = schema_editor.connection.alias

    Article.objects.using(db_alias).create(
        title='Only Top Quality Services',
        description=(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
            'Donec malesuada lorem ma ximus mauris scelerisque, at rutrum nulla dictum. '
            'Ut ac ligula sapien. Suspendisse cursus faucibus finibus. Curabitur ut '
            'augue finibus, luctus tortor at, ornare erat. Nulla facilisi. Sed est risus, '
            'laoreet et quam non, malesuada viverra accumsan leo.'
        )
    )

    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)

    tab_image = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'static',
        'services',
        'images',
        'service-tab-img.png'
    )
    tab_image_name = os.path.join(
        settings.MEDIA_ROOT, 'service-tab-img.png'
    )
    shutil.copy(tab_image, tab_image_name)

    tab_names = [
        'Pellentesque pulvinar', 'Pellentesque lacinia',
        'Consectetur diam', 'CMauris tortor', 'Phasellus sit amet'
    ]
    for name in tab_names:
        with open(tab_image_name, 'rb') as image:
            DescriptionTab.objects.using(db_alias).create(
                name=name,
                title='Scelerisque, at rutrum nulla dictum. Ut ac ligula sapien.',
                description=(
                    'Amet, consectetur adipiscing elit. Donec malesuada lorem maximus mauris '
                    'scelerisque, at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse '
                    'cursus faucibus finibus. Curabitur ut augue finibus, luctus tortor at, '
                    'ornare erat. Nulla facilisi. Sed est risus, laoreet et quam non, viverra '
                    'accumsan leo. Amet, consectetur adipiscing elit. Donec malesuada lorem '
                    'maximus mauris scelerisque, at rutrum nulla dictum. Ut ac ligula sapien. '
                    'Suspendisse cursus faucibus finibus'
                ),
                image=File(image, name=os.path.basename(tab_image_name))
            )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                )),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('read_more_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='DescriptionTab',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                )),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Service Description',
                'verbose_name_plural': 'Services Descriptions',
            },
        ),
        migrations.RunPython(
            code=initial_services_page,
        ),
        migrations.AlterModelOptions(
            name='descriptiontab',
            options={'verbose_name': 'Description Tab', 'verbose_name_plural': 'Description Tabs'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='descriptiontab',
            name='created_at',
        ),
        migrations.AddField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='descriptiontab',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='descriptiontab',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='read_more_link',
            field=models.URLField(blank=True, null=True, verbose_name='Read More Link'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=80, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='descriptiontab',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='descriptiontab',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='descriptiontab',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='descriptiontab',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='descriptiontab',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='descriptiontab',
            name='image',
            field=fancy_imagefield.fields.ImageField(upload_to='', validators=[fancy_imagefield.validators.MaxSizeValidator(1024)], verbose_name='Image'),
        ),
    ]
