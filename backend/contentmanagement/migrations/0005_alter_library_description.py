# Generated by Django 3.2.4 on 2023-02-23 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentmanagement', '0004_library_libraryfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
