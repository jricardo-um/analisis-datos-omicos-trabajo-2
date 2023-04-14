#!/bin/env -S python3 -i
import os
import pandas
import requests
import sys

### parse arguments like `key` or `key=value`
sysargs = dict( arg.partition( '=' )[ ::2 ] for arg in sys.argv[ 1: ] )
"""
fasta="galaxy output file.tabular"
index=0 # column for accession id 
fasta="my download.fasta"
uniprot_only # avoid external databases
"""

### rest url services
cluster_url = "https://rest.uniprot.org/uniref/{}.{}"
protein_url = {
	"UniProtKB ID": "https://rest.uniprot.org/uniprotkb/{}.{}",
	"UniParc": "https://rest.uniprot.org/uniparc/{}.{}",
}
if 'uniprot_only' in sysargs: protein_url.pop( "UniParc" )

### get cluster list from results
if 'table' in sysargs: galaxy_output = sysargs[ 'table' ]
else: raise SystemError( 'You must provide the .tabular results file via command line.' )
with open( galaxy_output ) as file:
	clusters = pandas.read_csv( file, sep='\t', header=None )
if 'index' in sysargs:
	i = sysargs[ 'index' ]
	try:
		i = int( i )
	except:
		raise ValueError( 'The column index must be an integer.' )
else:
	i = 0
clusters = clusters[ i ].values
### get fasta for each result
clen = len( clusters )


def save_proteins_from_cluster( clen, cnum, cfile, msg1, member_list ):
	mlen = len( member_list )
	for mnum, member in enumerate( member_list ):
		msg2 = msg1 + ', member {}'
		pct = ( cnum + mnum / mlen ) / clen
		print( msg2.format( pct, cnum, mnum ), end='\r' )
		mt = member[ 'memberIdType' ]
		mi = member[ 'memberId' ]
		if mt in protein_url:
			resp2 = requests.get( protein_url[ mt ].format( mi, 'fasta' ) )
			with open( cfile, 'a' ) as file:
				file.write( resp2.text )
				file.write( '\n' )


for cnum, cluster in enumerate( clusters ):
	if 'fasta' in sysargs: cfile = sysargs[ 'fasta' ]
	else: cfile = './member_downloads/' + cluster + '.fasta'
	os.makedirs( os.path.dirname( cfile ), exist_ok=True )
	msg1 = '\x1B[2K [{:>6.1%}] Processing cluster {}'
	pct = cnum / clen
	print( msg1.format( pct, cnum ), end='\r' )
	resp = requests.get( cluster_url.format( cluster, 'json' ) )
	resp = resp.json()
	save_proteins_from_cluster( clen, cnum, cfile, msg1, [ resp[ "representativeMember" ] ] )
	try:
		save_proteins_from_cluster( clen, cnum, cfile, msg1, resp[ 'members' ] )
	except:
		continue
print( '\x1B[2K [100.0%] Done!' )
