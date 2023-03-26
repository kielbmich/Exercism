def first_letters_consonant(word, vowel):
    i,j = 0,0
    for letter in word:
        if letter not in vowel:
            i += 1
            if word[0:2] == "qu":
                j = 1
            elif word[i:i+2] == "qu":
                j = i
        else:
            break
    return i,j

def translate(text):
    text = text.split()
    vowel = ["a", "e", "i", "o", "u", "y"]
    extra_two = ["xr", "yt"]
    for index, word in enumerate(text):
        if word[0].isalpha():
            k, j = first_letters_consonant(word, vowel)
            if word[0:2] == "ye":
                text[index] = word[1:] + "yay"       
            elif word[0] in vowel or word[:2] in extra_two:
                text[index] += "ay"
            elif j > 0:
                text[index] = word[k+1:] + word[0:k+1] + "ay"               
            elif k > 1 and word[k:k+1] == "y" or k > 0:
                text[index] = word[k:] + word[0:k] + "ay"       
            elif len(word) == 2 and word[1] == "y":
                text[index] = word[1:] + word[0] + "ay"
    return " ".join(text)