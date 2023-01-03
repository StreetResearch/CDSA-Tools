print ('what would you like to calculate?')
to_calc = input ('moles, mass, or rmm? ')
if to_calc == 'moles':
    mass = input ('what is the mass of you sample (in g)? ')    
    rmm = input ('what is the molecular weight of your sample? ')
    mass = float (mass)
    rmm = float (rmm)
    moles = mass / rmm
    print ('your sample is ' + str(moles) + ' moles')
elif to_calc == 'mass':
    moles = input('what is the number of moles of your sample? ')
    rmm = input ('what is the molecular weight of your sample? ')
    moles = float (moles)
    rmm = float (rmm)
    mass = moles * rmm
    print ('your sample is ' + str(mass) + ' g')
elif to_calc == 'rmm':
    mass = input ('what is the mass of your sample (in g)? ')
    moles = input ('what is the number of moles of your sample? ')
    mass = float (mass)
    moles = float (moles)
    rmm = mass / moles
    print ('your sample has a molecular weight of ' + str(rmm) + ' g/mol')
else:
    print ("Error: please type either 'moles', 'mass' or 'rmm' ")
print ('thank you for using the molecular weight calculator. Have a nice day =)')
    
    
    