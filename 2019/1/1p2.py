data_file = 'CraftMasses.txt'

def get_mass_data():
    f = open(data_file, 'r')
    lines = f.readlines()
    f.close()
    masses = []
    for line in lines:
        line = line.splitlines()
        line = float(line[0])
        masses.append(line)
    return masses

def calculate_fuel(mass):
    fuel = int(float(mass)/3) - 2
    if fuel > 0:
        return fuel
    else:
        return 0

def total_fuel(masses):
    total_fuel = 0
    for mass in masses:
        module_fuel = 0
        fuel = calculate_fuel(mass)
        module_fuel += fuel
        while fuel > 0:
            fuel = calculate_fuel(fuel)
            module_fuel += fuel
        total_fuel += module_fuel
    return total_fuel

def main():
    module_masses = get_mass_data()
    #module_masses = [100756]
    total = total_fuel(module_masses)
    print("Total Fuel Needed Is: ", total)
    

if __name__ =="__main__":
    main()

