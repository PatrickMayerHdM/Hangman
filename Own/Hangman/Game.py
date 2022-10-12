from backend import letter_in_word_check
from backend import word_generator
import re


class Hangman:
    letter = ""

    def __init__(self, test):
        self.__test = test
        self.len_test = len(test)
        self.show_word = self.len_test * "*"
        self.my_sting = ""
        self.count = 0


    def game(self):
        self.show_word = list(self.show_word) # Mache show_word zu einer Liste
        print("Das Wort:", self.show_word)

        while self.my_sting != self.__test: # Testen ob der Spieler schon gewonnen hat und ausführen des Spiels wenn nicht
            if self.count < 12:
                self.letter = input("Buchstabe:") # Input, wo der Spieler einen Buchstaben eingeben muss
                self.letter = self.letter.upper() # Macht es zu einem Großbuchstaben
                self.replacer() # Ausführen der replacer Funktion
                print(f"Anzahl Fehlversuche: {self.count}")
            else:
                print("Du hast verloren")
                break





    def replacer(self):
        if letter_in_word_check(self.letter,self.__test) is True: # Testen ob der Buchstabe enthalten ist
            index_of_letter = [m.start() for m in re.finditer(self.letter, self.__test)]
            """Erstellen einer Liste mit den 
            Indexen der Buchstaben (kann den Buchstaben öfters enthalten)"""
            #print("Der Index ist:", index_of_letter) # Ausgeben der Indexe zur Überprüfung
            len_index = len(index_of_letter) # Wie oft kommt der Buchstabe vor?
            #print("Der Buchstabe kommt", len_index, "mal vor")
            self.letter = self.letter * len_index # Erhöht die Anzahl an Buchstaben, jenachdem wie viele im Wort vorhanden sind
            #print(self.letter)
            for (index, replacement) in zip(index_of_letter, self.letter):
                self.show_word[index] = replacement

                """Ersetzt die """

            self.my_sting = "".join(map(str, self.show_word)) # Erstelle den String aus der Liste Show_Word
            print(f"Das Wort sieht jetzt so aus: {self.my_sting}")
        else:   # Aktionen wenn der Buchstabe nicht in dem Wort ist
            print("Der Buchstabe kommt nicht vor")
            self.count += 1


h = Hangman(word_generator())
print(h.game())