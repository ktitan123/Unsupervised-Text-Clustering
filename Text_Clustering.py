from random import randint
import itertools
import Word_sim as ws
import Text_Processing as tp

cluster_lookup = {}
inverted_cluster = {}

def randomize(tokens,range = 4):
	for sentence in tokens:
		for word in sentence:
			cluster_lookup[word]=randint(0,1000)%range
	return cluster_lookup


class Cluster():
	newid = itertools.count().next
	def __init__(seed_words=[]):
		self.no_words = len(seed_words)
		self.index = Cluster.newid()
		self.words = seed_words
		for word in self.words:
			if len(word.strip())>1:
				cluster_lookup[word] = self.index
	


Clusters={}
for i in range(1000):
	inverted_cluster[i] = []
	Clusters[i] = 0

Text = "I have a cat. I also have a dog. My cat has four legs. My dog also has four legs. I love playing with my cat and my dog. I also feed them regularly. My cat likes to eat fish and drink milk. My dog usually eats meat. My cat also eats meat sometimes but prefers fish.Both my cat and my dog are my pets. My cat is three years old and my dog is four years old. I like drinking milk as well. I also take my dog out for walks in the park."
Text += "My name is Ann Smith. I am a senior in high school. Everyone can agree that I am a good student and that I like to study. My favorite subjects are chemistry and biology. I am going to enter the university because my goal is to study these subjects in future and to become a respected professional in one of the fields.I can say that I am a responsible and a hard-working student. Moreover, being a sociable person, I have many friends since I like to communicate with people and get to know new interesting individuals. I enjoy my time at school: it is really nice to study and the students are very friendly and ready to help. The atmosphere cannot but make me want to go there every time. I like to receive and deal with challenging tasks. I am a very enthusiastic student and I think this is a strong point of mine." 

Text += " I have a cat. I have a dog. I have a cow. I have a horse. My cat eats fish. My dog eats meat. My cow eats grass. My horse eats hay.  "
Text = "Cow gives milk.Cat drinks milk.Humans drink milk.Shops sell milk."
tokens = tp.get_words(Text)
cluster_lookup = randomize(tokens,15)

for key in cluster_lookup:
	Clusters[ cluster_lookup[key] ] +=1

iteration = 0
no_clusters = 15
epoch = 0
empty_clusters = [1,2,3,4,5]


for epoch in range(1):
	epoch+=1
	for iteration in range(2000):
		iteration+=1
		for sentence in tokens:
			for word in sentence:
				if len(word.strip())>1:
					cluster_no = ws.word_sim(cluster_lookup[word],word,tokens,cluster_lookup,no_clusters)
					Clusters[cluster_lookup[word]]-=1
					Clusters[cluster_no]+=1
					cluster_lookup[word] = cluster_no



for key in cluster_lookup:
	inverted_cluster[ cluster_lookup[key] ].append(key)

for key in inverted_cluster:
	if len(inverted_cluster[key]) > 0:
		print key,"\n"
		print inverted_cluster[key],"\n\n"





