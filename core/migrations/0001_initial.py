# Generated by Django 3.2.9 on 2021-11-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=128, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=128, verbose_name='e-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Quantidade em estoque')),
            ],
        ),
        migrations.CreateModel(
            name='Teste1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Test1', models.CharField(max_length=128, verbose_name='Teste')),
                ('TipoCharField', models.CharField(max_length=128, verbose_name='TipoCharField')),
                ('TipoEmail', models.EmailField(max_length=128, verbose_name='TipoEmail')),
                ('TipoTextField', models.TextField(max_length=512, verbose_name='TipoTextField')),
            ],
        ),
        migrations.CreateModel(
            name='Teste2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Test2', models.CharField(max_length=128, verbose_name='Test2')),
                ('TipoIntegerField', models.IntegerField(verbose_name='TipoIntegerField')),
                ('TipoDecimalField', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='TipoDecimalField')),
                ('TipoFloatField', models.FloatField(max_length=8, verbose_name='TipoFloatField')),
                ('TipoBooleanFieldTrue', models.BooleanField(default=True, verbose_name='TipoBooleanFieldTrue')),
                ('TipoBooleanFieldFalse', models.BooleanField(default=False, verbose_name='TipoBooleanFieldFalse')),
            ],
        ),
    ]