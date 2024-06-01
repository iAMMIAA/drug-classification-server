# Generated by Django 5.0.6 on 2024-06-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informationdrug',
            fields=[
                ('namedrug', models.CharField(db_column='nameDrug', max_length=255, primary_key=True, serialize=False)),
                ('cites', models.CharField(blank=True, max_length=255)),
                ('detail', models.TextField(blank=True)),
                ('tagDrug', models.CharField(blank=True, db_column='tagDrug', max_length=255)),
                ('imgdrug', models.CharField(blank=True, db_column='imgDrug', max_length=255)),
                ('colordrug', models.CharField(blank=True, db_column='colorDrug', max_length=255)),
                ('shapedrug', models.CharField(blank=True, db_column='shapeDrug', max_length=255)),
                ('imprintdrug', models.CharField(blank=True, db_column='imprintDrug', max_length=255)),
                ('describedrug', models.TextField(blank=True, db_column='describeDrug')),
            ],
            options={
                'db_table': 'informationdrug',
                'managed': False,
            },
        ),
    ]
