import subprocess
from random import shuffle

NUMTOPICS = 6
ALL_SONGS = 'all_songs.txt'

def ReadSongs(songfile):
	songlist = []
	with open(songfile, 'r') as f:
		for line in f.readlines():
			songlist.append(line)
	return songlist

def MakeTrainTest(songlist):
	"""
	Shuffles songlist,
	returns list of five sections.
	"""
	shuffle(songlist)
	listlen = len(songlist)
	split = listlen/5
	return [songlist[0:split], songlist[split:2*split], songlist[2*split:3*split], songlist[3*split:4*split], songlist[4*split:]]	

def GetTrain(heldout, splits):
	train = []
	for i in range(5):
		if i!=heldout:
			train += splits[i]
	return train

def ReadLikelihood(lfile):
	logpr = 0.0
	with open(lfile, 'r') as f:
		for line in f.readlines():
			logpr += float(line.strip('\n'))
	return logpr

def CrossValidate():
	songlist = ReadSongs(ALL_SONGS)
	splits = MakeTrainTest(songlist)
	likelihoods = []
	with open('likelihood'+str(NUMTOPICS)+'.txt', 'w') as outfile:
		for i in range(5):
			print "Holding out fold {0}".format(i)
			heldout = splits[i]
			train = GetTrain(i, splits)
			with open('LDAformatted.txt', 'w') as f:
				for l in train:
					f.write(l)
			with open('testfile.txt', 'w') as f:
				for h in heldout:
					f.write(h)
			subprocess.call('./lda est 0.03 '+str(NUMTOPICS)+' settings.txt LDAformatted.txt random Output', shell=1)
			subprocess.call('./lda inf settings.txt Output/final testfile.txt results', shell=1)
			likelihood = ReadLikelihood('results-lda-lhood.dat')
			print likelihood
			outfile.write(str(likelihood)+',')

if __name__ == '__main__':
	"""
	Before running this, run FormatForLDAngram.py to get the LDAformatted.txt file
	for your chosen n-gram length.

	python FormatForLDAngram.py [path to chords] [n gram]

	then:

	mv LDAformatted.txt all_songs.txt

	"""
	CrossValidate()

