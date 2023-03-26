class PhoneNumber:
    def __init__(self, phoneNumber):
        self.number = self.cleanNumber(phoneNumber)
        self.area_code = self.number[0:3]

    def cleanNumber(self, phoneNumber):
        out = ""
        for i in phoneNumber:
            if i.isnumeric():
                out += i
            elif i.isalpha():
                raise ValueError("letters not permitted")
            elif i in ",!@":
                raise ValueError("punctuations not permitted") 
        return out

    def validate(self, phoneNumber):
        out = self.cleanNumber(phoneNumber)
        if len(out) == 10 and out[0] == "0" or len(out) == 11 and out[1] == "0":
            raise ValueError("area code cannot start with zero")
        if len(out) == 10 and out[0] == "1" or len(out) == 11 and out[1] == "1":
            raise ValueError("area code cannot start with one")
        if len(out) == 10 and out[3] == "0" or len(out) == 11 and out[4] == "0":
            raise ValueError("exchange code cannot start with zero")
        if len(out) == 10 and out[3] == "1" or len(out) == 11 and out[4] == "1":
            raise ValueError("exchange code cannot start with one")
        if len(out) < 10:
            raise ValueError("incorrect number of digits")
        if len(out) > 11:
            raise ValueError("more than 11 digits")
        if len(out) == 11 and out[0] != "1":
            raise ValueError("11 digits must start with 1")
        return out if len(out) == 10 else out[1:]

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"