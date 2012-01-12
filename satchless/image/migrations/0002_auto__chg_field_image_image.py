# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Image.image'
        db.alter_column('image_image', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=255))


    def backwards(self, orm):
        
        # Changing field 'Image.image'
        db.alter_column('image_image', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))


    models = {
        'image.image': {
            'Meta': {'object_name': 'Image'},
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'image.thumbnail': {
            'Meta': {'unique_together': "(('image', 'size'),)", 'object_name': 'Thumbnail'},
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'original': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image.Image']"}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['image']
