import pandas as pd

with open('filename.txt', 'w') as file:  # Creating a text file named filename.txt and writing into it. No library needed for it
    file.write("Hey this is Saad\n")
    file.write("Who are you")

Pakistan = ["Faisalabad", "Lahore", "Karachi", "Islamabad", "Multan"]
Population = [10000, 8000, 30000, 2500, 5000]
print(f"\nFirst List: {Pakistan}")
print(f"Second List: {Population}")
print()

dict_country = {"Pakistan": Pakistan, "Population": Population}  # This stores the 2 lists in the form of indexes

df = pd.DataFrame(dict_country)

print("\n------------------------------------------------\n")

print(" -> DataFrame: 👇\n")
print(df)

df.to_csv("states.csv", index = False) # Exporting the Data Frame to CSV file without index numbers

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

# Exception Handling
print("\n------------------------------------------------\n")

print(" -> EXCEPTION HANDLING 👇\n")
mixed_list = [1, 2, 'three', 4, 'five', 6]

for i, element in enumerate(mixed_list):
    try:
        result = element / 2
        print(result)
    except TypeError:
        print("Element is not an integer")
