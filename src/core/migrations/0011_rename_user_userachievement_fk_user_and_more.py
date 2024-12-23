# Generated by Django 4.2.10 on 2024-12-17 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_achievement_userachievement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userachievement',
            old_name='user',
            new_name='fk_user',
        ),
        migrations.AlterUniqueTogether(
            name='userachievement',
            unique_together={('fk_user', 'fk_achievement')},
        ),
        migrations.RemoveField(
            model_name='userachievement',
            name='progress',
        ),
    ]
