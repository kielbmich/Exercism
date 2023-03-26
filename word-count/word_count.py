import re
def count_words(sentence):
    dictionary = dict()
    sentence_clean = re.findall(r"[a-z\d]+'[a-z]+|[a-z\d]+", sentence.lower())    
    for item in sentence_clean:
        dictionary[item] = dictionary.setdefault(str(item), 0) + 1
    return dictionary