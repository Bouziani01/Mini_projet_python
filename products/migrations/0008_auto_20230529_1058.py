# Generated by Django 2.1 on 2023-05-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
