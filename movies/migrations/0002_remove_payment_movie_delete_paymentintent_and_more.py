# Generated by Django 4.0.4 on 2022-05-30 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='movie',
        ),
        migrations.DeleteModel(
            name='PaymentIntent',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
