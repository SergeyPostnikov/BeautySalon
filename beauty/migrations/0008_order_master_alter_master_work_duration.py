# Generated by Django 4.2.1 on 2023-05-28 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0007_alter_master_work_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.master', verbose_name='мастер'),
        ),
        migrations.AlterField(
            model_name='master',
            name='work_duration',
            field=models.IntegerField(verbose_name='стаж работы (лет)'),
        ),
    ]