import openmc

# Create geometry for the model
fuel = openmc.Cell(...)
clad = openmc.Cell(...)
moderator = openmc.Cell(...)

...

# Specify energy group structure
groups = openmc.mgxs.EnergyGroups([0.0, 1.0, 20.0e6])

# Create MGXS library
library = openmc.mgxs.Library(geometry)
library.energy_groups = groups

# Specify desired reactions and spatial domains
library.mgxs_types = ['transport', 'fission', 'total', 'scatter matrix']
library.domain_type = 'cell'
library.domains = [fuel, clad, moderator]

# Add tallies to collection and export to XML
tallies = openmc.Tallies()
library.add_to_tallies_file(tallies)
tallies.export_to_xml()

# Run OpenMC and read in results of simulation
openmc.run()
sp = openmc.StatePoint('statepoint.500.h5')
library.load_from_statepoint(sp)
