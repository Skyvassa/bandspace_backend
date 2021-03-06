# Generated by Django 3.2.5 on 2021-07-15 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=100)),
                ('photo', models.TextField()),
                ('about', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('music_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.TextField()),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserFavBand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandfavusers', to='bandspace_app.band')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfavbands', to='bandspace_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='band',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bands', to='bandspace_app.user'),
        ),
    ]
