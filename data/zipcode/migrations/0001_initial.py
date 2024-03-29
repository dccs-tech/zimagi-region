# Generated by Django 3.2.5 on 2021-11-07 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('country', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='zipcode_relation', to='country.country')),
            ],
            options={
                'verbose_name': 'zipcode',
                'verbose_name_plural': 'zipcodes',
                'db_table': 'region_zipcode',
                'ordering': ['name'],
                'abstract': False,
                'unique_together': {('country', 'name')},
            },
        ),
    ]
