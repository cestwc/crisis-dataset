import os
import csv
from collections import Counter

from cleaner import TweetCleaner

class CrisisTweetsLoader():
	def __init__(self, clean):
		self.clean = clean
		self.tweets26, self.tweets26_unlabeled, self.truth26 = self.load26()
		self.tweets6, self.tweets6_unlabeled, self.truth6 = self.load6()
		self.tweets8, self.tweets8_unlabeled, self.truth8 = self.load8()

	def __call__(self, name):
		assert name in ['C6', 'C26', 'C8']
		if name == 'C6':
			return self.tweets6, self.tweets6_unlabeled, self.truth6
		elif name == 'C8':
			return self.tweets8, self.tweets8_unlabeled, self.truth8
		else:
			return self.tweets26, self.tweets26_unlabeled, self.truth26
		
	def unlabel(self, tweets_labeled):
		tweets_unlabeled = Counter()
		for v in tweets_labeled.values():
			tweets_unlabeled.update(v)
		return tweets_unlabeled

	def load26(self):
		folder = 'tweets-C26'
		entries = os.listdir(folder)
		tweets_labeled = {}
		for entry in entries:
			if 'Truth' not in entry:
				with open(os.path.join(folder, entry), 'r') as f:
					tweets_labeled[entry.replace('-tweets_labeled.csv', '')] = Counter([self.clean(x[1]) for x in list(csv.reader(f))[1:]])

		tweets_unlabeled = self.unlabel(tweets_labeled)
			
		with open('tweets-C26/crisisTruthC26.csv', 'r', errors='ignore') as f:
			truth = {x[0]:x[1] for x in list(csv.reader(f))[1:]}

		assert set(truth.keys()).issubset(set(tweets_labeled.keys()))

		return tweets_labeled, tweets_unlabeled, truth

	def load6(self):
		folder = 'tweets-C6'
		entries = os.listdir(folder)
		tweets_labeled = {}
		for entry in entries:
			if 'Truth' not in entry:
				with open(os.path.join(folder, entry), 'r') as f:
					tweets_labeled[entry.replace('-ontopic_offtopic.csv', '')] = Counter([self.clean(x[1]) for x in list(csv.reader(f))[1:] if x[2] == 'on-topic'])

		tweets_unlabeled = self.unlabel(tweets_labeled)

		with open('tweets-C6/crisisTruthC6.csv', 'r', errors='ignore') as f:
			truth = {x[0]:x[1] for x in list(csv.reader(f))[1:]}

		assert truth.keys() == tweets_labeled.keys()

		return tweets_labeled, tweets_unlabeled, truth

	def load8(self):
		entry = 'tweets-C8/en-scheme-annotations.TweetOut.csv'
		tweets_labeled = {}
		with open(entry, 'r') as f:
			for x in list(csv.reader(f))[1:]:
				if len(x) != 0:
					if x[0] not in tweets_labeled:
						tweets_labeled[x[0]] = Counter({self.clean(x[2])})
					tweets_labeled[x[0]].update(Counter({self.clean(x[2])}))

		tweets_unlabeled = self.unlabel(tweets_labeled)
		with open('tweets-C8/eventTruth.csv', 'r', errors='ignore') as f:
			truth = {x[0]:x[1] for x in list(csv.reader(f))[1:]}

		assert truth.keys() == tweets_labeled.keys()

		return tweets_labeled, tweets_unlabeled, truth
