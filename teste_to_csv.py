#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:40:02 2018

@author: jherfson
"""
from pymatgen.analysis.pourbaix.entry import PourbaixEntry, IonEntry #, MultiEntry
from pymatgen.analysis.pourbaix.entry import PourbaixEntryIO
from pymatgen.analysis.phase_diagram import PDEntry
from pymatgen.core.ion import Ion
from pymatgen.core.structure import Composition

 
Zn_solids = ["Zn", "ZnO", "ZnO2"]
sol_g = [0.0, -3.338, -1.315]
Zn_ions = ["Zn[2+]", "ZnOH[+]", "HZnO2[-]", "ZnO2[2-]", "ZnO"]
liq_g = [-1.527, -3.415, -4.812, -4.036, -2.921]
liq_conc = [1e-6, 1e-6, 1e-6, 1e-6, 1e-6]
solid_entry = list()
for sol in Zn_solids:
    comp = Composition(sol)
    delg = sol_g[Zn_solids.index(sol)]
    solid_entry.append(PourbaixEntry(PDEntry(comp, delg)))
ion_entry = list()
for ion in Zn_ions:
    comp_ion = Ion.from_formula(ion)
    delg = liq_g[Zn_ions.index(ion)]
    conc = liq_conc[Zn_ions.index(ion)]
    PoE = PourbaixEntry(IonEntry(comp_ion, delg))
    PoE.conc = conc
    ion_entry.append(PoE)
entries = solid_entry + ion_entry
PourbaixEntryIO.to_csv("pourbaix_test_entries.csv", entries)
 


