ALLERGIES = ['eggs', 'peanuts', 'shellfish', 'strawberries',
             'tomatoes', 'chocolate', 'pollen', 'cats']

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        if (self.score & 1 << ALLERGIES.index(item)) != 0:
            return True
        return False

    @property
    def lst(self):
        return [item for item in ALLERGIES if self.allergic_to(item)]