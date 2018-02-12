from pymatgen.ext.matproj import MPRester
from pymatgen.apps.borg.hive import VaspToComputedEntryDrone
from pymatgen.apps.borg.queen import BorgQueen
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotte

# Assimilate VASP calculations into ComputedEntry object. Let's assume that
# the calculations are for a series of new LixSnySz phases that we want to
# know the phase stability.
drone = VaspToComputedEntryDrone()
queen = BorgQueen(drone, rootpath=".")
entries = queen.get_data()

# Obtain all existing Li-Sn-S phases using the Materials Project REST API
with MPRester("Fvlb5EsNq71JxDy3") as m:
    mp_entries = m.get_entries_in_chemsys(["Li", "Sn", "S"])

# Combined entry from calculated run with Materials Project entries
entries.extend(mp_entries)

# Process entries using the MaterialsProjectCompatibility
compat = MaterialsProjectCompatibility()
entries = compat.process_entries(entries)

# Generate and plot Li-Sn-S phase diagram

pd = PhaseDiagram(entries)
plotter = PDPlotter(pd, color='black', markerfacecolor='c', markersize=15, linewidth = 1)
plotter.show()
