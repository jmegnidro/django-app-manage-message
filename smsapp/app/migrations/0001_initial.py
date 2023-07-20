# Generated by Django 2.2.28 on 2023-07-08 11:25

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientBoxs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailCampagne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150, verbose_name='Objet')),
                ('message', models.TextField(max_length=1000)),
                ('attachement_piece', models.FileField(blank=True, null=True, upload_to='emailattachement', verbose_name='piece jointe')),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephon', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='MessagesWhatsapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corps', models.TextField(max_length=200)),
                ('recipient', models.ManyToManyField(to='app.ClientBoxs')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Entreprise')),
            ],
        ),
        migrations.CreateModel(
            name='MessagesDiffusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corps', models.TextField(max_length=200)),
                ('recipient', models.ManyToManyField(primary_key={}, to='app.ClientBoxs')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Entreprise')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corps', models.TextField(max_length=200)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ClientBoxs')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Entreprise')),
            ],
        ),
    ]
