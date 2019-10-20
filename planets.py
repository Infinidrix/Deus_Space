def CPlanet(starType):
    Chemical = {
        "Metals":["Lithium","Beryllium","Iron","Nickel","Cobalt","Zinc","Copper","Titanium","Aluminium"],
        "Non-metals":["Hydrogen","Helium","Carbon","Nitrogen","Oxygen"],
        "Compounds": ["Carbondioxide","Methane","Ammonia","Water","Hydrogen Sulphide","Hydrogen Cyanide","Carbonmonoxide","Acetylene","Phosphine" ]
        }
    
     Mass = {
        "A":[("2.097*10^27 - 2.837*10^27 Kilograms"),("volume")],
        "B":[("1.299*10^27 - 1.750*10^27 Kilograms"),("volume")],
        "F":[("1.467*10^26 - 1.084*10^26 Kilograms"),("volume")],
        "G":[("1.690*10^30 - 2.286*10^30 Kilograms"),("1.31*10^18 - 1.49*10^18 cubic Kilometer")]
        }
     
    if starType == "A":
        Mass.pop("A")
    elif starType == "B":
        Mass.pop("B")
    elif starType == "F":
        Mass.pop("F")
    else:
        Mass.pop("G")
        
class Planet:
    def __init__ (self ,mass, volume, chemcom):
        self.mass = mass
        self.volume = volume
        self.temp = chemcom #chemical composition
    def set_mass(self, mass):
        self.mass= mass
    def get_mass(self):
        return self.mass
    def set_volume(self, volume):
        self.volume = volume
    def get_volume(self):
        return self.volume
    def set_chemcom(self, mass):
        self.chemcom = chemcom
    def get_chemcom(self):
        return self.chemcom
    
        
