#import modules we need
import math
import pandas as pd
from UliPlot.XLSX import auto_adjust_xlsx_column_width

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
def append_to_dataframe (run_index,residence_time, reactor_volume, reactor_length, reactor_ID, total_flow_rate, streamA_flow_ratio, streamB_flow_ratio, streamA_flow_rate, streamB_flow_rate, streamA_min_vol, streamB_min_vol):
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
    Output_data['Stream A Min. Volume Needed (mL)'].append(streamA_min_vol)
    Output_data['Stream B Min. Volume Needed (mL)'].append(streamB_min_vol)

#calculate min volume needed for each solution
def calc_min_vol (residence_time, streamA_flow_rate, streamB_flow_rate):
    streamA_min_vol = streamA_flow_rate * residence_time
    streamB_min_vol = streamB_flow_rate * residence_time
    #convert uL to mL
    streamA_min_vol = streamA_min_vol / 1000
    streamB_min_vol = streamB_min_vol / 1000
    return(streamA_min_vol, streamB_min_vol)

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
               'Stream B Flow Rate (uL/min)':[],
               'Stream A Min. Volume Needed (mL)':[],
               'Stream B Min. Volume Needed (mL)':[]}
                   
# make it loop-able
new_iteration = True
run_index = 1
change_single_variable = False
while new_iteration == True:
    print(f'run number {run_index}')
    #change single variable or multiple
    if change_single_variable == True:
        #find and change one variable
        print("Which variable would you like to change?")
        print('N.B. this will assume you are calculating the same parameter as before, ie you want to calculate the flow rate based on a new residence time')
        variable_to_change = input("please type 'tr' for residence time, 'rl' for reactor length, and 'fr' for flow rate: ")
        if variable_to_change == 'tr':
            residence_time = float(input('What is the desired residence time in min? '))
            if to_calc == 'rl':
                reactor_length, reactor_volume = rl_calc(residence_time, reactor_ID, total_flow_rate)
                streamA_min_vol, streamB_min_vol = calc_min_vol (residence_time, streamA_flow_rate, streamB_flow_rate)
            elif to_calc == 'fr':
                total_flow_rate, streamA_flow_rate, streamB_flow_rate, streamB_flow_ratio, reactor_volume = fr_calc(residence_time, reactor_ID, reactor_length, streamA_flow_ratio)
                streamA_min_vol, streamB_min_vol = calc_min_vol (residence_time, streamA_flow_rate, streamB_flow_rate)
        elif variable_to_change == 'rl':
            reactor_length = float(input('What is the length of your reactor in cm? '))
            if to_calc == 'tr':
                residence_time, reactor_volume = tr_calc(reactor_ID, reactor_length, total_flow_rate)
                streamA_min_vol, streamB_min_vol = calc_min_vol (residence_time, streamA_flow_rate, streamB_flow_rate)
            elif to_calc == 'fr':
                total_flow_rate, streamA_flow_rate, streamB_flow_rate, streamB_flow_ratio, reactor_volume = fr_calc(residence_time, reactor_ID, reactor_length, streamA_flow_ratio)
                streamA_min_vol, streamB_min_vol = calc_min_vol (residence_time, streamA_flow_rate, streamB_flow_rate)                
        elif variable_to_change == 'fr':
            total_streams = float(input('How many input streams do you have? '))
            total_flow_rate, streamA_flow_rate, streamB_flow_rate, streamA_flow_ratio, streamB_flow_ratio = get_combined_fr(total_streams)
            if to_calc == 'tr':
                residence_time, reactor_volume = tr_calc(reactor_ID, reactor_length, total_flow_rate)
                streamA_min_vol, streamB_min_vol = calc_min_vol (residence_time, streamA_flow_rate, streamB_flow_rate)
            elif to_calc == 'rl':
                reactor_length, reactor_volume = rl_calc(residence_time, reactor_ID, total_flow_rate)
                streamA_min_vol, streamB_min_vol = calc_min_vol (residence_time, streamA_flow_rate, streamB_flow_rate)
        else:
            print('Error, please choose a variable to change.')
    elif change_single_variable == False:
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
            #calculate min volumes needed for each stream
            streamA_min_vol, streamB_min_vol = calc_min_vol (residence_time, streamA_flow_rate, streamB_flow_rate)
        elif to_calc == 'rl':
            residence_time = float(input('What is the desired residence time in min? '))
            reactor_ID = float(input('What is the inner diameter of your tubing in mm? '))
            total_streams = float(input('How many input streams do you have? '))
            total_flow_rate, streamA_flow_rate, streamB_flow_rate, streamA_flow_ratio, streamB_flow_ratio = get_combined_fr(total_streams)
            reactor_length, reactor_volume = rl_calc(residence_time, reactor_ID, total_flow_rate)
            #calculate min volumes needed for each stream
            streamA_min_vol, streamB_min_vol = calc_min_vol (residence_time, streamA_flow_rate, streamB_flow_rate)
        elif to_calc == 'fr':
            residence_time = float(input('What is the desired residence time in min? '))
            reactor_ID = float(input('What is the inner diameter of your tubing in mm? '))
            reactor_length = float(input('What is the length of your reactor in cm? '))
            streamA_flow_ratio = float(input(f"For two input streams, what % of the total input flow is stream A (as an integer between 0 and 100)? "))
            total_flow_rate, streamA_flow_rate, streamB_flow_rate, streamB_flow_ratio, reactor_volume = fr_calc(residence_time, reactor_ID, reactor_length, streamA_flow_ratio)
            #calculate min volumes needed for each stream
            streamA_min_vol, streamB_min_vol = calc_min_vol (residence_time, streamA_flow_rate, streamB_flow_rate)
        else:
            print('Error, please choose a type of calculation.')
    iterate = input('Would you like to perform another calculation? y or n? ')
    if iterate == 'y':
        #append current run data to output table
        append_to_dataframe (run_index,residence_time, reactor_volume, reactor_length, reactor_ID, total_flow_rate, streamA_flow_ratio, streamB_flow_ratio, streamA_flow_rate, streamB_flow_rate, streamA_min_vol, streamB_min_vol)
        #ask if they want to vary 1 parameter or many
        print("Would you like to change one variable, or multiple?")
        single_variable_next = input("Press 'y' to change one variable, and 'n' to change multiple variables. ")
        if single_variable_next == 'y':
            change_single_variable = True
        #iterate for the next run
        new_iteration = True
        run_index += 1
    elif iterate == 'n':
        #end iteration of runs
        new_iteration = False
        #append current run data to output table
        append_to_dataframe (run_index,residence_time, reactor_volume, reactor_length, reactor_ID, total_flow_rate, streamA_flow_ratio, streamB_flow_ratio, streamA_flow_rate, streamB_flow_rate, streamA_min_vol, streamB_min_vol)
        Output_dataframe = pd.DataFrame(Output_data, index=[Output_data['Entry']])
        
        #---create summary sheet---
        #calculate volume of solutions needed
        streamA_total_vol = sum(Output_data['Stream A Min. Volume Needed (mL)'])
        streamB_total_vol = sum(Output_data['Stream B Min. Volume Needed (mL)'])
        #create second dataframe for summary data
        #create dictionary for second dataframe
        summary_data = {'Total volume of stream A needed (mL)':[],
                        'Total volume of stream B needed (mL)':[]}
        #append data to dictionary
        summary_data['Total volume of stream A needed (mL)'].append(streamA_total_vol)
        summary_data['Total volume of stream B needed (mL)'].append(streamB_total_vol)
        summary_dataframe = pd.DataFrame(summary_data)
        #transpose summary data so is 2 columns
        summary_dataframe = summary_dataframe.T
               
        #output data to excel sheet
        fname = input('What would you like to call the results file? (Do not add .xslx) ')
        #create excel workbook
        with pd.ExcelWriter(f'{fname}.xlsx') as writer:
            Output_dataframe.to_excel(writer, sheet_name='Flow Runs Planned')
            summary_dataframe.to_excel(writer, sheet_name='Summary Data')
            #auto adjust column widths
            auto_adjust_xlsx_column_width(Output_dataframe, writer, sheet_name='Flow Runs Planned', margin=0)
            auto_adjust_xlsx_column_width(summary_dataframe, writer, sheet_name='Summary Data', margin=0)
        #all done!
        #print(Output_data)
        print(summary_data)
        print('Thanks for using the flow chemistry calculator. Have a FABULOUS day, and remember to always GO WITH THE FLOW!')
    else:
        print('Error, please choose if you want to continue by pressing \'y\' or \'n\'.')
        

#add reccommended volumes and recommended total to sheet
#add in what is your solvent, and concentrations, and add in productivity and amounts needed, etc
#add in reynolds number if possible
#optimize excel sheet to look cool - remove column A

#future ideas
#add productivity, min / max volumes, concentration, reynolds number, solvents etc
#add volume of reagent required and run time - add these detals to a second 'experiment design' sheet that has the total amount of unimer solution needed, etc.