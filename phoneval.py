import NigerianPhone

phone = NigerianPhone('+2348135087966')

# Check if is valid
phone.is_valid() #True

# Get formatted
phone.formatted() #08135087966

# Get Network
phone.get_network() #mtn

# Check if is mtn
phone.is_mtn() # True


# Get network from phone number prefix e.g
phone.get_network_by_prefix('0703') # mtn