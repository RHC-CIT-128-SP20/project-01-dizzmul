#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Initializing variables + dictionaries

mapName =""

maps = ("the lab", "interchange", "woods", "customs", "factory", "reserve", "shoreline")

weight = 0

mapWeight ={'the lab' : 100, 'reserve' : 80, 'factory' : 50, 'woods' : 50, 'customs' : 40, 'interchange' : 60, 'shoreline' : 40}

gunsDict = {"ash-12": "127x55", 
"ak-105": "545x39", "ak-74": "545x39", "ak-74m": "545x39", "ak-74n": "545x39", "aks-74": "545x39", "aks-74u": "545x39", "aks-74ub": "545x39", "aks-74un": "545x39", "rpk-16": "545x39",
"adar 2-15": "556x45", "ak-101": "556x45", "ak-102": "556x45", "dt mdr": "556x45", "hk 416a5": "556x45", "m4a1": "556x45", "tx-15 dml": "556x45",
"tt pistol": "762x25", "ppsh-41": "762x25",
"ak-103": "762x39", "ak-104": "762x39", "akm": "762x39", "akmn": "762x39", "akms": "762x39", "akmsn": "762x39", "vepr km/vpo-136": "762x39", "op-sks": "762x39", "sks": "762x39", 
"dt mdr .308": "762x51", "sa-58": "762x51", "vepr hunter/vpo-101": "762x51", "m1a": "762x51", "rsass": "762x51", "sr-25": "762x51", "dvl-10": "762x51", "m700": "762x51", "t-5000": "762x51",
"svds": "762x54", "mosin": "762x54", "mosin inf.": "762x54", "sv-98": "762x54",
"vepr akm/vpo-209": "366", "vpo-25": "366",
"mp7a1": "46x30", "mp7a2": "46x30",
"p90": "57x28", "fn 5-7": "57x28",
"pp-9": "9x18", "pp-91": "9x18", "pp-91-01": "9x18", "apb": "9x18", "aps": "9x18", "pb pistol": "9x18", "pm pistol": "9x18",
"mp5": "9x19", "mp5kn": "9x19", "mp9": "9x19", "mp9-n": "9x19", "mpx": "9x19", "pp-19-01 vitaz sn": "9x19", "saiga-9": "9x19", "glock17": "9x19", "glock18c": "9x19", "m9a3": "9x19", "mp-433 'grach'": "9x19", "p226r": "9x19",
"sr-1mp gyurza": "9x21",
"as val": "9x39", "vss vintorez": "9x39",
"m870": "12x70", "mp-133": "12x70", "mp-153": "12x70", "saiga-12": "12x70", 
"toz-106": "20x70"}

# These dictionaries are used to rank ammo from best(most expensive) to worst, respectively.
bullets127x55 = {1: "AP-20 Slugs", 2: "Flechette rounds", 3: "RIP rounds", 4: "Poleva-6u Slug", 5: "8.5mm Magnum Buckshot"} # For 12.7x55 rounds, AP-20 Slugs are the best, 8.5mm Magnum Slugs are the worst, but still best on a budget
bullets545x39 = {1: "7N39 Igolnik", 2: "BS rounds", 3: "BT Rounds", 4: "BP Rounds"}
bullets556x45 = {1: "M995 Rounds", 2:"M855A1 Rounds", 3: "M856A1 Rounds"}
bullets762x25 = {1: "LRNPC Rounds", 2: "AKBS Rounds"}
bullets762x39 = {1: "BP Rounds", 2: "PS Rounds"}
bullets762x51 = {1: "M62 Rounds", 2: "M61 Rounds", 3: "M80 Rounds"}
bullets762x54 = {1: "7n1 Rounds", 2: "SNB Rounds", 3: "LPS Gzh Rounds"}
bullets366 = {1: "EKO Rounds", 2: "FMJ Rounds", 3: "Geksa Rounds"}
bullets46x30 = {1: "AP SX Rounds", 2: "FMJ SX Rounds"}
bullets57x28 = {1: "SB193 Rounds", 2: "SS190 Rounds"}
bullets9x18 = {1: "PMM Rounds if using Klin/PM, PBM Rounds if using Kedr/Kedr-B"}
bullets9x19 = {1: "RIP Rounds for leg meta, AP 6.3 Rounds for penetration", 2: "Pst gzh rounds"}
bullets9x21 = {1: "SP13 Rounds"}
bullets9x39 = {1: "BP Rounds", 2: "SPP Rounds", 3: "SP-6 Rounds"}
bullets12x70 = {1: "AP-20 Slugs or Flechette rounds", 2: "RIP Rounds (Aim for legs)", 3: "Poleva Slugs or 8.5mm Magnum Buckshot"}
bullets20x70 = {1: "Buckshot"}

allGuns = ("ash-12", "null", "ak-105", "ak-74", "ak-74m", "ak-74n", "aks-74", "aks-74n", "aks-74u", "aks-74ub", "aks-74un", "rpk-16", "adar 2-15", "ak-101", "ak-102", "dt mdr", "hk 416a5", "m4a1", "tx-15 dml", "tt pistol", "ppsh-41", 
"ak-103", "ak-104", "akm", "akmn", "akms", "akmsn", "vepr km/vpo-136", "op-sks", "sks", "dt mdr .308", "sa-58", "vepr hunter/vpo-101", "m1a", "rsass", "sr-25", "dvl-10", "m700", "t-5000", "svds", "mosin", "mosin inf.", "sv-98", "vepr akm/vpo-209", "vpo-215", 
"mp7a1", "mp7a2", "p90", "fn 5-7", "pp-9", "pp-91", "pp-91-01", "apb", "aps", "pb pistol", "pm pistol", "mp5", "mp5kn", "mp9", "mp9-n", "mpx", "pp-19-01 vitaz sn", "saiga-9", "glock17", "glock18c", "m9a3", "mp-433 'grach'", "p226r", 
"sr-1mp gyurza", "as val", "vss vintorez", "m870", "mp-133", "mp-153", "saiga-12", "toz-106")

guns127x55 = ("ash-12", "null")
guns545x39 = ("ak-105", "ak-74", "ak-74m", "ak-74n", "aks-74", "aks-74n", "aks-74u", "aks-74ub", "aks-74un", "rpk-16")
guns556x45 = ("adar 2-15", "ak-101", "ak-102", "dt mdr", "hk 416a5", "m4a1", "tx-15 dml")
guns762x25 = ("tt pistol", "ppsh-41")
guns762x39 = ("ak-103", "ak-104", "akm", "akmn", "akms", "akmsn", "vepr km/vpo-136", "op-sks", "sks", )
guns762x51 = ("dt mdr .308", "sa-58", "vepr hunter/vpo-101", "m1a", "rsass", "sr-25", "dvl-10", "m700", "t-5000")
guns762x54 = ("svds", "mosin", "mosin inf.", "sv-98")
guns366 = ("vepr akm/vpo-209", "vpo-215")
guns46x30 = ("mp7a1", "mp7a2")
guns57x28 = ("p90", "fn 5-7")
guns9x18 = ("pp-9", "pp-91", "pp-91-01", "apb", "aps", "pb pistol", "pm pistol")
guns9x19 = ("mp5", "mp5kn", "mp9", "mp9-n", "mpx", "pp-19-01 vitaz sn", "saiga-9", "glock17", "glock18c", "m9a3", "mp-433 'grach'", "p226r")
guns9x21 = ("sr-1mp gyurza")
guns9x39 = ("as val", "vss vintorez", )
guns12x70 = ("m870", "mp-133", "mp-153", "saiga-12")
guns20x70 = ("toz-106", "null")

# Function definitions which determine the best ammo, given user input

def bulletCalculate20x70(totalWeight, guns12x70):
    return bullets20x70[1]

def bulletCalculate12x70(totalWeight, guns12x70):
    if totalWeight <=100:
        return bullets12x70[3]
    if totalWeight <=200:
        return bullets12x70[2]
    if totalWeight <=300:
        return bullets12x70[1]

def bulletCalculate9x39(totalWeight, guns9x39):
    if totalWeight <= 100:
        return bullets9x39[3]
    if totalWeight <= 200:
        return bullets9x39[2]
    if totalWeight <= 300:
        return bullets9x39[1]

def bulletCalculate9x21(totalWeight, guns9x21):
    return bullets9x21[1]

def bulletCalculate9x19(totalWeight, guns9x19):
    if totalWeight <=150:
        return bullets9x19[2]
    if totalWeight <=300:
        return bullets9x19[1]

def bulletCalculate9x18(totalWeight, guns9x18):
    return bullets9x18[1]

def bulletCalculate57x28(totalWeight, guns57x28):
    if totalWeight <= 150:
        return bullets57x28[2]
    if totalWeight <= 300:
        return bullets57x28[1]

def bulletCalculate46x30(totalWeight, guns46x30):
    if totalWeight <=150:
        return bullets46x30[2]
    if totalWeight <=300:
        return bullets46x30[1]

def bulletCalculate366(totalWeight, guns366):
    if totalWeight <=100:
        return bullets366[3]
    if totalWeight <=200:
        return bullets366[2]
    if totalWeight <=300:
        return bullets366[3]

def bulletCalculate762x54(totalWeight, guns762x54):
    if totalWeight <= 100:
        return bullets762x54[3]
    if totalWeight <=200:
        return bullets762x54[2]
    if totalWeight <=300:
        return bullets762x54[1]

def bulletCalculate762x51(totalWeight, guns762x51):
    if totalWeight <=100:
        return bullets762x51[3]
    if totalWeight <=200:
        return bullets762x51[2]
    if totalWeight <=300:
        return bullets762x51[1]

def bulletCalculate762x39(totalWeight, guns762x39):
    if totalWeight <=150:
        return bullets762x39[2]
    if totalWeight <=300:
        return bullets762x39[1]


def bulletCalculate762x25(totalWeight, guns762x25):
    if totalWeight <=150:
        return bullets762x25[2]
    if totalWeight <=300:
        return bullets762x25[1]

def bulletCalculate556x45(totalWieght, guns556x45):
    if totalWeight <=100:
        return bullets556x45[3]
    if totalWeight <=200:
        return bullets556x45[2]
    if totalWeight <=300:
        return bullets556x45[1]

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
def bulletCalculate545x39(totalWeight, guns545x39):
    if totalWeight <=75:
        return bullets545x39[4]
    if totalWeight <=150:
        return bullets545x39[3]
    if totalWeight <=225:
        return bullets545x39[2]
    if totalWeight <=300:
        return bullets545x39[1]

# Input retrieval and validity checks

mapName = input("Which map are you playing on?\n")
if mapName.strip().lower() not in maps:
    while mapName.strip().lower() not in maps:
        mapName = input("Invalid input.Try again:\n")

budget = input("What is your budget? Please enter one of the following: ""extremely low"", ""low"", ""medium"", ""high"", or ""extremely high:""\n")
if budget.strip().lower() != "extremely low" and budget.strip().lower() != "low" and budget.strip().lower() != "medium" and budget.strip().lower() != "high" and budget.strip().lower() != "extremely high":
    while budget.strip().lower() != "extremely low" and budget.strip().lower() != "low" and budget.strip().lower() != "medium" and budget.strip().lower() != "high" and budget.strip().lower() != "extremely high":
        budget = input("Invalid input. Try again:\n")


gunName = input("What gun are you using?\n")
if gunName.strip().lower() not in allGuns:
    while gunName.strip().lower() not in allGuns:
        gunName = input("Invalid input. Try again:\n")


objective = input("Are you focusing on killing scavs only?\n")
if objective != "yes" and objective != "no":
    while objective != "yes" and objective != "no":
        objective = input("Invalid input. Try again:\n")

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

    
# Normalizing input
mapName = mapName.strip().lower()
gunName = gunName.strip().lower()

# Calculates "weight" - a word which quantifies the need for expensive/stronger ammo types
def calculateWeight(mapWeight, budget, objective):
    totalWeight = mapWeight[mapName] + budget + objective
    return totalWeight

totalWeight = calculateWeight(mapWeight, budget, objective)

ammoType = gunsDict[gunName]
    
if ammoType == "127x55":
    print(bulletCalculate127x55(totalWeight, guns127x55))
if ammoType == "545x39":
    print(bulletCalculate545x39(totalWeight, guns545x39))
if ammoType == "556x45":
    print(bulletCalculate556x45(totalWeight, guns556x45))
if ammoType == "762x25":
    print(bulletCalculate762x25(totalWeight, guns762x25))
if ammoType == "762x39":
    print(bulletCalculate762x39(totalWeight, guns762x39))
if ammoType == "762x51":
    print(bulletCalculate762x51(totalWeight, guns762x51))
if ammoType == "366":
    print(bulletCalculate366(totalWeight, guns366))
if ammoType == "46x30":
    print(bulletCalculate46x30(totalWeight, guns46x30))
if ammoType == "57x28":
    print(bulletCalculate57x28(totalWeight, guns57x28))
if ammoType == "9x18":
    print(bulletCalculate9x18(totalWeight, guns9x18))
if ammoType == "9x19":
    print(bulletCalculate9x19(totalWeight, guns9x19))
if ammoType == "9x21":
    print(bulletCalculate9x21(totalWeight, guns9x21))
if ammoType == "9x39":
    print(bulletCalculate9x39(totalWeight, guns9x39))
if ammoType == "762x54":
    print(bulletCalculate762x54(totalWeight, guns762x54))
if ammoType == "12x70":
    print(bulletCalculate12x70(totalWeight, guns12x70))
if ammoType == "20x70":
    print(bulletCalculate20x70(totalWeight, guns20x70))