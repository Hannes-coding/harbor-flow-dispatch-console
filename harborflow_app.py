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

if __name__ == "__main__":
    main()
