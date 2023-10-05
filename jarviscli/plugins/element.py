from plugin import plugin



@plugin("element")
def element(jarvis, s):
    from collections import namedtuple

    #symbol atomic_number atomic_mass group

    elements = {
        'Hydrogen': ('H', '1', '1', 'Non Metals'),
        'Helium': ('He', '2', '4', 'Noble Gases'),
        'Lithium': ('Li','3', '7', 'Alkali Metals'),
        'Berylium': ('Be', '4', '9', 'Alkaline Earth Metals'),
        'Boron': ('B', '5', '11', 'Non Metals'),
        'Carbon': ('C', '6', '12', 'Non Metals'),
        'Nitrogen': ('N', '7', '14', 'Non Metals'),
        'Oxygen': ('O', '8', '16', 'Non Metals'),
        'Fluorine': ('F', '9', '19', 'Halogens'),
        'Neon': ('Ne', '10', '20', 'Noble Gasses'),
        'Sodium': ('Na', '11', '23', 'Alkali Metals'),
        'Magnesium': ('Mg', '12', '24', 'Alkaline Earth Metal'),
        'Aluminium': ('Al', '13', '27', 'Other Metals'),
        'Silicon': ('Si', '14', '28', 'Non Metals'),
        'Phosphorus': ('P', '15', '31', 'Non Metals'),
        'Sulfur': ('S', '16', '32', 'Non Metals'),
        'Chlorine': ('Cl', '17', '35.5', 'Halogens'),
        'Argon': ('Ar', '18', '40', 'Noble Gasses'),
        'Potassium': ('K', '19', '39', 'Alkali Metals'),
        'Calcium': ('Ca', '20', '40', 'Alkaline Earth Metals'),
        'Scandium': ('Sc', '21', '45', 'Transition Metals'),
        'Titanium': ('Ti','22', '48', 'Transition Metals'),
        'Vanadium': ('V','23', '51', 'Transition Metals'),
        'Chromium': ('Cr', '24', '52', 'Transition Metals'),
        'Manganese': ('Mn', '25', '55', 'Transition Metals'),
        'Iron': ('Fe', '26', '56', 'Transition Metals'),
        'Cobalt': ('Co', '27', '59', 'Transition Metals'),
        'Nickel': ('Ni', '28', '59', 'Transition Metals'),
        'Copper': ('Cu', '29', '63.5', 'Transition Metals'),
        'Zinc': ('Zn', '30', '65', 'Transition Metals'),
        'Gallium': ('Ga', '31', '70', 'Other Metals'),
        'Germanium': ('Ge', '32', '73', 'Other Metals'),
        'Arsenic': ('As', '33', '75', 'Non Metals'),
        'Selenium': ('Se', '34', '79', 'Non Metals'),
        'Bromine': ('Br', '35', '80', 'Halogens'),
        'Krypton': ('Kr', '36', '84', 'Noble Gasses'),
        'Rubidium': ('Rb', '37', '85', 'Alkali Metals'),
        'Strontium': ('Sr', '38', '88', 'Alkaline Earth Metals'),
        'Yttrium': ('Y', '39', '89', 'Transition Metals'),
        'Zirconium': ('Zr', '40', '91', 'Transition Metals'),
        'Niobium': ('Nb', '41', '93', 'Transition Metals'),
        'Molybdenum': ('Mo', '42', '96', 'Transition Metals'),
        'Technetium': ('Tc', '43', '98', 'Transition Metals'),
        'Ruthenium': ('Ru', '44', '101', 'Transition Metals'),
        'Rhodium': ('Rh', '45', '103', 'Transition Metals'),
        'Palladium': ('Pd', '46', '106', 'Transition Metals'),
        'Silver': ('Ag', '47', '108', 'Transition Metals'),
        'Cadmium': ('Cd', '48', '112', 'Transition Metals'),
        'Indium': ('In', '49', '115', 'Other Metals'),
        'Tin': ('Sn', '50', '119', 'Other Metals'),
        'Antimony': ('Sb', '51', '122', 'Other Metals'),
        'Tellurium': ('Te', '52', '128', 'Non Metals'),
        'Iodine': ('I',' 53', '127', 'Halogens'),
        'Xenon': ('Xe', '54', '131', 'Noble Gasses'),
        'Caesium': ('Cs', '55', '133', 'Alkali Metals'),
        'Barium': ('Ba', '56', '137', 'Alkaline Earth Metals'),
        'Lanthanum': ('La', '57', '139', 'Rare Earth Metals'),
        'Astatine': ('At','85' ,'210' , 'Halogens'),
        'Americium': ('Am','95','243' , 'Actinides') ,
        'Actinium': ('Ac','89' ,'227' , 'Actinides'),
        'Bismuth': ('Bi','83' ,'209.0', 'Other Metals'),
        'Bohrium': ('Bh','107 ','264' , 'Transition Metals'),
        'Copernicium': ('Cn','112' ,'285', 'Transition Metals'),
        'Cerium': ('Ce','58' ,'140.1' , 'Lanthanides'),
        'Curium': ('Cm','96' ,'247' , 'Actinides'),
        'Californium': ('Cf','98' ,'251' , 'Actinides'),
        'Dubnium': ('Db','105' ,'268' , 'Transition Metals'),
        'Darmstadtium': ('Ds','110' ,'281' , 'Transition Metals'),
        'Dysprosium': ('Dy','66' ,'162.5' , 'Lanthanides'),
        'Europium': ('Eu','63' ,'152.0' , 'Lanthanides'),
        'Einsteinium': ('Es','99' ,'252' , 'Actinides'),
        'Francium': ('Fr','87' ,'223' , 'Alkaki Metals'),
        'Fermium': ('Fm','100' ,'257' , 'Actinides'),
        'Gold': ('Au','79' ,'197.0' , 'Transition Metals'),
        'Gadolinium': ('Gd','64' ,'157.2' , 'Lanthanides'),
        'Hafnium': ('Hf','72' ,'178.5' , 'Transition Metals'),
        'Hassium': ('Hs','108' ,'277' , 'Transition Metals'),
        'Holmium': ('Ho','67' ,'164.9' , 'Lanthanides'),
        'Iridium': ('Ir','77' ,'192.2' , 'Transition Metals'),
        'Lead': ('Pb','82' ,'207.2' , 'Other Metals'),
        'Lutetium': ('Lu','71' ,'175.0' , 'Lanthanides'),
        'Lawrencium': ('Lr','103' ,'262' , 'Actinides'),
        'Meitnerium': ('Mt','109' ,'276' , 'Transition Metals'),
        'Mendelevium': ('Md','101' ,'258' , 'Actinides'),
        'Neodymium': ('Nd','60' ,'144.2' , 'Lanthanides'),
        'Nobelium': ('No','102' ,'259' , 'Actinides'),
        'Neptunium': ('Np','93' ,'237' , 'Actinides'),
        'Osmium': ('Os','76' ,'190.2' , 'Transition Metals'),
        'Platinum': ('Pt','78' ,'195.1' , 'Transition Metals'),
        'Plutonium': ('Pu','94' ,'244' , 'Actinides'),
        'Promethium': ('Pm','61' ,'145' , 'Lanthanides'),
        'Protactinium': ('Pa','91' ,'231.0' , 'Actinides'),
        'Praseodymium': ('Pr','59' ,'140.9' , 'Lanthanides'),
        'Radon': ('Rn','86' ,'222' , 'Noble Gases'),
        'Rhenium': ('Re','75' ,'186.2' , 'Transition Metals'),
        'Radium': ('Ra','88' ,'226' , 'Alkaline Earth Metals'),
        'Rutherfordium': ('Rf','104' ,'265' , 'Transition Metals'),
        'Roentgenium': ('Rg','111' ,'280' , 'Transition Metals'),
        'Seaborgium': ('Sg','106' ,'271' , 'Transition Metals'),
        'Samarium': ('Sm','62' ,'150.4' , 'Lanthanides'),
        'Tantalum': ('Ta','73' ,'180.9' , 'Transition Metals'),
        'Tungsten': ('W','74' ,'183.9' , 'Transition Metals'),
        'Thallium': ('Tl','81' ,'204.38' , 'Other Metals'),
        'Terbium': ('Tb','65' ,'158.9' , 'Lanthanides'),
        'Thulium': ('Tm','69' ,'168.9' , 'Lanthanides'),
        'Thorium': ('Th','90' ,'232.0' , 'Actinides'),
        'Uranium': ('U','92' ,'238.0' , 'Actinides'),
        'Ytterbium': ('Yb','70' ,'173.0' , 'Lanthanides'),
    }
    found = False
    element = str(input("Enter a periodic element: ").strip().capitalize())
    for key,value in elements.items():
        if (element == key):
            jarvis.say(
                f'Symbol: {value[0]}'
                + '\nAtomic Number: '
                + value[1]
                + '\nAtomic Mass: '
                + value[2]
                + '\nGroup: '
                + value[3]
            )
            found = True
    if not found:
        jarvis.say('Please make sure you typed the element correctly.')

