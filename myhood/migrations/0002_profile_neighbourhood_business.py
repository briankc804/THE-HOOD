# Generated by Django 4.0.4 on 2022-06-21 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myhood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='Profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=60)),
                ('hood_logo', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('health_tell', models.IntegerField(blank=True, null=True)),
                ('police_number', models.IntegerField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='myhood.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='myhood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='myhood.profile')),
            ],
        ),
    ]
