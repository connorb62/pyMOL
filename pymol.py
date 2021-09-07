# Calculate Mol

# Calculate Option
calculate = input('Calculate? (M/E/P/N or HELP): ').upper()
print('-----------------')

# Gather Input From User
element = input('Element: ')
print('-----------------')
print(element)
print('-----------------')

atomic_number = float(input('Atomic #: '))
mass_number = float(input('Mass #: '))
element_amount = float(input('Element Amount (g): '))
g_mol = float(mass_number)
n = float(element_amount / g_mol)
molecules = float(n * 6.023e+23)

# Calculate Molecules
if calculate == 'M':
    print('-----------------')
    print(f"{element} has {molecules} molecules in {element_amount}g")
    print('-----------------')

# Calculate Electrons
elif calculate == 'E':
    print('-----------------')
    electrons = float(molecules * atomic_number)
    print(f"{element} has {electrons} electrons in {element_amount}g")
    print('-----------------')

# Calculate Protons
elif calculate == 'P':
    print('-----------------')
    protons = float(molecules * atomic_number)
    print(f"{element} has {protons} protons in {element_amount}g")
    print('-----------------')

# Calculate Neutrons
elif calculate == 'N':
    print('-----------------')
    neutrons_initial = float(mass_number - atomic_number)
    neutrons_final = float(molecules * neutrons_initial)
    print(f"{element} has {neutrons_final} neutrons in {element_amount}g")
    print('-----------------')

# Help Function
elif calculate == 'Help':
    print('-----------------')
    print('M = Molecules')
    print('E = Electrons')
    print('P = Protons')
    print('N = Neutrons')
    print('Re-Run')
    print('-----------------')

# If not Proper Input is Selected
else:
    print('-----------------')
    print('Please Select either M, E, P, N or Help. Try Again')
    print('-----------------')


