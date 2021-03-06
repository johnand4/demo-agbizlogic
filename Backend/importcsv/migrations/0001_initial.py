# Generated by Django 4.0.1 on 2022-02-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Memo', models.TextField()),
                ('Payee', models.CharField(max_length=100)),
                ('Tags', models.CharField(max_length=100)),
                ('Total_by_cat', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Payment', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Deposit', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Cat', models.CharField(max_length=100)),
            ],
        ),
    ]
