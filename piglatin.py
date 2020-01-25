class Pig_latin:
    def __init__(self, get_str: str, pig_str: str):
        self.get_str = get_str
        self.pig_str = pig_str

    def check_str(self):
        self.get_str = input("What word did you want to translate to PigLatin?")
        if len(self.get_str) > 0 and self.get_str.isalpha():
            print("Untranslated:" + self.get_str)
        else:
            print("There is nothing to translate, try again.")
            my_pig_latin.check_str()

    def change_str(self):
        pig = "ay"
        first_letter = self.get_str[0]
        cut_word = self.get_str[1:len(self.get_str)]
        self.pig_str = cut_word + first_letter + pig
        print("Translated:" + self.pig_str)


my_pig_latin = Pig_latin("", "")
my_pig_latin.check_str()
my_pig_latin.change_str()
