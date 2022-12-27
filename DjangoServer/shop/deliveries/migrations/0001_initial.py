# Generated by Django 4.1.4 on 2022-12-27 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('detail_address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'shop_deliveries',
            },
        ),
    ]
