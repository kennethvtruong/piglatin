class Pig_latin2:
    def __init__(self, the_str: str, pig_str: str):
        self.the_str = the_str
        self.pig_str = pig_str

    def get_str(self):
        self.the_str = input("What word did you want to translate to PigLatin?").strip().split()

    def change_str(self):
        self.pig_str = ""
        for item in self.the_str:
            if item.isalpha():
                self.pig_str += (item[1:len(item)] + item[0] + 'ay' + ' ')
            else:
                self.pig_str += (item + ' ')
        print(self.pig_str)


my_pig_latin = Pig_latin2("", "")
my_pig_latin.get_str()
my_pig_latin.change_str()
