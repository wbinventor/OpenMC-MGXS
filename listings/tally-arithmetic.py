import openmc

# Open OpenMC's HDF5 statepoint file for the 100th batch
sp = openmc.StatePoint("statepoint.100.h5")

# Extract reaction rate and flux Tally objects
rxn_rates = sp.get_tally(name="reaction rates")
fluxes = sp.get_tally(name="fluxes")

# Slice a Tally with only the "total" reaction rates
total = rxn_rates.get_slice(scores=["total"])

# Compute the total MGXS with tally arithmetic
total_mgxs = total / flux
