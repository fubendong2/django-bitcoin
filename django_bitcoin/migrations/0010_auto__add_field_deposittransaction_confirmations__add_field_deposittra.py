# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DepositTransaction.confirmations'
        db.add_column('django_bitcoin_deposittransaction', 'confirmations',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DepositTransaction.txid'
        db.add_column('django_bitcoin_deposittransaction', 'txid',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WalletTransaction.txid'
        db.add_column('django_bitcoin_wallettransaction', 'txid',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DepositTransaction.confirmations'
        db.delete_column('django_bitcoin_deposittransaction', 'confirmations')

        # Deleting field 'DepositTransaction.txid'
        db.delete_column('django_bitcoin_deposittransaction', 'txid')

        # Deleting field 'WalletTransaction.txid'
        db.delete_column('django_bitcoin_wallettransaction', 'txid')


    models = {
        'django_bitcoin.bitcoinaddress': {
            'Meta': {'object_name': 'BitcoinAddress'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'least_received': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '8'}),
            'least_received_confirmed': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '8'}),
            'wallet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addresses'", 'null': 'True', 'to': "orm['django_bitcoin.Wallet']"})
        },
        'django_bitcoin.deposittransaction': {
            'Meta': {'object_name': 'DepositTransaction'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['django_bitcoin.BitcoinAddress']"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '8'}),
            'confirmations': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'txid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'wallet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['django_bitcoin.Wallet']"})
        },
        'django_bitcoin.historicalprice': {
            'Meta': {'object_name': 'HistoricalPrice'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'params': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'})
        },
        'django_bitcoin.payment': {
            'Meta': {'object_name': 'Payment'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'}),
            'amount_paid': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'transactions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['django_bitcoin.Transaction']", 'symmetrical': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {}),
            'withdrawn_total': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'})
        },
        'django_bitcoin.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'django_bitcoin.wallet': {
            'Meta': {'object_name': 'Wallet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'last_balance': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '8'}),
            'transaction_counter': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'transactions_with': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['django_bitcoin.Wallet']", 'through': "orm['django_bitcoin.WalletTransaction']", 'symmetrical': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        'django_bitcoin.wallettransaction': {
            'Meta': {'object_name': 'WalletTransaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'from_wallet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_transactions'", 'to': "orm['django_bitcoin.Wallet']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_bitcoinaddress': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'to_wallet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'received_transactions'", 'null': 'True', 'to': "orm['django_bitcoin.Wallet']"}),
            'txid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['django_bitcoin']