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
                raise ValueError("Error - Select a service from 1 to 8.")
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
                while distance < 0:
                    print("Error - Value must be greater than zero.")
                    distance = float(input("Distance (km): "))

                weight = float(input("Weight (kg): "))
                while weight < 0:
                    print("Error - Value must be greater than zero.")
                    weight = float(input("Weight (kg): "))

                service_code = (input("Service Code: ")).upper()
                while service_code != "X" and service_code != "S" and service_code != "P":
                    print("Error - Service code must be S, X or P.")
                    service_code = (input("Service Code: ")).upper().strip()
                consolidate_delivery_quote(distance, weight, service_code)
            case 4:
                lable = input("Lable: ")
                consolidate_parcel_labels(lable)
            case 5:
                van_cap = float(input("Van capacity: "))
                while van_cap < 0:
                    print("Invalid input")
                    van_cap = float(input("Van capacity: "))

                while True:
                    weights_input = input("Enter parcel weights separated by commas: ").split(',')
                    parecel_weights = []

                    try:
                        for weight_input in weights_input:
                            weight = float(weight_input.strip())
                            if weight < 0:
                                raise ValueError
                            parecel_weights.append(weight)
                    except ValueError:
                        print("Invalid input")
                        continue

                    break

                check_van_capacity(van_cap, parecel_weights)
            case 6:
                promised_minutes = float(input("Promised minutes: "))
                while promised_minutes < 0:
                    print("Error - Value must be greater than zero.")
                    promised_minutes = float(input("Promised minutes: "))

                actual_minutes = float(input("Actual minutes: "))
                while actual_minutes < 0:
                    print("Error - Value must be greater than zero.")
                    actual_minutes = float(input("Actual minutes: "))

                damaged_parcels = int(input("Damaged parcels: "))
                while damaged_parcels < 0:
                    print("Error - Value must be greater than zero.")
                    damaged_parcels = int(input("Damaged parcels: "))

                delay, status = classify_service_performance(promised_minutes, actual_minutes, damaged_parcels)

                print(f"Delay: {delay} minutes")
                print(f"Service status: {status}")
            case 7:
                    raw_deliveries = input("Completed deliveries: ")
                    while True:
                        delivery_parts = raw_deliveries.split(",")
                        try:
                            deliveries = [int(part.strip()) for part in delivery_parts]
                            if len(deliveries) != 7 or any(delivery < 0 for delivery in deliveries):
                                raise ValueError
                        except ValueError:
                            print("Error - Enter exactly 7 non-negative delivery counts separated by commas.")
                            raw_deliveries = input("Completed deliveries: ")
                            continue
                        break
                    
                    target = int(input("Daily target: "))
                    while target < 0:
                        print("Error - Value must be greater than zero.")
                        target = int(input("Daily target: "))

                    weekly_report(raw_deliveries, target)
            case 8:
                pass

# TASK 2
# Booking reference: hfl-nor-2048
# Valid reference: HFL-NOR-2048

# Booking reference: HFL-N4R-2048 (Invalid)
# Invalid booking reference. 

def contains_hyphens(reference):
    return reference[3] == "-" and reference[7] == "-"

def contains_letters(reference):
    return reference[0:3].isalpha() and reference[4:7].isalpha()

def contains_numbers(reference):
    return reference[8:12].isdigit()

def validate_reference(reference):
    reference = reference.strip().upper()
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

# TASK 6
# Calculate the delay and status for a delivered shippment.
#
# ARGUMENTS
# promised_minutes (float): The estimated minutes for the shippment in minutes
# actual_minites (float): The actual time the shippment took in minutes.
# damaged_parcels (int): The number of damaged parcels upon arriving.
#
# RETURNS
# delay (float): The delay in minutes.
# status (string): A description of the shippment status 
#   (e.i minor or major delay or on time, but most importantly "servide failure" if one of the parcels is damaged).
def classify_service_performance(promised_minutes, actual_minutes, damaged_parcels):
    delay = actual_minutes - promised_minutes

    if damaged_parcels > 0:
        status = "SERVICE FAILURE"
    elif delay <= 0:
        status = "ON TIME"
    elif delay <= 15 :
        status = "MINOR DELAY"
    else:
        status = "MAJOR DELAY"

    return delay, status

#TASK 7
def weekly_report(raw_deliveries, target):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    parts = raw_deliveries.split(",")
    deliveries = []
    for part in parts:
        deliveries.append(int(part.strip()))

    total = 0
    for delivery in deliveries:
        total += delivery
    average = total / 7


    highest_delivery = deliveries[0]
    highest_day = days[0]
    lowest_delivery = deliveries[0]
    lowest_day = days[0]
    days_meeting_target = 0

    for i in range(7):
        delivery = deliveries[i]
        if delivery >= highest_delivery:
            highest_delivery = delivery
            highest_day = days[i]
        if delivery <= lowest_delivery:
            lowest_delivery = delivery
            lowest_day = days[i]
        if delivery >= target:
            days_meeting_target += 1


    print(f"Completed deliveries: {deliveries}")
    print(f"Daily target: {target}")
    print("Weekly dispatch report")
    print(f"Total deliveries: {total}")
    print(f"Average per day: {average:.2f}")
    print(f"Highest day: {highest_day} ({highest_delivery})")
    print(f"Lowest day: {lowest_day} ({lowest_delivery})")
    print(f"Days meeting target: {days_meeting_target}")

#Task 8
#Make validation loops incase user enters a value outside of the range.
#rules:
#1) After an error, repeat only the affected prompt.
#2) The program must not crash

#Templates
#Error - Select a service from 1 to 8.
#Error - Value must be greater than zero.
#Error - Service code must be S, X or P.
#Error - Weekly report requires 7 delivery counts.

#What is Done
#Updated Case 3 (Line 42-58)
#Updated Case 5 (Line 61-84)
#Updated case 6 (Line 84-104)
#Updated case 7 (Line 104-124)
#Selecting service part was perfectly done by Hannes so I just added template.


if __name__ == "__main__":
    main()
