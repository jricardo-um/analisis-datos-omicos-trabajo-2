#!/bin/env -S python3 -i
import pandas
import requests

uprot = "https://rest.uniprot.org/uniprotkb/{}.{}"
with open( '../flow_2/evidences.tsv' ) as file:
	database = pandas.read_csv( file, sep='\t' )

non_sars2 = []
yes_sars2 = []
for index, series in database.iterrows():
	if series[ 'evidence-2' ] == -2: non_sars2.append( series[ 'uniprot' ] )
	elif series[ 'evidence-2' ] == 2: yes_sars2.append( series[ 'uniprot' ] )
for f, l in ( ( './yes.fasta', yes_sars2 ), ( './non.fasta', non_sars2 ) ):
	with open( f, 'w' ) as file:
		for i in l:
			print( f'{i:^35}', end='\r' )
			resp = requests.get( uprot.format( i, 'fasta' ) )
			file.write( resp.text )
			file.write( '\n' )