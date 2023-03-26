dict = {
    1:("","horse and the hound and the horn"),
    2:("belonged to the", "farmer sowing his corn"),
    3:("kept the", "rooster that crowed in the morn"),
    4:("woke the", "priest all shaven and shorn"),
    5:("married the", "man all tattered and torn"),
    6:("kissed the", "maiden all forlorn"),
    7:("milked the", "cow with the crumpled horn"),
    8:("tossed the", "dog"),
    9:("worried the", "cat"),
    10:("killed the", "rat"),
    11:("ate the", "malt"),
    12:("lay in the", "house that Jack built.")    
    }

def recite(start_verse, end_verse):
    out = list()
    for rows in range(start_verse, end_verse + 1):
        current_sentence = str()
        for sentence_part in range(1, rows + 1):
            if sentence_part == rows:
                current_sentence = f"This is the {dict.get(12 - rows + 1)[1]} " + current_sentence
            else:
                current_sentence = f"that {dict.get(12 - sentence_part + 1)[0]} {dict.get(12 - sentence_part + 1)[1]} " + current_sentence
        out.append(current_sentence.rstrip())
    return out