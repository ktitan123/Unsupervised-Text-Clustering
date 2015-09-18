import math

stop_words = ['I','the','and','a','an','have','has','my',
'his','hers','theirs','their','our','your','am','and','or','it','this','that',
'is','also','next','','mine','want','to','very','of','may','can','should','could'
]

def word_sim(old_index,word,tokens,cluster_lookup,no_clusters):
	sum = 0.0
	den = 0.00001
	index = 0
	contribution = {}
	for index in range(no_clusters):
		contribution[index]=0.000
		index+=1

	if word in stop_words:
		return old_index

	for sentence in tokens:
		sentence_sum = 0
		sentence_den = 0
		for token in sentence:
			index+=1
			if token==word:
				for pos in range(len(sentence)):
					candidate = sentence[pos]
					if candidate in cluster_lookup:
						gradient = abs(pos-index)
						index = cluster_lookup[candidate]
						contribution[index]+=(1/(gradient+0.001))
		

	
	return max(contribution, key=contribution.get)
	





