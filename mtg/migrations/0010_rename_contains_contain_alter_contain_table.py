# Generated by Django 4.1 on 2023-12-02 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtg', '0009_contains_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contains',
            new_name='Contain',
        ),
        migrations.AlterModelTable(
            name='contain',
            table='contain',
        ),
    ]
