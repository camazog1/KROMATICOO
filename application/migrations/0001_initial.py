# Generated by Django 4.2.4 on 2023-12-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ref', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='application/img/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
