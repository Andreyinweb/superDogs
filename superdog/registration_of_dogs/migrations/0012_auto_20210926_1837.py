# Generated by Django 3.2.7 on 2021-09-26 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration_of_dogs', '0011_auto_20210926_1701'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exhibitions',
            new_name='Exebitions',
        ),
        migrations.RemoveField(
            model_name='registrationexhibition',
            name='exebition_venue',
        ),
        migrations.AddField(
            model_name='registrationexhibition',
            name='exebition_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration_of_dogs.exebitions', verbose_name='Место проведения'),
            preserve_default=False,
        ),
    ]
