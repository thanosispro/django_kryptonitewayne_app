# Generated by Django 5.0.6 on 2024-06-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('games_id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(default='', max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='', upload_to='images/')),
                ('date', models.DateField(auto_now_add=True)),
                ('download_url', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
