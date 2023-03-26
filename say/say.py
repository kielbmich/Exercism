num2words = {1: 'one', 2: 'two', 3: 'Three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'Eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
            90: 'ninety', 0: 'zero'}
def say(number):
    if number in num2words:
        return  num2words[number]
    if number > 999999999999:
        raise ValueError("Out of range")
    number = str(number)
    number = number.rjust(3 * (len(number) // 3 + 1) if len(number) % 3 != 0 else 0)
    numberSplit = [number[i:i+3] for i in range(0, len(number), 3)]
    order = ["hundred", "thousand", "million", "billion"][0:len(numberSplit)]
    for index, item in enumerate(numberSplit):
        print(num2words[int(item[0])], order[index], )
say(100)