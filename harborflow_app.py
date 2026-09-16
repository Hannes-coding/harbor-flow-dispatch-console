"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""

def main():
    """Start the terminal based application and prompt the user with options for calling other programs or closing the console.
    The cases are where the programs will be called. its based on the programs id.
    """

    run = True
    while run:
        program_id = int(input("""
        HARBORFLOW DISPATCH CONSOLE
        1. Close console
        2. Validate booking reference
        3. Calculate delivery quote
        4. Consolidate parcel labels
        5. Check van capacity
        6. Classify service performance
        7. Produce weekly dispatch report
        8. Compare service scenarios
        Select service: """))

        """Simple error handling for the user input"""
        try:
            program_id = int(program_id)
            if program_id < 1 or program_id > 8:
                raise ValueError("Invalid input")
        except ValueError as error:
            print(error)

        match program_id:
            case 1:
                print("Console closed. Dispatch data remains safe.")
                run = False
            case 2:
                booking_reference = input("Booking reference: ")
                normalized_reference = validate_reference(booking_reference)
                print(normalized_reference)
            case 3:
                distance = float(input("Distance (km): "))
                weight = float(input("Weight (kg): "))
                service_code = (input("Service Code: ")).upper()
                consolidate_delivery_quote(distance, weight, service_code)
            case 4:
                lable = input("Lable? ")
                consolidate_parcel_labels(lable)
            case 5:
                van_cap = float(input("Van capacity: "))

                weights_input = input("Enter parcel weights separated by commas: ")
                parecel_weights = [float(w.strip()) for w in weights_input.split(",")]

                check_van_capacity(van_cap, parecel_weights)
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass

# TASK 2
# Booking reference: hfl-nor-2048
# Valid reference: HFL-NOR-2048

# Booking reference: HFL-N4R-2048 (Invalid)
# Invalid booking reference. 

def remove_leading_and_trailing_spaces(reference):
   reference = reference.strip()
   reference = reference.upper()
   return reference

def contains_hyphens(reference):
    return reference[3] == "-" and reference[7] == "-"

def contains_letters(reference):
    return reference[0:3].isalpha() and reference[4:7].isalpha()

def contains_numbers(reference):
    return reference[8:12].isdigit()

def validate_reference(reference):
    reference = remove_leading_and_trailing_spaces(reference)
    if len(reference) == 12 and contains_hyphens(reference) and contains_letters(reference) and contains_numbers(reference):
        return reference
    else:
        return ""

# TASK 3
# Give sales staff a consistent quote before they promise a price to a customer.
#
# distance (float):
# wight (float):
# service_code (string): either "S", "X" or "P"
#
# Prints the delivery quote

def consolidate_delivery_quote(distance, weight, service_code):
    Base_charge = 45.00

    # Validate arguments
    if distance <= 0 or weight <= 0:
        print("Error: Distance and weight must be positive numbers.")
        return

    # Determine service type and multiplier
    if service_code == "S":
        service_multiplier = 1.0
    elif service_code == "X":
        service_multiplier = 1.25
    elif service_code == "P":
        service_multiplier = 1.6
    else:
        print("Error: Invalid service type.")
        return

    # Calculate the delivery quote
    subtotal = Base_charge + (distance * 6.50) + (weight * 4.00)
    quote = subtotal * service_multiplier

    print(f"Delivery Quote: {quote:.2f} SEK")

# Task 4
# scanned labels: gb-104, GB-220, gb-104, se-011, GB-220
# Unique load list:
# 1. GB-104
# 2. GB-220
# 3. SE-011
# Total unique parcels: 3

def consolidate_parcel_labels(label):
    scanned_labels = label
    unique_labels = []
    for word in label.upper().split():
        clean_word = word.strip(",")
        if clean_word not in unique_labels:
            unique_labels.append(clean_word)
    print(f"scanned labels: {scanned_labels}")
    print("Unique load list:")
    i = 0
    while len(unique_labels) > i:
        print(f"{i+1}: {unique_labels[i]}")
        i +=1
    print(f"Total unique parcels: {len(unique_labels)}")

# TASK 5
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

if __name__ == "__main__":
    main()
