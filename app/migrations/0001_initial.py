# Generated by Django 3.1.7 on 2021-03-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Healthyheart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_name', models.CharField(max_length=150)),
                ('Age', models.SmallIntegerField()),
                ('Gender', models.CharField(max_length=150)),
                ('Chestpaintype', models.SmallIntegerField()),
                ('RestBP', models.SmallIntegerField()),
                ('Cholestrol', models.SmallIntegerField()),
                ('Sugar', models.SmallIntegerField()),
                ('ECG', models.SmallIntegerField()),
                ('Heartrate', models.SmallIntegerField()),
                ('Exercise_induced_angina', models.SmallIntegerField()),
                ('Oldpeak', models.FloatField()),
                ('Slope', models.SmallIntegerField()),
                ('No_of_vessels', models.SmallIntegerField()),
                ('Thal', models.SmallIntegerField()),
                ('Report_date', models.DateTimeField()),
            ],
        ),
    ]
