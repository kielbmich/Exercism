bottles = [
    "{} green {} hanging on the wall,", 
    "And if one green bottle should accidentally fall,", 
    "There'll be {} green {} hanging on the wall."
    ]

num2words = {
    0: ("No", "bottles"), 1: ("One", "bottle"), 2: ("Two", "bottles"), 
    3: ("Three", "bottles"), 4: ("Four", "bottles"), 5: ("Five", "bottles"), 
    6: ("Six", "bottles"), 7: ("Seven", "bottles"), 8: ("Eight", "bottles"), 
    9: ("Nine", "bottles"), 10: ("Ten", "bottles")
    }

def recite(start, take = 1):
    out = []
    for i in range(take):
        out.append(bottles[0].format(num2words.get(start - i)[0], num2words.get(start - i)[1]))
        out.append(bottles[0].format(num2words.get(start - i)[0], num2words.get(start - i)[1]))
        out.append(bottles[1])
        out.append(bottles[2].format(num2words.get(start - i - 1)[0].lower(), num2words.get(start - i - 1)[1].lower()))
        out.append("") if i != take - 1 else 0
    return(out)