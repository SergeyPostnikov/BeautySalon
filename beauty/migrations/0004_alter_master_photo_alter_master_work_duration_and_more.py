# Generated by Django 4.2.1 on 2023-05-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0003_auto_20230528_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='master',
            name='work_duration',
            field=models.DurationField(blank=True, null=True, verbose_name='стаж работы'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='описание'),
        ),
    ]
