#Booking reference: hfl-nor-2048
#Valid reference: HFL-NOR-2048


#Booking reference: HFL-N4R-2048 (Invalid)
#Invalid booking reference. 

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
        return True
    else:
        return False

print(validate_reference("HFL-N4R-2048")) #=> False
print(validate_reference("HFL-NgR-2048")) #=> true
print(validate_reference(" HFL-ggg-5638 ")) #=> true
    