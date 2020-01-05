class SimulationConfig:
    x0 = 0.0 		# Waktu awal
    x  = 1.0 		# Waktu Selesai (Sampai ke perulangan ke berapa)
    h  = 0.01 		# Delta time

    def getConfig(self):
        return (
            self.x0,
            self.x,
            self.h,
        )

class Carboncycle:
    # Reservoir
    atmosphere = 750
    terrestrialbiosphere = 600
    oceansurface = 800
    deepocean = 38000
    soil = 1500

    # Fluxes
    terrestrialphotosynthesis = 110
    marinephotosynthesis = 40
    terrestrialrespiration = 55
    marinerespiration=40
    carbondissolving = 100
    evaporation = 100
    upwelling = 27
    downwelling = 23
    marinedeath = 4
    plantdeath = 55
    plantdecay = 55



    def __init__(self): 
        self.sumFluxes = self.terrestrialphotosynthesis+self.marinephotosynthesis+self.terrestrialrespiration+self.marinerespiration+self.carbondissolving+self.evaporation+self.upwelling+self.downwelling+self.marinedeath+self.plantdeath+self.plantdecay
        self.terrestrialphotosynthesisprec = self.terrestrialphotosynthesis/self.sumFluxes
        self.marinephotosynthesisprec      = self.marinephotosynthesis/self.sumFluxes
        self.terrestrialrespirationprec         = self.terrestrialrespiration/self.sumFluxes
        self.marinerespirationprec     = self.marinerespiration/self.sumFluxes
        self.carbondissolvingprec      = self.carbondissolving/self.sumFluxes
        self.evaporationprec      = self.evaporation/self.sumFluxes
        self.upwellingprec      = self.upwelling/self.sumFluxes
        self.downwellingprec      = self.downwelling/self.sumFluxes
        self.marinedeathprec      = self.marinedeath/self.sumFluxes
        self.plantdeathprec      = self.plantdeath/self.sumFluxes
        self.plantdecayprec      = self.plantdecay/self.sumFluxes

    def updateFluxes(self,population):
        a = round( self.sumFluxes  *  (population /(self.soil + self.oceansurface + self.terrestrialbiosphere + self.deepocean)) , 3)
        return (
            a*self.terrestrialphotosynthesis,
            a*self.marinephotosynthesis,
            a*self.terrestrialrespiration,
            a*self.marinerespiration,
            a*self.carbondissolving,
            a*self.evaporation,
            a*self.upwelling,
            a*self.downwelling,
            a*self.marinedeath,
            a*self.plantdeath,
            a*self.plantdecay
        )

    def getPools(self):
        return (self.atmosphere,self.soil,self.oceansurface,self.terrestrialbiosphere,self.deepocean)

    def getFluxes(self):
        return (
            self.terrestrialphotosynthesis,
            self.marinephotosynthesis,
            self.terrestrialrespiration,
            self.marinerespiration,
            self.carbondissolving,
            self.evaporation,
            self.upwelling,
            self.downwelling,
            self.marinedeath,
            self.plantdeath,
            self.plantdecay
        )


