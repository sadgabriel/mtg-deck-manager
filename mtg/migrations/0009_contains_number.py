# Generated by Django 4.1 on 2023-12-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtg', '0008_alter_contains_cardname_alter_contains_deckname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contains',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
