# Generated by Django 3.2.4 on 2023-02-23 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contentmanagement', '0005_alter_library_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='file_attributes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='library',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owned_libraries', to='contentmanagement.user', verbose_name='صاحب'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='libraries', to='contentmanagement.User', verbose_name='کاربر\u200cها'),
        ),
        migrations.AlterUniqueTogether(
            name='library',
            unique_together={('owner', 'name', 'type')},
        ),
        migrations.RemoveField(
            model_name='library',
            name='user',
        ),
    ]
