# Generated by Django 3.0 on 2021-08-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_pdf_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdf',
            field=models.FileField(upload_to='pdf'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video'),
        ),
    ]
