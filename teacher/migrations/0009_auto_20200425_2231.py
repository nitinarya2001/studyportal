# Generated by Django 3.0.5 on 2020-04-25 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0008_auto_20200425_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.Section'),
        ),
    ]
