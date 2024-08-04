import re

def validate_names(names):
    # Define the regex pattern for a valid name
    pattern = re.compile(r"^[A-Z][a-z]*([ ][A-Z][a-z]*)*$")
    
    for name in names:
        if pattern.match(name):
            print(name)
        else:
            print("Invalid name")

# Test the function with the provided list of names
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]
validate_names(names)