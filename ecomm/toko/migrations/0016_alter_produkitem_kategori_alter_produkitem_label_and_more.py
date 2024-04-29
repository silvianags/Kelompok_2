# Generated by Django 4.2 on 2024-04-29 15:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('toko', '0015_alter_produkitem_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkitem',
            name='kategori',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sportwear'), ('OW', 'Outwear')], max_length=9),
        ),
        migrations.AlterField(
            model_name='produkitem',
            name='label',
            field=models.CharField(choices=[('NEW', 'primary'), ('SALE', 'info'), ('BEST', 'danger')], max_length=11),
        ),
        migrations.CreateModel(
            name='ProdukReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('komentar', models.TextField()),
                ('publish', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.BooleanField(default=True)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2)),
                ('produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='toko.produkitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='ProdukImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='produk.jpg', upload_to='product-images')),
                ('produk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_images', to='toko.produkitem')),
            ],
            options={
                'verbose_name_plural': 'Gambar Produk',
            },
        ),
        migrations.CreateModel(
            name='Kontak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('pesan', models.TextField()),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Kontak',
            },
        ),
    ]