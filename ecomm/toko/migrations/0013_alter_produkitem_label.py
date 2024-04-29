# Generated by Django 4.2 on 2024-04-29 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0012_alter_produkitem_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkitem',
            name='label',
            field=models.CharField(choices=[('NEW', 'primary'), ('SALE', 'info'), ('BEST', 'danger')], max_length=4),
        ),
    ]