# Generated by Django 4.2.10 on 2024-12-12 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_storeitem_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='amassed_points',
            new_name='amassed_coins',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='points',
            new_name='coins',
        ),
    ]
