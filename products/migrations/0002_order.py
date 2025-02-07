# Generated by Django 2.1 on 2023-05-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=300)),
                ('zipcode', models.CharField(max_length=300)),
                ('date_commande', models.DateTimeField(auto_now=True)),
                ('total', models.CharField(max_length=300)),

            ],
        ),
    ]
