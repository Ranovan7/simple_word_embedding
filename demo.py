from word_embedding import WordEmbedding
import json
import re
import random

# load data
filedata = "random_quotes.json"
data = json.load(open(filedata))

texts = []
labels = []

# preprocess or clean the data
for i in data:
    text = i['quote']
    text = re.sub(r"[']", '', text) # remove aphostrope and join the chars into the word
    text = re.sub(r'[^\w]', ' ', text) # change all non alpha-numeric char into spaces
    text = re.sub(r" +", ' ', text) # remove the duplicate spaces
    text = text.rstrip() # remove space at the end of string
    texts.append(text)
    labels.append(random.randrange(4))

# do the embedding and print some of the result
embedded = WordEmbedding(texts, labels)
for result in embedded[100:101]:
    for token in result:
        for i in token:
            print(f"{i} : {token[i]}")
    print()
