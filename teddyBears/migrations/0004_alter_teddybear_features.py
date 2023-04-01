# Generated by Django 3.2.15 on 2023-04-01 00:42

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teddyBears', '0003_alter_teddybear_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teddybear',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('moveable arms', 'Moveable arms'), ('moveable legs', 'Moveable legs'), ('button eyes', 'Button eyes'), ('embroidered eyes', 'Embroidered eyes'), ('satin bow', 'Satin bow'), ('growler', 'Growler'), ('jingle bell', 'Jingle bell'), ('ribbon', 'Ribbon'), ('heart-shaped nose', 'Heart-shaped nose'), ('paw pads', 'Paw pads'), ('bean filling', 'Bean filling'), ('jointed', 'Jointed')], max_length=255),
        ),
    ]
