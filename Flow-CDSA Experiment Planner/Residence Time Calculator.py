#import modules we need
import math
import pandas as pd

#----define the functions used to calculate components---

#a simple calculator for residence time
def tr_calc(reactor_ID, reactor_length, flow_rate):
    #convert reactor volume to cm and work out volume in cm3
    reactor_volume = math.pi * (((reactor_ID/10)/2)**2) * reactor_length
    print(f'Your reactor volume is {reactor_volume} cm3')
    #convert flow rate to mL/min
    flow_rate = flow_rate/1000
    #now units are sorted, get the residence time
    residence_time = reactor_volume / flow_rate
    print(f'The residence time of your reactor is {residence_time} min')
    #convert min to h in case its very big
    print('The residence time of your reactor is ' + str(residence_time/60) + ' h')
    return(residence_time, reactor_volume)

#a simple calculator for reactor length
def rl_calc(residence_time, reactor_ID, flow_rate):
    #convert flow rate to mL/min
    flow_rate = flow_rate/1000
    reactor_volume = residence_time * flow_rate
    print(f'You will need a reactor volume of {reactor_volume} cm3')
    #work out reactor length needed in cm
    reactor_length = reactor_volume / (math.pi * (((reactor_ID/10)/2)**2))
    print(f'You will need a reactor that is {reactor_length} cm long for a residence time of {residence_time} min')
    return(reactor_length, reactor_volume)

#a simple calculator to work our the flow rates of 2 input streams from reactor volume, residence time and flow split
def fr_calc(residence_time, reactor_ID, reactor_length, streamA_flow_ratio):
    streamB_flow_ratio = 100-streamA_flow_ratio
    print(f'Input stream A is {streamA_flow_ratio}% of the combined flow')
    print(f'Input stream B is {streamB_flow_ratio}% of the combined flow')
    #convert reactor volume to cm and work out volume in cm3
    reactor_volume = math.pi * (((reactor_ID/10)/2)**2) * reactor_length
    print(f'Your reactor volume is {reactor_volume} cm3')
    #calculate total flow rate
    total_flow_rate = reactor_volume / residence_time
    print(f'the total flow rate is {total_flow_rate} mL/min')
    #calculate flow rate for A and B
    flow_rate_A = total_flow_rate * (streamA_flow_ratio/100)
    flow_rate_B = total_flow_rate * (streamB_flow_ratio/100)
    print(f'the flow rate for stream A is {flow_rate_A} mL/min.')
    print(f'the flow rate for stream B is {flow_rate_B} mL/min.')
    #convert flow rates to ul/min
    total_flow_rate = total_flow_rate * 1000
    flow_rate_A = flow_rate_A * 1000
    flow_rate_B = flow_rate_B * 1000
    print(f'the total flow rate is {total_flow_rate} uL/min')
    print(f'the flow rate for stream A is {flow_rate_A} uL/min.')
    print(f'the flow rate for stream B is {flow_rate_B} uL/min.')
    return(total_flow_rate, flow_rate_A, flow_rate_B, streamB_flow_ratio, reactor_volume)
    
#a simple calculator for finding the total flow rate from a number of seperate streams
def get_combined_fr(total_streams):
    current_stream = 1
    total_flow_rate = 0
    stream_list = []
    while current_stream <= total_streams:
        current_flow_rate = float(input(f'What is the flow rate of stream {current_stream} in uL/min? '))
        total_flow_rate = total_flow_rate + current_flow_rate
        stream_list.append(current_flow_rate)
        current_stream += 1
    flow_rate_1 = stream_list[0]
    flow_rate_2 = stream_list[1]
    stream1_flow_ratio = (flow_rate_1 / total_flow_rate) * 100
    stream2_flow_ratio = (flow_rate_2 / total_flow_rate) * 100
    return(total_flow_rate, flow_rate_1, flow_rate_2, stream1_flow_ratio, stream2_flow_ratio)

#function to append data to output dataframe
def append_to_dataframe (run_index,residence_time, reactor_volume, reactor_length, reactor_ID, total_flow_rate, streamA_flow_ratio, streamB_flow_ratio, streamA_flow_rate, streamB_flow_rate):
    Output_data['Entry'].append(run_index)
    Output_data['Residence Time (min)'].append(residence_time)
    Output_data['Reactor Volume (mL)'].append(reactor_volume)
    Output_data['Reactor Length (cm)'].append(reactor_length)
    Output_data['Reactor ID (mm)'].append(reactor_ID)
    Output_data['Total Flow Rate (uL/min)'].append(total_flow_rate)
    Output_data['Stream A Flow Ratio (%)'].append(streamA_flow_ratio)
    Output_data['Stream B Flow Ratio (%)'].append(streamB_flow_ratio)
    Output_data['Stream A Flow Rate (uL/min)'].append(streamA_flow_rate)
    Output_data['Stream B Flow Rate (uL/min)'].append(streamB_flow_rate)

#---Do the calculatons---
#prepare dictionary for dataframe output
Output_data = {'Entry':[],
                   'Residence Time (min)':[],
                   'Reactor Volume (mL)':[],
                   'Reactor Length (cm)':[],
                   'Reactor ID (mm)':[],
                   'Total Flow Rate (uL/min)':[],
                   'Stream A Flow Ratio (%)':[],
                   'Stream B Flow Ratio (%)':[],
                   'Stream A Flow Rate (uL/min)':[],
                   'Stream B Flow Rate (uL/min)':[]}
# make it loop-able
new_iteration = True
run_index = 1
while new_iteration == True:
    print(f'run number {run_index}')

    #---find out what to calculate---
    print('What would you like to calculate?')
    to_calc = input("please type 'tr' for residence time, 'rl' for reactor length, and 'fr' for flow rate: ")
    #calculate the desired variable
    if to_calc == 'tr':
        reactor_ID = float(input('What is the inner diameter of your tubing in mm? '))
        reactor_length = float(input('What is the length of your reactor in cm? '))
        total_streams = float(input('How many input streams do you have? '))
        total_flow_rate, streamA_flow_rate, streamB_flow_rate, streamA_flow_ratio, streamB_flow_ratio = get_combined_fr(total_streams)
        print(f'The total flow rate is {total_flow_rate} uL/min')
        residence_time, reactor_volume = tr_calc(reactor_ID, reactor_length, total_flow_rate)
    elif to_calc == 'rl':
        residence_time = float(input('What is the desired residence time in min? '))
        reactor_ID = float(input('What is the inner diameter of your tubing in mm? '))
        total_streams = float(input('How many input streams do you have? '))
        total_flow_rate, streamA_flow_rate, streamB_flow_rate, streamA_flow_ratio, streamB_flow_ratio = get_combined_fr(total_streams)
        reactor_length, reactor_volume = rl_calc(residence_time, reactor_ID, total_flow_rate)
    elif to_calc == 'fr':
        residence_time = float(input('What is the desired residence time in min? '))
        reactor_ID = float(input('What is the inner diameter of your tubing in mm? '))
        reactor_length = float(input('What is the length of your reactor in cm? '))
        streamA_flow_ratio = float(input(f"For two input streams, what % of the total input flow is stream A (as an integer between 0 and 100)? "))
        total_flow_rate, streamA_flow_rate, streamB_flow_rate, streamB_flow_ratio, reactor_volume = fr_calc(residence_time, reactor_ID, reactor_length, streamA_flow_ratio)
    else:
        print('Error, please choose a type of calculation.')
    iterate = input('Would you like to perform another calculation? y or n? ')
    if iterate == 'y':
        #append current run data to output table
        append_to_dataframe (run_index,residence_time, reactor_volume, reactor_length, reactor_ID, total_flow_rate, streamA_flow_ratio, streamB_flow_ratio, streamA_flow_rate, streamB_flow_rate)
        #iterate for the next run
        new_iteration = True
        run_index += 1
    elif iterate == 'n':
        #end iteration of runs
        new_iteration = False
        #append current run data to output table
        append_to_dataframe (run_index,residence_time, reactor_volume, reactor_length, reactor_ID, total_flow_rate, streamA_flow_ratio, streamB_flow_ratio, streamA_flow_rate, streamB_flow_rate)
        #output data to excel sheet
        print(Output_data)
        Output_dataframe = pd.DataFrame(Output_data, index=[Output_data['Entry']])
        fname = input('What would you like to call the results file? (Do not add .xslx) ')
        Output_dataframe.to_excel(f'{fname}.xlsx', sheet_name='Flow Runs Planned')
        print('Thanks for using the flow chemistry calculator. Have a FABULOUS day, and remember to always GO WITH THE FLOW!')
    else:
        print('Error, please choose if you want to continue by pressing \'y\' or \'n\'.')
        


#optimize excel sheet to look cool - auto sized headings? remove column A

#future ideas
#add productivity, min / max volumes, concentration, reynolds number, solvents etc
#add volume of reagent required and run time - add these detals to a second 'experiment design' sheet that has the total amount of unimer solution needed, etc.