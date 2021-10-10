"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dict
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Pring dict literal representation
print(schools)

# Access a value by its key
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dict by its key
# schools.pop("Duke")

# Test for the existence of a key
# is_duke_present: bool = "Duke" in schools

# print(f"Duke is present: {is_duke_present}")
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")