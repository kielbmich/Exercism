bands = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, 
    "yellow": 4, "green": 5, "blue": 6, "violet": 7,
    "grey": 8, 'white': 9
    }

def label(colors):
    ohms = "{}{}{}".format(bands.get(colors[0]), bands.get(colors[1]), "0"*(bands.get(colors[2])))
    return ohms + " ohms" if int(ohms) < 1000 else ohms[:-3] + " kiloohms"