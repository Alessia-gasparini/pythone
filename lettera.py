class Letter :
    def __init__(self, letterFrom, letterTo):
        self._letterFrom = letterFrom
        self._letterTo = letterTo
        self._line = ""
    
    def addLine(self, line):
        self._line += line + "\n"

    def getText(self):
        LetterText = f"Dear" (self._letterTo)
        for line in self._line :
            LetterText += line
        LetterText += "\n Sincerely, \n\n" + LetterFrom

    missiva = Letter("Mary", "John")
    missiva.addLine("I'm sorry we must part.")
    missiva.addLine("I wish you all the best.")
    print(missiva.getText())