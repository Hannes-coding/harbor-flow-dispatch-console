"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""

"Feature: you can scroll down to see what you wrote"

import math

#To clear unnecessary parts. (looks cleaner)
def clear():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_number(prompt, error_message="Invalid input", cast=float, min_value=0, max_value=math.inf):
    """Keep asking until the user enters something that converts with `cast`
    and is >= min_value. Never crashes on bad input."""
    while True:
        raw = input(prompt)
        try:
            value = cast(raw)
        except ValueError:
            print("")
            print(error_message)
            print("")
            continue

        if  value < min_value or value > max_value:
            print("")
            print(error_message)
            print("")
            continue

        return value

def get_number_list(prompt, error_message="Invalid input", cast=float, min_value=0, count=None):
    """Keep asking until the user enters a comma-separated list where every
    value converts with `cast`, is >= min_value, and (optionally) the list
    has exactly `count` items."""
    while True:
        raw = input(prompt)
        parts = raw.split(",")
        try:
            values = [cast(part.strip()) for part in parts]
            if min_value is not None and any(v < min_value for v in values):
                raise ValueError
            if count is not None and len(values) != count:
                raise ValueError
        except ValueError:
            print("")
            print(error_message)
            print("")
            continue

        return values

def main():
    """Start the terminal based application and prompt the user with options for calling other programs or closing the console.
    The cases are where the programs will be called. its based on the programs id.
    """

    clear()
    clear()

    run = True
    while run:
        program_id = get_number("""
        HARBORFLOW DISPATCH CONSOLE
        1. Close console
        2. Validate booking reference
        3. Calculate delivery quote
        4. Consolidate parcel labels
        5. Check van capacity
        6. Classify service performance
        7. Produce weekly dispatch report
        8. Compare service scenarios
        Select service: """, "Error - Select a service from 1 to 8.", int, 1, 8)

        match program_id:
            case 1:
                clear()
                print("Console closed. Dispatch data remains safe.")
                run = False
            case 2:
                clear()
                print("2. Validate booking reference")
                print("______________________________")
                print("")

                booking_reference = input("Booking reference: ")
                normalized_reference = validate_reference(booking_reference)
                print(normalized_reference)
            case 3:
                clear()
                print("3. Calculate delivery quote")
                print("____________________________")
                print("")

                distance = get_number("Distance (km): ", "Error - Value must be greater than zero.")
                weight = get_number("Weight (kg): ", "Error - Value must be greater than zero.")

                service_code = input("Service Code: ").upper()
                while service_code != "X" and service_code != "S" and service_code != "P":
                    print("")
                    print("Error - Service code must be S, X or P.")
                    print("")
                    service_code = (input("Service Code: ")).upper().strip()

                consolidate_delivery_quote(distance, weight, service_code)
            case 4:
                clear()
                print("4. Consolidate parcel labels")
                print("_____________________________")
                print("")

                lable = input("Label: ")
                consolidate_parcel_labels(lable)
            case 5:
                clear()
                print("5. Check van capacity")
                print("______________________")
                print("")

                van_cap = get_number(
                    "Van capacity: ", 
                    "Error - Value must be greater than zero.")
                parecel_weights = get_number_list(
                    "Enter parcel weights separated by commas: ", 
                    "Error - Enter valid numbers separated by commas.")

                check_van_capacity(van_cap, parecel_weights)
            case 6:
                clear()
                print("6. Classify service performance")
                print("________________________________")
                print("")

                promised_minutes = get_number("Promised minutes: ", "Error - Value must be greater than zero.")
                actual_minutes =  get_number("Actual minutes: ", "Error - Value must be greater than zero.")
                damaged_parcels =  get_number("Damaged parcels: ", "Error - Value must be greater than zero.", int)

                delay, status = classify_service_performance(promised_minutes, actual_minutes, damaged_parcels)

                print(f"Promised minutes: {promised_minutes}")
                print(f"Actual minutes: {actual_minutes}")
                print(f"Damaged parcels: {damaged_parcels}")

                clear()

                print(f"Delay: {delay} minutes")
                print(f"Service status: {status}")
            case 7:
                clear()
                print("7. Produce weekly dispatch report")
                print("__________________________________")
                print("")

                delivery_count = get_number_list("Completed deliveries: ", "Error - Weekly report requires 7 delivery counts.", int, count=7)
                target = get_number("Daily target: ", "Error - Value must be greater than zero.", int)

                weekly_report(delivery_count, target)
            case 8:
                clear()
                print("8. Compare service scenarios")
                print("_____________________________")
                print("")

                distance = get_number("Distance (km): ", "Error - Value must be greater than zero.")
                weight= get_number("Weight (kg): ", "Error - Value must be greater than zero.")

                compare_delivery_scenarios(distance, weight)

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


def calculate_delivery_quote(distance, weight, service_multiplier):
    subtotal = 45.00 + (distance * 6.50) + (weight * 4.00)
    return subtotal * service_multiplier


def consolidate_delivery_quote(distance, weight, service_code):

    clear()

    # Determine service type and multiplier
    if service_code == "S":
        service_multiplier = 1.0
    elif service_code == "X":
        service_multiplier = 1.25
    elif service_code == "P":
        service_multiplier = 1.6

    # Calculate the delivery quote
    quote = calculate_delivery_quote(distance, weight, service_multiplier)

    print(f"Distance (km): {distance}")
    print(f"Weight (kg): {weight}")
    print(f"Service code: {service_code}")

    clear()

    print(f"Delivery Quote: {quote:.2f} SEK")

# Task 4
# scanned labels: gb-104, GB-220, gb-104, se-011, GB-220
# Unique load list:
# 1. GB-104
# 2. GB-220
# 3. SE-011
# Total unique parcels: 3

def consolidate_parcel_labels(label):

    clear()

    scanned_labels = label
    unique_labels = []
    for word in label.upper().split():
        clean_word = word.strip(",")
        if clean_word not in unique_labels:
            unique_labels.append(clean_word)
    print(f"label: {label}")
    clear()
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

    clear()

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

    clear()

    print(f"Van capacity (kg): {van_cap}")
    print(f"Parcel weights (kg): {parecel_weights}")

    clear()

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

    clear()

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
def weekly_report(deliveries, target):

    clear()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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

    clear()

    print("WEEKLY DISPATCH REPORT")
    print(f"Total deliveries: {total}")
    print(f"Average per day: {average:.2f}")
    print(f"Highest day: {highest_day} ({highest_delivery})")
    print(f"Lowest day: {lowest_day} ({lowest_delivery})")
    print(f"Days meeting target: {days_meeting_target}")


#Task 9
#Compare delivery scenarios

#Reuse your quote calculation function to calculate all three service prices
#Print each option and identify the cheapest and most expensive service

#Technical expectations
#Do not copy the quote formula three times.
#A single calculation function must accept the service code or multiplier.
#Keep the printed order Standard, Express, Priority.
#Format every price with exactly two decimal places
#After Task 8 is implemented, validate distance and weight before calculating.

def compare_delivery_scenarios(distance, weight):

    clear()

    standard = calculate_delivery_quote(distance, weight, 1)
    express = calculate_delivery_quote(distance, weight, 1.25)
    priority = calculate_delivery_quote(distance, weight, 1.6)

    cheap = min(standard, express, priority)
    expensive = max(standard, express, priority)
    services = {
        standard: "Standard",
        express: "Express",
        priority: "Priority",
    }


    print(f"Distance (km): {distance}")
    print(f"Weight (kg): {weight}")

    clear()

    print("SERVICE COMPARISON")
    print(f"Standard: {standard:.2f} SEK")
    print(f"Express: {express:.2f} SEK")
    print(f"Priority: {priority:.2f} SEK")
    print(f"Cheapest Service: {services[cheap]}")
    print(f"Most Expensive Service: {services[expensive]}")





if __name__ == "__main__":
    main()