# Generated by Django 4.2.10 on 2024-12-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_dailymission'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.PositiveIntegerField()),
                ('image', models.URLField()),
            ],
        ),
    ]
