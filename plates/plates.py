def main():
    plate = input("Plate: ").strip()
    if verifica(plate):
        print("Valid")
    else:
        print("Invalid")


def verifica(value):
    
    """
    Validates a personalized license plate.
    Rules:
    - Length between 2 and 6 characters
    - Must start with exactly 2 letters
    - Remaining characters (if any) must be digits only
    - No leading zeros in the numeric part
    """
    
    if not (len(value) >= 2 and len(value) <= 6):
        print("Length must be between 2 and 6 characters")
        return False
    if not value[:2].isalpha():
        print("The first two characters must be alphabetic")
        return False
    for i, v in enumerate(value):
        if v.isdigit():
            if not value[i:].isdigit():  # digits must form a contiguous block at the end
                print("Digits must form a contiguous block at the end")
                return False
            if v == "0":  # no leading zeros allowed
                print("No leading zeros allowed")
                return False
                break
    return True


main()