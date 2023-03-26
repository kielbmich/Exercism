import re
import collections
def count_words(sentence):
    sentence_clean = re.findall(r"[a-z\d]+(?:'[a-z]+)?", sentence.lower())
    return collections.Counter(sentence_clean)