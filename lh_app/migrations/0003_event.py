# Generated by Django 5.0.2 on 2024-03-04 09:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lh_app', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_name', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('event_venue', models.CharField(default='Auditorium', max_length=55)),
                ('event_date', models.DateField(default=django.utils.timezone.now)),
                ('event_description', models.TextField()),
                ('event_pic', models.FileField(default='', upload_to='lh_app/event_images')),
            ],
        ),
    ]
