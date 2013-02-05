# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AssetModel'
        db.create_table('inventory_assetmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('friendly_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('barcode_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('inventory', ['AssetModel'])

        # Adding model 'Asset'
        db.create_table('inventory_asset', (
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.AssetModel'])),
        ))
        db.send_create_signal('inventory', ['Asset'])


    def backwards(self, orm):
        # Deleting model 'AssetModel'
        db.delete_table('inventory_assetmodel')

        # Deleting model 'Asset'
        db.delete_table('inventory_asset')


    models = {
        'inventory.asset': {
            'Meta': {'object_name': 'Asset'},
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.AssetModel']"}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'})
        },
        'inventory.assetmodel': {
            'Meta': {'object_name': 'AssetModel'},
            'barcode_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'friendly_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['inventory']