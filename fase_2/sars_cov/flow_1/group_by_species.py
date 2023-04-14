#!/bin/env -S python3 -i
import os
import pandas
import regex
import sys

### parse arguments like `key` or `key=value`
sysargs = dict( arg.partition( '=' )[ ::2 ] for arg in sys.argv[ 1: ] )
"""
table="galaxy output file.tabular"
index=0 # column for header
tsv="my table.tsv"
"""

### get cluster list from results
if 'table' in sysargs: galaxy_output = sysargs[ 'table' ]
else: raise SystemError( 'You must provide the .tabular results file via command line.' )
with open( galaxy_output ) as file:
	results = pandas.read_csv( file, sep='\t', header=None )
if 'index' in sysargs:
	i = sysargs[ 'index' ]
	try:
		i = int( i )
	except:
		raise ValueError( 'The column index must be an integer.' )
else:
	i = 0
template = pandas.DataFrame( {
	'uniprot': [],
	'species': [],
	'taxid': [],
	'name': [],
	'score': [],
} )
searches = {
	'species': regex.compile( r'(OS=)([^=]*)( )' ),
	'taxid': regex.compile( r'(OX=)([^=]*)( )' ),
	'name': regex.compile( r'(GN=)([^=]*)( )' ),
}
id_search = regex.compile( r'(tr|sp)\|([^ ]*)\|([^ ]*)' )
for r, row in results.iterrows():
	temp = dict()
	temp[ 'score' ] = row[ 1 ]
	temp[ 'uniprot' ] = id_search.search( row[ 0 ] ).group( 2 )
	for key in searches:
		try:
			temp[ key ] = searches[ key ].search( row[ i ] ).group( 2 )
		except:
			temp[ key ] = None
	template = pandas.concat( [ template, pandas.DataFrame( pandas.Series( temp ) ).T ] )

if 'tsv' in sysargs: filename = sysargs[ 'tsv' ]
else: filename = './filtered.tsv'
with open( filename, 'w' ) as file:
	template.to_csv( file, sep='\t' )
