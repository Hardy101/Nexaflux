# Generated by Django 5.0.4 on 2024-05-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts_and_data', '0004_alert_validuntil'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='status',
            field=models.TextField(default='active'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='validuntil',
            field=models.DateTimeField(default='2024-05-03 10:32'),
        ),
    ]
