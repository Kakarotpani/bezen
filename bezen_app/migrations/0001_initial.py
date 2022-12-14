# Generated by Django 4.0.1 on 2022-09-17 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('f_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=60)),
                ('f_description', models.CharField(max_length=200)),
                ('f_procedure', models.TextField()),
                ('f_photo', models.ImageField(blank=True, null=True, upload_to='food_img')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('i_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ing', models.CharField(max_length=60)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bezen_app.food')),
            ],
        ),
    ]
