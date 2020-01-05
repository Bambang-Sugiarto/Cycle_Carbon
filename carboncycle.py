import matplotlib.pyplot as plt
from fungsi import *
from data import *

# _____________________________[ Mercury Cycle ] __________________________
# ______________________________ Initialization ___________________________

# ___________________ PreIndustri ____________________
PI = Carboncycle()
# Pools
atmosphere,soil,oceansurface,terrestrialbiosphere,deepocean = PI.getPools()
# Fluxes
carbonCycleFluxesData = PI.getFluxes()

# _________________ Simulation settings _______________
Config   = SimulationConfig()
x0, x, h = Config.getConfig()

# ___________________ List for output _________________
listAtmospherePopulation = []
listSoilPopulation = []
listOceanSurface = []
listTerrestrialBiosphere = []
listDeepOcean = []
listTime = []

# ________________________________ Process _________________________________

# Tambahkan populasi awal
listAtmospherePopulation.append(atmosphere)
listSoilPopulation.append(soil)
listOceanSurface.append(oceansurface)
listTerrestrialBiosphere.append(terrestrialbiosphere)
listDeepOcean.append(deepocean)
listTime.append(x0)
x0 += h 

n = (int)((x - x0)/h) + 1

for i in range(0,n): # perulangan per 0.01 year
    # soil
    soil = processRunge(growthSoilPools,h,x0,soil,carbonCycleFluxesData)
    listSoilPopulation.append(soil)
    # deep ocean
    deepocean = processRunge(growthDeepOceanPools,h,x0,soil,carbonCycleFluxesData)
    listDeepOcean.append(deepocean)

    #ocean surface
    oceansurface = processRunge(growthOceanSurfacePools, h, x0, oceansurface, carbonCycleFluxesData)
    listOceanSurface.append(oceansurface)

    #terestrial biosphere
    terrestrialbiosphere = processRunge(growthTerestriallBiospherePools, h, x0, terrestrialbiosphere, carbonCycleFluxesData)
    listTerrestrialBiosphere.append(terrestrialbiosphere)

    # Atmosphere
    atmosphere = processRunge(growthAtmospherePools,h,x0,atmosphere,carbonCycleFluxesData)
    listAtmospherePopulation.append(atmosphere)

    # Update Fluxes Rate
    carbonCycleFluxesData = PI.updateFluxes(soil)

    # Time List
    listTime.append(x0)

    # update x0 dgn delta 
    x0 += h 

#  ________________________________ Output _________________________________

# Jika ingin lihat nilai populasi dari setiap iterasi
outputTable(listTime,listAtmospherePopulation,listSoilPopulation,listOceanSurface,listTerrestrialBiosphere,listDeepOcean)

# Draw point based on above x, y axis values.
plt.plot(listTime,listAtmospherePopulation)
plt.plot(listTime,listSoilPopulation)
plt.plot(listTime,listOceanSurface)
plt.plot(listTime,listTerrestrialBiosphere)
plt.plot(listTime,listDeepOcean)

plt.legend(["Atmosphere","Soil","Ocean Surface","Terestrial Biosphere","Deep Ocean"], loc='upper right')

# Set chart title.
plt.title("Reservoir versus Time")

# Set x, y label text.
plt.xlabel("Time")
plt.ylabel("Reservoir")
plt.show()