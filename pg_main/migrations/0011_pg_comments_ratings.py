# Generated by Django 4.1.7 on 2023-04-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg_main', '0010_alter_pg_amenities_attached_washroom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pg_comments',
            name='ratings',
            field=models.PositiveIntegerField(null=True),
        ),
    ]