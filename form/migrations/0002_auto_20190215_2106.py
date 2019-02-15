# Generated by Django 2.1.5 on 2019-02-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='about_me',
            field=models.TextField(blank='True', default='', max_length=350),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='email_id',
            field=models.EmailField(blank='True', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='last_name',
            field=models.CharField(blank='True', default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.CharField(blank='True', default='', max_length=13),
        ),
    ]
