#!/bin/env -S python3 -i
import pandas
import itertools
import collections


def sliding_window( iterable, n ):
	# sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
	it = iter( iterable )
	window = collections.deque( itertools.islice( it, n ), maxlen=n )
	if len( window ) == n:
		yield tuple( window )
	for x in it:
		window.append( x )
		yield tuple( window )


with open( 'non_sl.txt' ) as file:
	nondb = pandas.read_csv( file, sep='\t', skiprows=7, index_col=0 ).rename( columns=lambda c: c.strip() )
with open( 'yes_sl.txt' ) as file:
	yesdb = pandas.read_csv( file, sep='\t', skiprows=7, index_col=0 ).rename( columns=lambda c: c.strip() )

props = { aa: pr
	for aa, pr in zip(
	list( 'RHKDESTNQGAVILMFYWPC' ),
	list( '+++--pppphhhhhbbbWPC' ),
	) }


def getpattern( muscle ):
	amax = max( sum( row ) for ind, row in muscle.iterrows() )
	for ind, row in muscle.iterrows():
		xmax = row.idxmax()
		vmax = row[ xmax ] if pandas.notna( xmax ) else 0
		yield xmax if vmax == amax else '-'


nonp = list( getpattern( nondb.drop( nondb.columns[ -4: ], axis=1 ) ) )
yesp = list( getpattern( yesdb.drop( yesdb.columns[ -4: ], axis=1 ) ) )
diff = ''.join( '=' if y == n or y != '-' else n for y, n in zip( yesp, nonp ) )


def cprint( l, m=7 ):
	s = 0
	for x in sliding_window( l, m ):
		if sum( c != '=' for c in x ) > 2: s = m
		if s:
			print( '\x1b[33m', end='' )
			s -= 1
		print( x[ 0 ], end='\x1b[0m' )


cprint( diff )
