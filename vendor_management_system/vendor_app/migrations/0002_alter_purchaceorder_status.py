# Generated by Django 5.0.4 on 2024-05-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaceorder',
            name='status',
            field=models.CharField(choices=[('pending,', 'pending,'), ('completed,', 'completed'), ('canceled', 'canceled')], max_length=50),
        ),
    ]