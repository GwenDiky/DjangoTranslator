# Generated by Django 4.2.7 on 2023-11-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_course_date_remove_course_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetranslation',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]