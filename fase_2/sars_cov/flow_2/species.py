#!/bin/env -S python3 -i

import requests, sys


def get_from_ensembl_by_id( tid, b='classification' ):  # classification|id
	ens_tax_url = "https://rest.ensembl.org/taxonomy/{}/{}?"
	r = requests.get( ens_tax_url.format( b, tid ), headers={ "Content-Type": "application/json" } )
	if not r.ok: return None
	return r.json()


taxids = list()
print( 'Enter taxonomy ids (one per line):' )
while True:
	tid = input()
	if tid: taxids.append( tid )
	else: break
with open( './species_f.txt', 'w' ) as file1, open( './species_v.tsv', 'w' ) as file2:
	for tid in taxids:
		t = get_from_ensembl_by_id( tid )
		k = 'scientific_name'
		family = list( map( lambda x: x[ k ], t ) )
		family = [ i for i in family[ :5 ] if i.endswith( 'ae' ) ]
		vulgar = t[ 0 ][ 'tags' ][ 'name' ]
		file1.write( ' '.join( reversed( family ) ) + '\n' )
		file2.write( '\t'.join( vulgar ) + '\n' )
		print( '{:7}'.format( t[ 0 ][ 'id' ] ), end='\r' )
