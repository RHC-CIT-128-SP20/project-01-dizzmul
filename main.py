#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
class Map:
    def __init__(self, weight):
        self.weight=weight

mapWeight ={'the labs' : 100, 'reserve' : 80, 'factory' : 50, 'woods' : 50, 'customs' : 40, 'interchange' : 60, 'shoreline' : 40}

bullets127x55 = {1: "AP-20 Slugs", 2: "Flechette rounds", 3: "RIP rounds", 4: "Poleva-6u Slug", 5: "8.5mm Magnum Buckshot"}
bullets545x39 = {1: "7N39 Igolnik", 2: "BS rounds", 3: "BT Rounds", 4: "BP Rounds"}
bullets556x45 = {1: "M995 Rounds", 2:"M855A1 Rounds", 3: "M856A1 Rounds"}

guns127x55 = ("ash-12", "null")
guns545x39 = ("ak-105", "ak-74", "ak-74m", "ak-74n", "aks-74", "aks-74n", "aks-74u", "aks-74ub", "aks-74un", "rpk-16")
guns556x45 = ("adar 2-15", "ak-101", "ak-102", "dt mdr", "hk 416a5", "m4a1", "tx-15 dml")
guns762x25 = ("tt pistol")
guns762x39 = ("ak-103", "ak-104", "akm", "akmn", "akms", "akmsn", "vepr km/vpo-136", "op-sks", "sks", )
guns762x51 = ("dt mdr .308", "sa-58", "vepr hunter/vpo-101", "m1a", "rsass", "sr-25", "dvl-10", "m700", "t-5000")
guns762x54 = ("svds", "mosin", "mosin inf.", "sv-98")
guns366 = ("vepr akm/vpo-209", "vpo-215")
guns46x30 = ("mp7a1", "mp7a2")
guns57x28 = ("p90", "fn 5-7")
guns9x18 = ("pp-9", "pp-91", "pp-91-01", "apb", "aps", "pb pistol", "pm pistol")
guns9x19 = ("mp5", "mp5kn", "mp9", "mp9-n", "mpx", "pp-19-01 vitaz SN", "saiga-9", "glock17", "glock18c", "m9a3", "mp-433 'grach'", "p226r")
guns9x21 = ("sr-1mp gyurza")
guns9x39 = ("as val", "vss vintorez", )
guns12x70 = ("m870", "mp-133", "mp-153", "saiga-12")
guns20x70 = ("toz-106", "null")

def bulletCalculate127x55(totalWeight, guns127x55):
    if totalWeight <= 60:
        return bullets127x55[5]
    if totalWeight <=120:
        return bullets127x55[4]
    if totalWeight <=180:
        return bullets127x55[3]
    if totalWeight <=240:
        return bullets127x55[2]
    if totalWeight <=300:
        return bullets127x55[1]


maps = ("the lab", "interchange", "woods", "customs", "factory", "reserve", "shoreline")
weight = 0


mapName = input("Which map are you playing on?\n")
budget = input("What is your budget? Please enter one of the following: ""extremely low"", ""low"", ""medium"", ""high"", or ""extremely high:""\n")
gunName = input("What gun are you using?\n")
objective = input("Are you focusing on killing scavs? Yes or no.\n")

if objective.strip().lower() == "yes":
    objective = 0
else:
    objective = 100

budget = budget.strip().lower()
if budget == "extremely low":
    budget = 0
if budget == "low":
    budget = 25
if budget == "medium":
    budget = 50
if budget == "high":
    budget = 75
if budget == "extremely high":
    budget = 100
    

mapName = mapName.strip().lower()
gunName = gunName.strip().lower()

def calculateWeight(mapWeight, budget, objective):
    totalWeight = mapWeight[mapName] + budget + objective
    return totalWeight

totalWeight = calculateWeight(mapWeight, budget, objective)

ammoType = 0


while ammoType == 0:
    for item in guns127x55:
        if gunName == item:
            ammoType = "127x55"
    for item in guns545x39:
        if gunName == item:
            ammoType = "545x39"
    

# ***CONTINUE HERE ***
if ammoType == "127x55":
    print(bulletCalculate127x55(totalWeight, guns127x55))
    print(bullets127x55[1], bullets127x55[5])