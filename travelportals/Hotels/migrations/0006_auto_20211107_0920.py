# Generated by Django 3.2.8 on 2021-11-07 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0005_auto_20211107_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='Banner_Image',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='Gallery',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item_images')),
                ('banner_image', models.ImageField(upload_to='item_images')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_item_images', to='Hotels.hotel')),
            ],
        ),
    ]