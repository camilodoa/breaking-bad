'''
Find all possible elements you can make with a name (like in the breaking bad
credits)
'''

def solution(input):
    input = input.lower()
    elements = {
        'H': 'Hydrogen',
        'He': 'Helium',
        'Li': 'Lithium',
        'Be':'Beryllium',
	    "B":"Boron",
	    "C":'Carbon',
        "N":'Nitrogen',
        "O":'Oxygen',
        "F":'Fluorine',
        "Ne":'Neon',
        "Na":'Sodium',
        "Mg":'Magnesium',
        "Al":'Aluminum',
        "Si":'Silicon',
        "P":'Phosphorus',
        "S":'Sulfur',
        "Cl":'Chlorine',
        "Ar":'Argon',
        "K":"Potassium",
        "Ca":"Calcium",
        "Sc":"Scandium",
        "Ti":"Titanium",
        "V":"Vanadium",
        "Cr":"Chromium",
        "Mn":"Manganese",
        'Fe':'Iron',
        'Co':'Cobalt',
        'Ni':'Nickel',
        'Cu':'Copper',
        'Zn':'Zinc',
        'Ga':'Gallium',
        'Ge':'Germanium',
        'As':'Arsenic',
        'Se':'Selenium',
        'Br':'Bromine',
        'Kr':'Krypton',
        'Rb':'Rubidium',
        'Sr':'Strontium',
        'Y':'Yttrium',
        'Zr':'Zirconium',
        'Nb':'Niobium',
        'Mo':'Molybdenum',
        'Tc':'Technetium',
        'Ru':'Ruthenium',
        'Rh':'Rhodium',
        'Pd':'Palladium',
        'Ag':'Silver',
        'Cd':'Cadmium',
        'In':'Indium',
        'Sn':'Tin',
        'Sb':'Antimony',
        'Te':'Tellurium',
        'I':'Iodine',
        'Xe':'Xenon',
        'Cs':'Cesium',
        'Ba':'Barium',
        'La':'Lanthanum',
        'Ce':'Cerium',
        'Pr':'Praseodymium',
        'Nd':'Neodymium',
        'Pm':'Promethium',
        'Sm':'Samarium',
        'Eu':'Europium',
        'Gd':'Gadolinium',
        'Tb':'Terbium',
        'Dy':'Dysprosium',
        'Ho':'Holmium',
        'Er':'Erbium',
        'Tm':'Thulium',
        'Yb':'Ytterbium',
        'Lu':'Lutetium',
        'Hf':'Hafnium',
        'Ta':'Tantalum',
        'W':'Tungsten',
        'Re':'Rhenium',
        'Os':'Osmium',
        'Ir':'Iridium',
        'Pt':'Platinum',
        'Au':'Gold',
        'Hg':'Mercury',
        'Tl':'Thallium',
        'Pb':'Lead',
        'Bi':'Bismuth',
        'Po':'Polonium',
        'At':'Astatine',
        'Rn':'Radon',
        'Fr':'Francium',
        'Ra':'Radium',
        'Ac':'Actinium',
        'Th':'Thorium',
        'Pa':'Protactinium',
        'U':'Uranium',
        'Np':'Neptunium',
        'Pu':'Plutonium',
        'Am':'Americium',
        'Cm':'Curium',
        'Bk':'Berkelium',
        'Cf':'Californium',
        'Es':'Einsteinium',
        'Fm':'Fermium',
        'Md':'Mendelevium',
        'No':'Nobelium',
        'Lr':'Lawrencium',
        'Rf':'Rutherfordium',
        'Db':'Dubnium',
        'Sg':'Seaborgium',
        'Bh':'Bohrium',
        'Hs':'Hassium',
        'Mt':'Meitnerium',
        'Ds':'Darmstadtium',
        'Rg':'Roentgenium',
        'Cn':'Copernicium',
        'Nh':'Nihonium',
        'Fl':'Flerovium',
        'Mc':'Moscovium',
        'Lv':'Livermorium',
        'Ts':'Tennessine',
        'Og':'Oganesson'
    }

    n = len(input)
    solutions = {}

    for i in range(n):
        # 1 to 5 because we're looking at the character itself,
        # and up to 2 characters after it
        for j in range(1, 3):
            if i + j < n:
                test = elements.get(input[i: i + j].capitalize())
                if test:
                    solutions.update({input[i: i + j].capitalize(): test})

    return solutions

print(solution("Camilo Diego Ortiz Arribas Gomez Waterlot"))
