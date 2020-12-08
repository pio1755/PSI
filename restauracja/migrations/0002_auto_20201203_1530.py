# Generated by Django 2.2.17 on 2020-12-03 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restauracja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Danie',
            fields=[
                ('idDanie', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=45)),
                ('cena', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('idKlient', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=45)),
                ('haslo', models.CharField(max_length=45)),
                ('adres', models.CharField(max_length=45)),
                ('nrTelefonu', models.IntegerField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Platnosc',
            fields=[
                ('idPlatnosc', models.AutoField(primary_key=True, serialize=False)),
                ('rodzaj', models.CharField(choices=[('Na_miejscu', 'Na_miejscu'), ('przelew', 'Przelew')], default='przelew', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Restauracja',
            fields=[
                ('idRestauracja', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=45)),
                ('adres', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('idZamowienie', models.AutoField(primary_key=True, serialize=False)),
                ('dania', models.CharField(max_length=200)),
                ('dataZamowienia', models.DateField()),
                ('kwota', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restauracja.Klient')),
            ],
        ),
        migrations.DeleteModel(
            name='TEST',
        ),
        migrations.AddField(
            model_name='platnosc',
            name='zamowienie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restauracja.Zamowienie'),
        ),
        migrations.AddField(
            model_name='danie',
            name='restauracja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restauracja.Restauracja'),
        ),
        migrations.AddField(
            model_name='danie',
            name='zamowienie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restauracja.Zamowienie'),
        ),
    ]
