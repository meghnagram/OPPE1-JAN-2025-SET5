def next_roll_no(roll_no: str) -> str:
    """
    Generates the next roll number in sequence within the same term and year.

    Assumes the `num` part of the roll number will be less than 999999.


    Args:
        roll_no (str): The input roll number in the format {yy}f{t}{num}.

    Returns:
        str: The next roll number in sequence.
    """
    
    return f"{roll_no[:4]}{int(roll_no[4:])+1:06}"

# #Another Method:
# def next_roll_no(roll_no: str) -> str:
    
#     return roll_no[0:3]+str(int(roll_no[3::])+1)

# Get Next Roll Number
# Write a function next_roll_no that takes a roll number roll_no as input and returns the next roll number in sequence within the same year and term.

# The roll number format is {yy}f{t}{num}, where:

# {yy} represents the two-digit year
# f is a fixed character
# {t} represents the term number (1, 2, or 3)
# {num} is a six-digit number padded with zeros on the left
# Assume the num part of the roll number will be less than 999999.

# Example

# next_roll_no("23f2000001") -> '23f2000002'
# next_roll_no("24f3099999") -> '24f3100000'
    

