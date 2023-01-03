seed_conc = float(input ('what is your seed concentration in mg/mL? '))
seed_vol = float (input ('what is the volume of your seed solution in uL? '))
#convert seed volume to mL
seed_vol = seed_vol / 1000
seed_mass = seed_conc * seed_vol
print ('the mass of polymer in your sample is ' + str(seed_mass) + 'mg of polymer.')
unimer_seed_ratio = float(input ('what is your desired unimer/seed ratio? 1: '))
mass_of_unimer_to_add = seed_mass * unimer_seed_ratio
print ('you need to add ' + str(mass_of_unimer_to_add) + 'mg of unimer')
unimer_solution_concentration = float(input ('what is your unimer solution concentration in mg/mL? '))
unimer_volume_to_add = mass_of_unimer_to_add / unimer_solution_concentration
#convert unimer volume to uL
unimer_volume_to_add = unimer_volume_to_add * 1000
print ('you need to add ' + str(unimer_volume_to_add) + 'uL of your ' + str(unimer_solution_concentration) + 'mg/mL unimer solution to get a u/s ratio of ' + str(unimer_seed_ratio) + '.')
final_mass = seed_mass + mass_of_unimer_to_add
#convert unimer volume to mL
unimer_volume_to_add = unimer_volume_to_add / 1000
final_volume = seed_vol + unimer_volume_to_add
final_concentration = final_mass / final_volume
#convert final volume to uL
final_volume = final_volume * 1000
print ('your final solution concentration is ' + str(final_concentration) + 'mg/mL, your final volume is ' + str(final_volume) + 'uL, and your total mass of polymer is ' + str(final_mass) + 'mg.')
print ('thank you for using the seeded growth calculator. Have a nice day :) ')
