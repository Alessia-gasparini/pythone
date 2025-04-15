import math
class SodaCan :
    def _init_(self, altezza, raggio) : #costruttore
        self._altezza = altezza 
        self._raggio = raggio
        def getSurfaceArea(self) :
            circonferenza = 2 * math.pi * self._raggio
            laterale = self._alzetta * circonferenza
            area_base = math.pi * self._raggio ** 2
            return laterale + 2 * area_base
        def getVolume(self) :
            area_base = math.pi * self._raggio ** 2
            return self._altezza * area_base

       
mini_lattina = SodaCan (8, 2)
lattina = SodaCan (9.24, 3.37)

print(mini_lattina.getSurfaceArea())
print(lattina.getSurfaceArea())
print(mini_lattina.getVolume())
print(lattina.getVolume())