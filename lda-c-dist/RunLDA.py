import subprocess
import sys

"""
Before running this code, cd to lda-c-dist directory. 
FormatForLDAngram.py should be in this directory.

Usage: python RunLDA.py [number of topics] [path to chords directory] [output directory]

If you just want to run LDA again, write 'run' for the [path to chords directory]
"""

ALPHA = '0.05'
NGRAM = '3'

Num_Topics = sys.argv[1]
PathToChords = sys.argv[2]
OutputDir = sys.argv[3]

if PathToChords!='run':
	subprocess.call('python FormatForLDAngram.py '+PathToChords+' '+NGRAM, shell=1)

subprocess.call('./lda est '+ALPHA+' '+Num_Topics+' settings.txt LDAformatted.txt random '+OutputDir, shell=1)
subprocess.call('./lda inf settings.txt '+OutputDir+'/final LDAformatted.txt name', shell=1)



