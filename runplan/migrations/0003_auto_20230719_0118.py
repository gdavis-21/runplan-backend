# Generated by Django 3.2.20 on 2023-07-19 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runplan', '0002_auto_20230712_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='effort',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='strengthChallenge',
        ),
        migrations.AddField(
            model_name='workout',
            name='pace',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workout',
            name='distance',
            field=models.CharField(max_length=200),
        ),
    ]
