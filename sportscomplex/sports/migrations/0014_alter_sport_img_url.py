# Generated by Django 4.0.6 on 2022-09-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0013_alter_slot_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='img_url',
            field=models.CharField(default='https://uploads-ssl.webflow.com/617b224ba2374548fcc039ba/617b224ba237453ce1c0409b_hpfulq-1234-1024x512.jpg', help_text='(Copy-paste the sport-image url here)', max_length=2083, verbose_name='Image'),
        ),
    ]