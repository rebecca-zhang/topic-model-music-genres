import sys
import os

"""
Given a directory, formats all files in that
directory for usage with Blei's LDA code.
Produces a file 'LDAformatted.txt' and a file
'vocab.txt' which contains the mappings back to
the chord names.


Usage: python FormatForLDAngram.py [path to chords] [ngram length]

"""

def GetAllFilenames(dirpath, exten='chords'):
	all_filenames = []
	for root, dirnames, filenames in os.walk(dirpath):
		for f in filenames:
			ext = f.lower().rsplit(".", 1)[-1]
			if ext==exten:
				all_filenames.append(os.path.join(root, f))
	return all_filenames

# first we need to make the dictionary

def GetWords(filename, n):
	words = []
	wordgrams = []
	with open(infile, 'r') as g:
		words = g.read().strip('\n').strip(' ').split(' ')

	for i in range(len(words)-n+1):
		s = ''
		for j in range(n):
			s = s + words[i+j] + ','
		wordgrams.append(s)

	return wordgrams

# make dictionary
d = {}
files = {}
count = 0
mapping_in = {} # maps index number of word to word
mapping_out = {} # maps word to its index number

"""
path to degrees full 
"""
filenames = GetAllFilenames(sys.argv[1])

for infile in filenames:
	words = GetWords(infile, int(sys.argv[2]))
	files[infile] = words
	for w in words:
		d[w] = 0

for k,v in d.iteritems():
	mapping_in[count] = k
	mapping_out[k] = count 
	count += 1

with open('LDAformatted.txt', 'w') as f:
	with open('MapToFilenames.txt', 'w') as g:
		for fn,words in files.iteritems():
			outfilelist = fn.split('/')
			outfile = '/'.join(outfilelist[3:])
			g.write(outfile+'\n')
			f.write(str(count)+' ')
			for w in words:
				d[w] += 1
			for k,v in d.iteritems():
				f.write(str(mapping_out[k])+':'+str(v)+' ')
				d[k] = 0
			f.write('\n')

with open('vocab.txt', 'w') as f:
	for k,v in mapping_in.iteritems():
		f.write(v+'\n')


