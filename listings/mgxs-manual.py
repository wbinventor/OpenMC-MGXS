import openmc

# Create geometry for the model
fuel = openmc.Cell(...)
clad = openmc.Cell(...)
moderator = openmc.Cell(...)

...

# Specify energy group structure
groups = openmc.mgxs.EnergyGroups([0.0, 1.0, 20.0e6])

# Create MGXS object for the fuel only
total_xs = openmc.mgxs.TotalXS(domain=fuel, energy_groups=groups)

# Add tallies to collection and export to XML
tallies = openmc.Tallies()
tallies += total_xs.tallies.values()
tallies.export_to_xml()

# Run OpenMC and read in results of simulation
openmc.run()
sp = openmc.StatePoint('statepoint.500.h5')
total_xs.load_from_statepoint(sp)
