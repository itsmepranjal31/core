# Generated by Django 5.1.6 on 2025-03-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_id', models.IntegerField()),
                ('index', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('tags', models.JSONField(default=list)),
            ],
        ),
        migrations.AddField(
            model_name='contest',
            name='questions',
            field=models.ManyToManyField(blank=True, to='contests.question'),
        ),
    ]
