# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 12:13:12 2025

@author: ramin
"""

def totalkostnad_elbil(km_per_år, dager):
    forsikring = 5000
    trafikkforsikringsavgift = 8.38 * dager
    drivstoff = km_per_år * 0.4
    bom = km_per_år * 0.1
    return forsikring + trafikkforsikringsavgift + drivstoff + bom
    

def totalkostnad_bensinbil(km_per_år, dager):
    forsikring = 7500
    trafikkforsikringsavgift = 8.38 * dager
    drivstoff = km_per_år * 0.1
    bom = km_per_år * 0.1
    return forsikring + trafikkforsikringsavgift + drivstoff + bom

km_per_år = 10000
dager = 365

elbil_kostnad = totalkostnad_elbil(km_per_år, dager)
bensin_kostnad = totalkostnad_bensinbil(km_per_år, dager)
differanse = elbil_kostnad - bensin_kostnad

print(str(elbil_kostnad) + " kr for elbil")
print(str(bensin_kostnad) + "  kr for bensinbil")
print("Differanse:" + str(differanse))    