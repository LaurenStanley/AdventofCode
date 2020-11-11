data_file = 'CraftMasses.txt'

def get_mass_data():
    f = open('CraftMasses.txt', 'r')
    lines = f.readlines()
    f.close()
    masses = []
    for line in lines:
        line = line.splitlines()
        line = float(line[0])
        masses.append(line)
    return masses

def calculate_fuel(masses):
    total_fuel = 0
    for mass in masses:
        fuel = int(float(mass)/3) - 2
        total_fuel = total_fuel + fuel
    return total_fuel


def main():
    masses = get_mass_data()
    total_fuel = calculate_fuel(masses)
    print("Total Fuel Needed Is: ", total_fuel)
    

if __name__ =="__main__":
    main()

