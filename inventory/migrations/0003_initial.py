# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SystemModel'
        db.create_table('inventory_systemmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sku_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('family', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('inventory', ['SystemModel'])

        # Adding model 'System'
        db.create_table('inventory_system', (
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.SystemModel'])),
        ))
        db.send_create_signal('inventory', ['System'])

        # Adding model 'PeripheralModel'
        db.create_table('inventory_peripheralmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('inventory', ['PeripheralModel'])

        # Adding model 'Peripheral'
        db.create_table('inventory_peripheral', (
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.PeripheralModel'])),
        ))
        db.send_create_signal('inventory', ['Peripheral'])

        # Adding model 'Accessory'
        db.create_table('inventory_accessory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('stock', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('minimum', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('inventory', ['Accessory'])


    def backwards(self, orm):
        # Deleting model 'SystemModel'
        db.delete_table('inventory_systemmodel')

        # Deleting model 'System'
        db.delete_table('inventory_system')

        # Deleting model 'PeripheralModel'
        db.delete_table('inventory_peripheralmodel')

        # Deleting model 'Peripheral'
        db.delete_table('inventory_peripheral')

        # Deleting model 'Accessory'
        db.delete_table('inventory_accessory')


    models = {
        'inventory.accessory': {
            'Meta': {'object_name': 'Accessory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'minimum': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stock': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'inventory.peripheral': {
            'Meta': {'object_name': 'Peripheral'},
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.PeripheralModel']"}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'inventory.peripheralmodel': {
            'Meta': {'object_name': 'PeripheralModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'inventory.system': {
            'Meta': {'object_name': 'System'},
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.SystemModel']"}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'inventory.systemmodel': {
            'Meta': {'object_name': 'SystemModel'},
            'family': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sku_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['inventory']