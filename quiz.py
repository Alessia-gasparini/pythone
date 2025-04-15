class Student:
    def __init__(self, nome, cognome):
        self._nome = nome 
        self._cognome = cognome 
        self._score = 0.0
        self._numeroDiQuiz = 0 #variabile di appoggio 
    def getName(self):
        return f"{self._nome} {self._cognome}"
    def addQuiz(score):
        self._score += score
        self._numeroDiQuiz += 1
    def getTotaleScore(self):
        return self._score
    def getAverageScore(self):
        return self._score / self._numeroDiQuiz
    
mauro = Student ("Mauro", "Bellagamba")
sara = Student ("Sara", "Bianchi")

sara.addQuiz(29)
sara.addQuiz(21)
sara.addQuiz(25)

sara.getAverageScore()