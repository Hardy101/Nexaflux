# Generated by Django 5.0.4 on 2024-04-26 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_coinname_coin_coinname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Alert',
        ),
        migrations.DeleteModel(
            name='coin',
        ),
    ]
