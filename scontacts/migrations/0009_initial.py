# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'scontacts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('birth', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_review_time', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('rate', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('work_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('face', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('v1', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('v2', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('v3', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('service', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'scontacts', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'scontacts_contact')


    models = {
        u'scontacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'birth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'face': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_review_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'service': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'v1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'v2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'v3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'work_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['scontacts']