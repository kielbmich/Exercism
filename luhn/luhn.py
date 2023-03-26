class Luhn:
    def __init__(self, num):
        self.card_num = num
        self.valid_num = self.valid()

    def valid(self):
        out = list()
        if not all(i.isnumeric() or i == " " for i in self.card_num):
            return False
        clean = [int(digit) for digit in self.card_num if digit.isnumeric()]
        if len(clean) < 2:
            return False
        clean_single = clean[::-1][0::2]
        clean_double = clean[::-1][1::2]
        for digit in clean_double:
            if digit > 4:
                out.append(2*digit - 9)
            else:
                out.append(2*digit)
        return (sum(int(i) for i in out) + sum(int(i) for i in clean_single)) % 10 == 0
