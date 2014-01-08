# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            bases = (models.Model,),
            fields = [('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True),), ('question', models.CharField(max_length=200),), ('pub_date', models.DateTimeField(verbose_name='date published'),)],
            options = {},
            name = 'Poll',
        ),
        migrations.CreateModel(
            bases = (models.Model,),
            fields = [('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True),), ('poll', models.ForeignKey(to_field='id', to='polls.Poll'),), ('choice', models.CharField(max_length=200),), ('votes', models.IntegerField(),)],
            options = {},
            name = 'Choice',
        ),
    ]
