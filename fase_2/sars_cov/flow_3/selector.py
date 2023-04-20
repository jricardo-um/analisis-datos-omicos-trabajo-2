#!/bin/env -S python3 -i
import pandas
import regex
import requests

uprot = "https://rest.uniprot.org/uniprotkb/{}.{}"
with open( '../flow_2/evidences.tsv' ) as file:
	database = pandas.read_csv( file, sep='\t' )

non_sars2 = []
yes_sars2 = []
unk_sars2 = []
for index, series in database.iterrows():
	if series[ 'evidence-2' ] == -2: non_sars2.append( series[ 'uniprot' ] )
	elif series[ 'evidence-2' ] == 2: yes_sars2.append( series[ 'uniprot' ] )
	elif series[ 'score' ] > 1400: unk_sars2.append( series[ 'uniprot' ] )
for f, l in ( ( 'yes', yes_sars2 ), ( 'non', non_sars2 ), ( 'lss', unk_sars2 ) ):
	with open( f'./more/{f}.fasta', 'a' ) as file:
		rgp = regex.compile( r'(tr|sp)\|([^ ]*)\|([^ ]*)' )
		rgt = regex.compile( r'(OS=)([^=]*)( )' )
		rgx = regex.compile( r'(OX=)([^=]*)( )' )
		taxids = set()
		for i in l:
			resp = requests.get( uprot.format( i, 'fasta' ) )
			txt = resp.text.splitlines()
			protein_id = rgp.search( txt[ 0 ] ).group( 2 )
			tax_id = rgx.search( txt[ 0 ] ).group( 2 )
			tax_nm = rgt.search( txt[ 0 ] ).group( 2 ).replace( ' ', '_' )
			if tax_id in taxids or 'Fragment' in txt[ 0 ]: continue
			else: taxids.add( tax_id )
			txt[ 0 ] = '>{}|{}|{}|{}'.format( f, protein_id, tax_id, tax_nm )
			print( txt[ 0 ], end=' ' * 15 + '\r' )
			file.write( '\n'.join( txt ) )
			file.write( '\n' * 2 )
