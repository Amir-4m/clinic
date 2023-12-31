# Generated by Django 2.2.3 on 2019-08-05 18:40
import os
import shutil

from django.db import migrations, models
from django.core.files import File
import django.utils.timezone
from django.conf import settings
import ckeditor.fields
import fancy_imagefield.fields
import fancy_imagefield.validators


def make_about_us_page_defaults(apps, schema_editor):
    History = apps.get_model("about_us", "History")
    Faq = apps.get_model("about_us", "Faq")
    Stuff = apps.get_model("about_us", "Stuff")
    ClinicTeamMember = apps.get_model("about_us", "ClinicTeamMember")
    db_alias = schema_editor.connection.alias

    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)

    # Initial History
    history_image = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'static',
        'about_us',
        'images',
        'about-history.jpg'
    )
    history_image_name = os.path.join(
        settings.MEDIA_ROOT, 'about-history.jpg'
    )
    shutil.copy(history_image, history_image_name)
    with open(history_image_name, 'rb') as image:
        History.objects.using(db_alias).create(
            title="MedArt History",
            text=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                "Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum. "
                "Ut ac ligula sapien. Suspendisse cursus faucibus finibus. "
                "Curabitur ut augue finibus, luctus tortor at, ornare erat. Nulla facilisi. "
                "Sed est risus, laoreet et quam non, viverra accumsan leo. "
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                "Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum. "
                "Ut ac ligula sapien. Suspendisse cursus faucibus finibus. "
                "Curabitur ut augue finibus, luctus tortor at, ornare erat."
            ),
            image=File(image, name=os.path.basename(history_image_name))
        )

    # Initial Faq
    faqs_info = [
        {
            'question': 'Elit mir congue ligula et efficitur pellentesqu',
            'answer': (
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                'Donec malesuada lorem maximus mauris. Lorem ipsum dolor sit amet, '
                'consectetur adipiscing elit. Donec malesuada lorem maximus mauris.'
            )
        },
        {
            'question': 'Pulvinar elit mi. Integer congue ligula et efficitur',
            'answer': (
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                'Donec malesuada lorem maximus mauris. Lorem ipsum dolor sit amet, '
                'consectetur adipiscing elit. Donec malesuada lorem maximus mauris.'
            )
        },
        {
            'question': 'Pellentesque pulvinar elit mi. Integer congue',
            'answer': (
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                'Donec malesuada lorem maximus mauris. Lorem ipsum dolor sit amet, '
                'consectetur adipiscing elit. Donec malesuada lorem maximus mauris.'
            )
        }
    ]
    for faq_info in faqs_info:
        Faq.objects.using(db_alias).create(
            **faq_info
        )

    # Initial Stuff
    stuffs_info = [
        {
            'title': 'Professional',
            'description': (
                'Lorem ipsum dolor sit amet, cons ectetur adipiscing elit. Donec males uada lorem.'
            ),
            'logo': os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'static',
                'about_us',
                'images',
                'stuff-1.png'
            )
        },
        {
            'title': 'Quality',
            'description': (
                'Lorem ipsum dolor sit amet, cons ectetur adipiscing elit. Donec males uada lorem.'
            ),
            'logo': os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'static',
                'about_us',
                'images',
                'stuff-2.png'
            )
        }
    ]
    for stuf_info in stuffs_info:
        logo_name = os.path.join(
            settings.MEDIA_ROOT, os.path.basename(stuf_info['logo'])
        )
        shutil.copy(stuf_info['logo'], logo_name)

        with open(logo_name, 'rb') as logo:
            Stuff.objects.using(db_alias).create(
                title=stuf_info['title'],
                description=stuf_info['description'],
                logo=File(logo, name=os.path.basename(stuf_info['logo']))
            )

    # Initial Medical Team
    team_info = [
        {
            'name': 'Christinne Smith',
            'degree': 'PHD Surgeon',
            'avatar': os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'static',
                'about_us',
                'images',
                'team-1.jpg'
            )
        },
        {
            'name': 'Anna Gustav',
            'degree': 'PHD Surgeon',
            'avatar': os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'static',
                'about_us',
                'images',
                'team-2.jpg'
            )
        },
        {
            'name': 'Phillip Williams',
            'degree': 'PHD Surgeon',
            'avatar': os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'static',
                'about_us',
                'images',
                'team-3.jpg'
            )
        },
        {
            'name': 'Gina James',
            'degree': 'PHD Surgeon',
            'avatar': os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'static',
                'about_us',
                'images',
                'team-4.jpg'
            )
        }
    ]

    for member in team_info:
        avatar_name = os.path.join(
            settings.MEDIA_ROOT, os.path.basename(member['avatar'])
        )
        shutil.copy(member['avatar'], avatar_name)

        with open(avatar_name, 'rb') as avatar:
            ClinicTeamMember.objects.using(db_alias).create(
                name=member['name'],
                degree=member['degree'],
                avatar=File(avatar, name=os.path.basename(member['avatar']))
            )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicTeamMember',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                )),
                ('name', models.CharField(max_length=120)),
                ('degree', models.CharField(max_length=80)),
                ('avatar', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Clinic Team Member',
                'verbose_name_plural': 'Clinic Team Members',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                )),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Faq',
                'verbose_name_plural': 'Faqs',
            },
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                )),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Stuff',
                'verbose_name_plural': 'Stuffs',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                )),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('details_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'History',
                'verbose_name_plural': 'Histories',
            },
        ),
        migrations.RunPython(
            code=make_about_us_page_defaults,
        ),
        migrations.AddField(
            model_name='clinicteammember',
            name='created',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinicteammember',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='faq',
            name='created',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='history',
            name='created',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='stuff',
            name='created',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stuff',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='clinicteammember',
            name='avatar',
            field=models.ImageField(upload_to='', verbose_name='Avatar Image'),
        ),
        migrations.AlterField(
            model_name='clinicteammember',
            name='degree',
            field=models.CharField(max_length=80, verbose_name='Degree'),
        ),
        migrations.AlterField(
            model_name='clinicteammember',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(max_length=255, verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=100, verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='history',
            name='details_link',
            field=models.URLField(blank=True, null=True, verbose_name='Details Link'),
        ),
        migrations.AlterField(
            model_name='history',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='history',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='history',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='logo',
            field=models.ImageField(upload_to='', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='clinicteammember',
            name='avatar',
            field=fancy_imagefield.fields.ImageField(
                upload_to='',
                validators=[fancy_imagefield.validators.MaxSizeValidator(1024 * 512)],
                verbose_name='Avatar Image'
            ),
        ),
        migrations.AlterField(
            model_name='history',
            name='image',
            field=fancy_imagefield.fields.ImageField(
                upload_to='',
                validators=[fancy_imagefield.validators.MaxSizeValidator(1024 * 1024)],
                verbose_name='Image'
            ),
        ),
        migrations.AlterField(
            model_name='history',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='logo',
            field=fancy_imagefield.fields.ImageField(
                upload_to='',
                validators=[fancy_imagefield.validators.MaxSizeValidator(1024 * 256)],
                verbose_name='Logo'
            ),
        ),
    ]
