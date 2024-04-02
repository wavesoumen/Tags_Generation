text = """ Artificial intelligence (AI) is the science of creating machines that can think like humans. AI technology can process large amounts of data in ways that are different from humans. The goal of AI is to be able to do things like recognize patterns, make decisions, and judge like humans"""

BAD_CHARS = ".!?,\'\""

words = [ word.strip(BAD_CHARS) for word in text.strip().split() if len(word) > 4 ]

word_freq = {}

# generate a 'word histogram' for the text--ie, a list of the frequencies of each word
for word in words :
  word_freq[word] = word_freq.get(word, 0) + 1

# sort the word list by frequency
tx = [ (v, k) for (k, v) in word_freq.items()]
tx.sort(reverse=True)
word_freq_sorted = [ (k, v) for (v, k) in tx ]

#the most common words in that text
print(word_freq_sorted)

# term_importance = lambda word : 1.0/word_freq[word]

# # select document keywords from the words at/near the top of this list:
# map(term_importance, word_freq.keys())