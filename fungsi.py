

def processRunge(growthFunc, *args):
    # Fungsi runge kutta 4
    # IF : growthFunc   -> fungsi pertumbuhan
    #      args         -> h        -> Delta Time
    #                      x0       -> Waktu yg terus bertambah (ditambah delta time)
    #                      populasi -> Populasi pada waktu sebelumnya
    #                      lisData  -> Tuple untuk passing data fluxes ke fungsi pertumbuhan
    # FS : Populasi pada waktu x

    h, x0, populasi, listData = args

    k1 = h * growthFunc(x0,populasi,listData)
    k2 = h * growthFunc(x0 + 0.5 * h, populasi + 0.5 * k1,listData)
    k3 = h * growthFunc(x0 + 0.5 * h, populasi + 0.5 * k2,listData)
    k4 = h * growthFunc(x0 + h, populasi + k3,listData)
    
    return populasi + ((k1 + 2 * k2 + 2 * k3 + k4) / 6.0 )


def growthAtmospherePools(waktu,populasi, *args):
    # Fungsi Pertumbuhan Atmosphere
    terrestrialphotosynthesis,marinephotosynthesis,terrestrialrespiration,marinerespiration,carbondissolving,evaporation,upwelling,downwelling,marinedeath,plantdeath,plantdecay = args[0]

    return (((evaporation + marinerespiration + plantdecay + terrestrialrespiration)-(terrestrialphotosynthesis + marinephotosynthesis + carbondissolving))*waktu)


def growthSoilPools(waktu, populasi, *args):
    # Fungsi Pertumbuhan MixedLayer
    terrestrialphotosynthesis,marinephotosynthesis,terrestrialrespiration,marinerespiration,carbondissolving,evaporation,upwelling,downwelling,marinedeath,plantdeath,plantdecay = args[0]
    return ((plantdecay - plantdecay)*waktu)

def growthOceanSurfacePools(waktu, populasi, *args):
    # Fungsi Pertumbuhan MixedLayer
    terrestrialphotosynthesis,marinephotosynthesis,terrestrialrespiration,marinerespiration,carbondissolving,evaporation,upwelling,downwelling,marinedeath,plantdeath,plantdecay = args[0]
    return (((upwelling + marinephotosynthesis + carbondissolving) - (downwelling + evaporation + marinerespiration + marinedeath))*waktu)

def growthTerestriallBiospherePools(waktu, populasi, *args):
    # Fungsi Pertumbuhan MixedLayer
    terrestrialphotosynthesis,marinephotosynthesis,terrestrialrespiration,marinerespiration,carbondissolving,evaporation,upwelling,downwelling,marinedeath,plantdeath,plantdecay = args[0]
    return (((terrestrialphotosynthesis)-(terrestrialrespiration + plantdeath))*waktu)

def growthDeepOceanPools(waktu, populasi, *args):
    # Fungsi Pertumbuhan MixedLayer
    terrestrialphotosynthesis,marinephotosynthesis,terrestrialrespiration,marinerespiration,carbondissolving,evaporation,upwelling,downwelling,marinedeath,plantdeath,plantdecay = args[0]
    return (((downwelling + marinedeath)-(upwelling))*waktu)



def outputTable(time,listAtmosphere,listSoil, listOceanSurface, listTerestriallBieophere, listDeepOcean):
    # Outputkan nilai populasi pada setiap iterasi
    from tabulate import tabulate
    results=[]
    for i in range(0,len(time)):
        results.append((time[i], listAtmosphere[i], listSoil[i], listOceanSurface[i], listTerestriallBieophere[i], listDeepOcean[i]))

    print(tabulate(results,headers=["Time","Atmosphere","Soil","OceanSurface","TerestriallBieophere", "Deep Ocean"],tablefmt="fancy_grid"))