# Van capacity (kg): 100
# Parcel weights (kg): [40, 65, 20, 35]
# Parcel 1: ACCEPTED
# Parcel 2: REJECTED
# Parcel 3: ACCEPTED
# Parcel 4: ACCEPTED
# Accepted parcels: 3
# Loaded weight: 95.00 kg
# Remaining capacity: 5.00 kg

def check_van_capacity(van_cap, parecel_weights):
    parecel_status = []
    i = 0
    free_weight = van_cap
    
    while i < len(parecel_weights):
        if free_weight - parecel_weights[i] >= 0:
            free_weight -= parecel_weights[i]
            parecel_status.append(True)
        else:
            parecel_status.append(False)
        i += 1
        
    # Start count at 0
    accepted_parcels = 0
    for x in parecel_status:
        if x == True:
            accepted_parcels += 1

    print(f"Van capacity (kg): {van_cap}")
    print(f"Parcel weights (kg): {parecel_weights}")
    
    i = 0
    while i < len(parecel_status):
        if parecel_status[i] == True:
            print(f"Parcel {i+1}: ACCEPTED")
        else:
            print(f"Parcel {i+1}: REJECTED")
        i += 1
        
    print(f"Accepted parcels: {accepted_parcels}")
    print(f"Loaded weight: {(van_cap - free_weight):.2f} kg")
    print(f"Remaining capacity: {free_weight:.2f} kg")

check_van_capacity(100, [40, 65, 20, 35])