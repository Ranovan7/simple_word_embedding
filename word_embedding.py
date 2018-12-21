

def WordEmbedding(data, labels, separator=" "):
    '''
    Word Embedding which recieve a list of texts and its labels
    params:
    - list of the texts
    - list of the labels
    - separator to separate the token
    return : list of frequency of each words in each texts (i'll be back if i have clearer explanation)
    '''
    label_count = len(set(labels))
    frequency = []
    # Catch the frequency of each words per label
    for i in range(label_count):
        frequency.append({
            'freq': {},
            'count': 0
        })
    for i, text in enumerate(data):
        tokens = text.split(separator)
        for token in tokens:
            if token not in frequency[labels[i]]['freq']:
                frequency[labels[i]]['freq'][token] = 1
                frequency[labels[i]]['count'] += 1
            else:
                frequency[labels[i]]['freq'][token] += 1
                frequency[labels[i]]['count'] += 1
    for freq in frequency:
        for token in freq['freq']:
            freq['freq'][token] = round(freq['freq'][token] / freq['count'], 7)

    # turn it into better format for the result
    result = []
    for i, text in enumerate(data):
        text_ins = []
        tokens = text.split(separator)
        for token in tokens:
            word_ins = {token: []}
            for freq in frequency:
                if token in freq['freq']:
                    word_ins[token].append(freq['freq'][token])
                else:
                    word_ins[token].append(0)
            text_ins.append(word_ins)
        result.append(text_ins)
    return result
