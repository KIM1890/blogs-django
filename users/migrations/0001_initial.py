# Generated by Django 4.0 on 2022-02-27 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captions', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
