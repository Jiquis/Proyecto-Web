# Generated by Django 4.2.4 on 2023-12-07 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0006_participante_descripcion_participante_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apuesta',
            name='descripcion_apuesta',
            field=models.CharField(default='', max_length=100),
        ),
    ]
