import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


subgenre_index = {'prebop': 0, 
		'bossanova': 1,
		'bop': 2,
		'baroque': 3,
		'classical': 4,
		'romanticism': 5,
		'pop': 6,
		'blues': 7,
		'celtic': 8 }

rev_subgenre = ['prebop', 'bossanova', 'bop', 'baroque', 'classical', 'romanticism', 'pop', 'blues', 'celtic']
rev_genre = ['jazz', 'academic', 'pop']

NUMTOPICS = 6
NUMGENRES = 9

def GetSongNames(songfile):
	songnames = []
	with open(songfile, 'r') as f:
		for line in f.readlines():
			songnames.append(line.strip('\n'))
	return songnames

def GetGammas(gammafile):
	gammas = []
	with open(gammafile, 'r') as f:
		for line in f.readlines():
			gvals = line.strip('\n').split(' ')
			onedoc = []
			for g in gvals:
				onedoc.append(float(g))
			gammas.append(onedoc)
	return gammas

def FillSubGenreLists(songfile, gammafile):
	genrelists = [[] for _ in range(NUMGENRES)]
	sn = GetSongNames(songfile)
	ga = GetGammas(gammafile)
	for i in range(len(sn)):
		fields = sn[i].split('/')
		#subgenre = fields[1] 
		#songname = fields[2].strip('.chords') 
		subgenre = fields[0] 	#working around Rebecca's weird error??
		songname = fields[1]	#working around Rebecca's weird error??
		index = subgenre_index[subgenre]
		genrelists[index].append((songname, ga[i])) # append the pair of song name and corresponding gamma value
	return genrelists

def GenreTopicAvs(songfile, gammafile):
	"""
	Obtains distribution over topics for
	each subgenre by summing the topic weights
	for each document in that subgenre.
	Future work would include looking for
	outliers, which could be points of interest.
	"""
	subgenres = FillSubGenreLists(songfile, gammafile)
	topic_avs = [[0.0 for _ in range(NUMTOPICS)] for i in range(NUMGENRES)] # list of lists
	for i in range(NUMGENRES):
		sg = subgenres[i]
		ta = topic_avs[i]
		for song, topicdist in sg:
			for j in range(NUMTOPICS):
				ta[j] += topicdist[j]
	SaveTopicAvs(topic_avs)
	for i in range(3):
		PlotOneTopic(topic_avs, i)

def SaveTopicAvs(topic_avs):
	with open('TopicAvs.txt', 'w') as f:
		for t in topic_avs:
			outstr = ''
			for i in t:
				outstr += str(i)+' '
			outstr.strip(' ')
			f.write(outstr+'\n')

def PlotOneTopic(topic_avs, genre):
	"""
	Normalizes all the topic scores for 3 subgenres and
	plots them, one on top of another,
	for a given genre.
	"""
	i = genre*3

	overall_av = []
	for j in range(3):
		Normalize(topic_avs[i+j])
	for j in range(NUMTOPICS):
		overall_av.append(topic_avs[i][j]+topic_avs[i+1][j]+topic_avs[i+2][j])
	Normalize(overall_av)
	xvals = np.arange(NUMTOPICS)
	p1, = plt.plot(xvals, overall_av, 'r-')
	p2, = plt.plot(xvals, topic_avs[i], 'y-')
	p3, = plt.plot(xvals, topic_avs[i+1], 'b-')
	p4, = plt.plot(xvals, topic_avs[i+2], 'g-')
	plt.legend([p1, p2, p3, p4], [rev_genre[genre], rev_subgenre[i], rev_subgenre[i+1], rev_subgenre[i+2]], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.show()

def AddElementWise(l1, l2):
	lnew = []
	for i in range(len(l1)):
		lnew.append(l1[i]+l2[i])
	return lnew

def Normalize(topic_av):
	summed = sum(topic_av)
	for i in range(len(topic_av)):
		topic_av[i] = topic_av[i]/summed

if __name__ == '__main__':
	GenreTopicAvs('MapToFilenames.txt', 'name-gamma.dat')