# Generated by Django 4.1.3 on 2023-09-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petronexa_app', '0002_post_short_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
