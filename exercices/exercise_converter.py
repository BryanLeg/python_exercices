nb_miles = input("Enter your distance: ")
converter_miles_into_km = 1.610

try:
    nb_miles = int(nb_miles)
    resultat = nb_miles * converter_miles_into_km
    print(f"{nb_miles} miles is equal to {resultat} km")
except ValueError:
    print("Enter a NUMBER please")
