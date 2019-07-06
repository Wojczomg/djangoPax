# Generated by Django 2.2.3 on 2019-07-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sofascore', '0005_livetable_tennis_ssmg'),
    ]

    operations = [
        migrations.CreateModel(
            name='TennisHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customId', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=20)),
                ('event_id', models.CharField(max_length=20, unique=True)),
                ('formatedStartDate', models.CharField(max_length=20)),
                ('homeTeam_name', models.CharField(max_length=20)),
                ('awayTeam_name', models.CharField(max_length=20)),
                ('current_home', models.IntegerField()),
                ('current_away', models.IntegerField()),
                ('period1_home', models.IntegerField()),
                ('period1_away', models.IntegerField()),
                ('period2_home', models.IntegerField()),
                ('period2_away', models.IntegerField()),
                ('period3_home', models.IntegerField()),
                ('period3_away', models.IntegerField()),
                ('odds_home', models.FloatField(blank=True, null=True)),
                ('odds_away', models.FloatField(blank=True, null=True)),
                ('tennis_ssmg', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]