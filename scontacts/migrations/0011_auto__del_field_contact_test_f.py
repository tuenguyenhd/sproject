# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contact.test_f'
        db.delete_column(u'scontacts_contact', 'test_f')


    def backwards(self, orm):
        # Adding field 'Contact.test_f'
        db.add_column(u'scontacts_contact', 'test_f',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


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