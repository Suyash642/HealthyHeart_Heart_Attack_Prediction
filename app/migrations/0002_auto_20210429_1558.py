# Generated by Django 3.1.7 on 2021-04-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Healthyheart_Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_name', models.CharField(max_length=150)),
                ('Age', models.SmallIntegerField()),
                ('Gender', models.CharField(max_length=150)),
                ('Chestpaintype', models.SmallIntegerField()),
                ('RestBP', models.SmallIntegerField()),
                ('Cholestrol', models.SmallIntegerField()),
                ('Heartrate', models.SmallIntegerField()),
                ('Exercise_induced_angina', models.SmallIntegerField()),
                ('Oldpeak', models.FloatField()),
                ('Slope', models.SmallIntegerField()),
                ('No_of_vessels', models.SmallIntegerField()),
                ('Thal', models.SmallIntegerField()),
                ('Report_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='healthyheart',
            name='ECG',
        ),
        migrations.RemoveField(
            model_name='healthyheart',
            name='Sugar',
        ),
        migrations.AlterField(
            model_name='healthyheart',
            name='Report_date',
            field=models.DateField(),
        ),
    ]