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
        Select service: """))

        """Simple error handling for the user input"""
        try:
            program_id = int(program_id)
            if program_id < 1 or program_id > 7:
                raise ValueError("Invalid input")
        except ValueError as error:
            print(error)

        match program_id:
            case 1:
                print("Console closed. Dispatch data remains safe.")
                run = False
            case 2:
                # Call function 2 (validatie booking reference)
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass


#TASK 3
def consolidate_delivery_quote():


    # Input by user and base variables
    Base_charge = 45.00
    distance = float(input("Distance (km): "))
    Weight = float(input("Weight (kg): "))
    service_multiplier = (input("Service Code): ")).upper()

    # Validate inputs
    if distance <= 0 or Weight <= 0:
        print("Error: Distance and weight must be positive numbers.")
        return

    # Determine service type and multiplier
    if service_multiplier == "S":
        service_multiplier = 1.0
        service_code = "S"
    elif service_multiplier == "X":
        service_multiplier = 1.25
        service_code = "X"
    elif service_multiplier == "P":
        service_multiplier = 1.6
        service_code = "P"
    else:
        print("Error: Invalid service type.")
        return

    # Calculate the delivery quote
    subtotal = Base_charge + (distance * 6.50) + (Weight * 4.00)
    quote = subtotal * service_multiplier


    print(f"Delivery Quote: {quote:.2f} SEK")


if __name__ == "__main__":
    consolidate_delivery_quote()


if __name__ == "__main__":
    main()


    
