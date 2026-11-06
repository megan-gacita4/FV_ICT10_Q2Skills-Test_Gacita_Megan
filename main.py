from pyscript import document, display


elements = {"N": ("Nitrogen", 7, 14.007),
            "O": ("Oxygen", 8, 15.999), 
            "H": ("Hydrogen", 1, 1.008),
            "C": ("Carbon", 6, 12.011),
            "He": ("Helium", 2, 4.0026),
            "Ne": ("Neon", 10, 20.180),
            "Ar": ("Argon", 18, 39.948),
            "Kr": ("Krypton", 36, 83.798),
            "Xe": ("Xenon", 54, 131.293),
            "B": ("Boron", 5, 10.81),
            "Cl": ("Chlorine", 17, 35.45),
            "F": ("Fluorine", 9, 18.998),
            "I": ("Iodine", 53, 126.90),
            "P": ("Phosphorus", 15, 30.974),
            "S": ("Sulfur", 16, 32.06),
            "Se": ("Selenium", 34, 78.971),
            "Br": ("Bromine", 35, 79.904),
            "Rn": ("Radon", 86, 222),}

def find_element(e):
    # Get input from html
    nmetal1 = document.getElementById("nmetal1").value
    
    # retrieve information about the planet from the dictionary
    result = elements.get(nmetal1, ("Element not found", " -", " -"))
    
    # display the result in the html
    # symbol, name, number, and mass of the element
    document.getElementById("symbol").innerText = nmetal1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]