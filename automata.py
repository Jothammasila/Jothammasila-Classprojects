class Automata:

    def __init__(self):
        global Set
        Set =set()
        self.Alphabet = str(input("Enter Alphabet Σ : "))
        for s in self.Alphabet:
            Set.add(s)
        print(f"The Alphabet is :{Set}")


    def lang1(self):
        self.ask1 = True
        self.accepted1 = False

        print("------------------------------------------------------------------------------")
        print("L1 = {set of all strings ending with same character e.g 'aa','11','00' etc.}")
        print("------------------------------------------------------------------------------")
        while self.ask1:
            self.string = str(input("Enter a string in L1: "))
            try:
                for c in self.string:
                    if c in Set and self.string[-1]==self.string[-2]:
                        self.accepted1 = True
                        break
                    else:
                        self.accepted1 = False
            except IndexError:
                print("Srings must have a minimum length of 2 characters.")

            if self.accepted1:
                print(f"String1 '{self.string}' Accepted")
            else:
                print(f"String1 '{self.string}' Rejected")
            
            if self.string =="Q".lower():
                self.ask1 = False

    def lang2(self):
        self.ask2 = True
        self.accepted2 = False
        print("-------------------------------------------------------------------------------")
        print("L2 = {set of all strings ending with in form of 'aba','bab',010,101; i.e a character sandwiched between two same characters}")
        print("------------------------------------------------------------------------------")

        while self.ask2:
            self.string = str(input("Enter a string in L2: "))
            try:
                for c in self.string:
                    if c in Set and self.string[-1]==self.string[-3] and self.string[-1] != self.string[-2]:
                        self.accepted2 = True
                        break
                    else:
                        self.accepted2 = False
            
            except IndexError:
                print("Srings must have a minimum length of 3 characters.")
            
            if self.accepted2:
                print(f"String2 '{self.string}' Accepted")
            else:
                print(f"String2 '{self.string}' Rejected")

            if self.string == "Q".lower():
                self.ask2 = False



if __name__ =="__main__":
    dfa = Automata()
    dfa.lang1()
    dfa.lang2()
