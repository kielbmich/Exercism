dict_numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 
        'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 
        90: 'ninety'}

list = ["billion", "million", "thousand", ""]

def nine_nine_nine_and_below(number):
    if len(number) == 3:
        if number.endswith("00"):
            return "{} hundred".format(dict_numbers.get(int(number[0])))
        elif number.endswith("0"):
            return "{} hundred {}".format(dict_numbers.get(int(number[0])), dict_numbers.get(int(number[1:])))
        elif int(number[1:]) > 20:
            return "{} hundred {}-{}".format(dict_numbers.get(int(number[0])), dict_numbers.get(int((number[1]+"0"))), dict_numbers.get(int(number[2:])))
        else:
            return "{} hundred and {}".format(dict_numbers.get(int(number[0])), dict_numbers.get(int(number[1:])))
    else:
        if int(number) in dict_numbers.keys():
            return "{}".format(dict_numbers.get(int(number)))
        else:
            return "{}-{}".format(dict_numbers.get(int(number[0]+"0")), dict_numbers.get(int(number[1])))

def say(number):
    if number not in range(0, 999999999999 + 1):
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    out = ""
    number = str(number).rjust(12, '0')
    number_process = [number[0+i:3+i] for i in range(0, len(number) - 2, 3)]
    for index, item in enumerate(number_process):
        if item.lstrip("0"):
            out += nine_nine_nine_and_below(item.lstrip("0")) + " " + list[index] + " "
    return out.rstrip()
