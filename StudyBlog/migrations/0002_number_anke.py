# Generated by Django 4.2.3 on 2023-07-23 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='anke',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
