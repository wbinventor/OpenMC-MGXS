import openmc

...

fuel = openmc.Cell(...)
clad = openmc.Cell(...)
moderator = openmc.Cell(...)

...

# Create geometry for model
geometry = openmc.Geometry(...)

...

# Specify energy group structure
groups = openmc.mgxs.EnergyGroups([0.0, 1.0, 20.0e6])

# Create MGXS library
library = openmc.mgxs.Library(geometry)
library.energy_groups = groups

# Identify desired cross sections
library.mgxs_types = ['transport', 'fission', 'total', 'scatter matrix']

# Identify desired spatial domains
library.domain_type = 'cell'
library.domains = [fuel, clad, moderator]

# Add tallies to collection and export to XML
tallies = openmc.Tallies()
library.add_to_tallies_file(tallies)
tallies.export_to_xml()

# Run OpenMC and read in results of simulation
openmc.run()
sp = openmc.StatePoint('statepoint.500.h5')

# Load results into Library object
library.load_from_statepoint(sp)
