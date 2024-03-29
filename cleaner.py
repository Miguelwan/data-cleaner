import numpy as np
import pandas as pd
from datetime import datetime


######################################################################################################



                ####################
                #                  #
                # LOAD EXPORT MENU #
                #                  #
                ####################


def load_export_menu(dataset):

    print()
    print("         ##########################")
    print("         ##                      ##")
    print("         ##  LOAD - EXPORT MENU  ##")
    print("         ##                      ##")
    print("         ##########################")


    exit_variable=0

    while exit_variable==0:
        print()
        print("What would you like to do :")
        print()
        print("1) Load a dataset.")
        print("2) Export the dataset.")
        print("0) Return to Main Menu.")
        load_export_choice=input("Enter your choice: ")

        if load_export_choice=="1":
            continue_load=input("Remember to export your dataset before loading a new one, would you like to proceed with the loading (y/n)? ")
            if continue_load=="y":
                dataset=load_dataset(int(load_export_choice)).copy()

        elif load_export_choice=="2":
            export_dataset(dataset)

        elif load_export_choice=="0":
            exit_variable=1

        else:
            print()
            print("Please enter a valid choice.")

    return dataset


######################################################################################################



                #########################
                #                       #
                # LOAD DATASET FUNCTION #
                #                       #
                #########################


def load_dataset (message_indicator):

    if message_indicator==0:
        print()
        print("Since there is no dataset loaded, the export option is not avaliable.")
    print()
    print("To load a dataset please answer the following questions.")
    extension=input("Enter the extension of your dataset (csv, xlsx): ")
    name_file=input("Enter the name of your file (without extension): ")
    if extension=="csv":
        name_file=name_file + ".csv"
        separ=input("Enter the separation symbol of your data: ")
        df_to_clean = pd.read_csv(name_file, sep=separ)

    elif extension=="xlsx":
        name_file=name_file + ".xlsx"
        name_sheet=input("Enter the name of the sheet: ")
        df_to_clean = pd.read_excel(name_file, sheet_name=name_sheet)

    else:
        print()
        print("The extension", extension, "is not supported.")
        print()

        no_data_loaded = {'Error_message': ['No dataset loaded']}
        df_to_clean = pd.DataFrame(no_data_loaded)

        print("No dataset was loaded")

        return df_to_clean


    print()
    print("The dataset has been loaded.")

    return df_to_clean


######################################################################################################



                ###########################
                #                         #
                # EXPORT DATASET FUNCTION #
                #                         #
                ###########################


def export_dataset (df_to_export):

    print()
    extension_file=input("Enter the extension you would like to use to export the dataset (csv, xlsx): ")
    if extension_file=="csv":
        name_export_file=input("Enter the name for the new file: ")
        name_export_file=name_export_file + ".csv"
        df_to_export.to_csv(name_export_file, index = False)

    elif extension_file=="xlsx":
        name_export_file=input("Enter the name for the new file: ")
        name_export_file=name_export_file + ".xlsx"
        df_to_export.to_excel(name_export_file, index = False)

    print()
    print("The dataset was exported.")

    return ()


######################################################################################################



                ############################
                #                          #
                # INFORMATION DATASET MENU #
                #                          #
                ############################


def info_dataset(df_to_clean):

    print()
    print("         ################################")
    print("         ##                            ##")
    print("         ##  INFORMATION DATASET MENU  ##")
    print("         ##                            ##")
    print("         ################################")


    exit_variable=0

    while exit_variable==0:
        print()
        print("What information would you like to display:")
        print()
        print("1) Name of columns.")
        print("2) Type of the columns.")
        print("3) Amount of entries and missing values of the dataset.")
        print("4) Missing values of the dataset.")
        print("5) Information of a particular colunmn.")
        print("0) Return to Main Menu.")
        print()
        information_choice=input("Enter your choice: ")

        dataset_columns=obtaining_dataset_columns(df_to_clean)

        if information_choice=="1":
            string_to_print="Your dataset contains the following columns:"
            concatenate_name_columns(dataset_columns, string_to_print)

        elif information_choice=="2":
            type_of_columns(df_to_clean, dataset_columns)

        elif information_choice=="3":
            values_information(df_to_clean, dataset_columns)

        elif information_choice=="4":
            missing_values_visualization(df_to_clean, dataset_columns)

        elif information_choice=="5":
            print()
            column_to_explore=input("Please enter the name of the column you want to see the information: ")
            if column_to_explore not in dataset_columns:
                print(column_to_explore, "is not a column of the dataset, please check that the correct dataset was loaded.")
                print()
            else:
                column_information(df_to_clean, column_to_explore)

        elif information_choice=="0":
            exit_variable=1

        else:
            print()
            print("Please enter a valid choice.")

    return ()


######################################################################################################



                ############################
                #                          #
                # DATASET COLUMNS FUNCTION #
                #                          #
                ############################


def obtaining_dataset_columns(dataset):

    data_columns=dataset.columns

    return data_columns


######################################################################################################



                ########################
                #                      #
                # CONCATENATE FUNCTION #
                #                      #
                ########################


def concatenate_name_columns(set_to_concatenate, string_to_print):

    print()
    concatenated_string=string_to_print
    counter=0
    space=" "
    for word_to_add in set_to_concatenate:
        if counter==1:
            space=", "
        concatenated_string=concatenated_string + space + word_to_add
        counter=1
    print(concatenated_string+".")
    print()

    return ()


######################################################################################################



                #################
                #               #
                # TYPE FUNCTION #
                #               #
                #################


def type_of_columns(dataset, data_columns):

    print()
    for column in data_columns:
        print("The column", column, "has type", dataset.dtypes[column], "in its entries.")
        print()

    return ()


######################################################################################################



                ###############################
                #                             #
                # VALUES INFORMATION FUNCTION #
                #                             #
                ###############################


def values_information(dataset, data_columns):

    print()
    missing_data_counter=0
    for column in data_columns:
        missing_data_counter=missing_data_counter+len(dataset[dataset[column].isnull()])
        print("The column", column, "has", len(dataset[column])-
            len(dataset[dataset[column].isnull()]), "values and",
            len(dataset[dataset[column].isnull()]), "missing values.")
        print()
    print("The dataset contains a total of", missing_data_counter, "missing values.")

    return()


######################################################################################################



                ###################################
                #                                 #
                # MISSING VALUES DISPLAY FUNCTION #
                #                                 #
                ###################################


def missing_values_visualization(dataset, data_columns):

    print()
    print("The missing values are in the rows: ")
    for column in data_columns:
        if len(dataset[dataset[column].isnull()])>0:
            print(dataset[dataset[column].isnull()])
    print()

    return()


######################################################################################################



                #######################################
                #                                     #
                # COLUMN INFORMATION DISPLAY FUNCTION #
                #                                     #
                #######################################


def column_information(dataset, column_to_explore):

    print()
    print("The column", column_to_explore, "has type", dataset.dtypes[column_to_explore], "in its entries.")
    print()
    print("The column", column_to_explore, "has", len(dataset[column_to_explore])-
            len(dataset[dataset[column_to_explore].isnull()]), "values and",
            len(dataset[dataset[column_to_explore].isnull()]), "missing values.")
    print()
    if len(dataset[dataset[column_to_explore].isnull()])>0:
        print()
        print("The following rows contain missing values in the column"+ column_to_explore +":" )
        print(dataset[dataset[column_to_explore].isnull()])
        print()

    input_display_choice=input("Would you like to see information about the inputs of the column "+ column_to_explore +" (y/n)? ")
    if input_display_choice=="y":
        input_display_menu(dataset, column_to_explore)


    return()


######################################################################################################



                ######################
                #                    #
                # INPUT DISPLAY MENU #
                #                    #
                ######################


def input_display_menu(dataset, column_to_explore):

    print()
    print("         ##########################")
    print("         ##                      ##")
    print("         ##  INPUT DISPLAY MENU  ##")
    print("         ##                      ##")
    print("         ##########################")


    exit_variable=0

    while exit_variable==0:
        print()
        print("What input information would you like to display :")
        print()
        print("1) Characters in the entries of "+column_to_explore+".")
        print("2) Information about an specific character in "+column_to_explore+".")
        print("3) Information about an entry in "+column_to_explore+".")
        print("0) Return to Main Menu.")
        load_information_choice=input("Enter your choice: ")

        if load_information_choice=="1":
            print()
            print("This might take some time.")

            set_of_entries=input_set_calculation(dataset, column_to_explore, 0, len(dataset[column_to_explore]))

            print()
            print("The column", column_to_explore, "has the following characters in its entries:")
            print(set_of_entries)
            print()
            Latin_alphabet_and_numbers={"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
                        "R","S","T","U","V","W","X","Y","Z","a","b","c","d",
                        "e","f","g","h","i","j","k","l","m","n","o","p","q",
                        "r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"}
            print("The column", column_to_explore, "has the following special characters (not numbers, neither a letter in the latin alphabet:)")
            print(set_of_entries-Latin_alphabet_and_numbers)


        elif load_information_choice=="2":
            print()
            found_entries, set_found_entries, token_to_search=input_character_calculation(dataset, column_to_explore, 0, len(dataset[column_to_explore]))

            print("There are", len(found_entries), "entries with '"+token_to_search+"'.")
            print()
            print("There are", len(set_found_entries), "unique entries with'"+token_to_search+"'.")

            display_all_unique_entries=input("Would you like to display the unique entries (y/n)? ")
            if display_all_unique_entries=="y":
                string_to_print="The character "+token_to_search+" is in the following entries: "
                concatenate_name_columns(set_found_entries, string_to_print)


        elif load_information_choice=="3":
            print()
            found_entries, token_to_search=input_string_calculation(dataset, column_to_explore, 0, len(dataset[column_to_explore]))

            print("There are", len(found_entries), "entries equal to '"+token_to_search+"'.")


        elif load_information_choice=="0":
            exit_variable=1


        else:
            print()
            print("Please enter a valid choice.")

    return ()


######################################################################################################



                ##################################
                #                                #
                # SET INPUT CALCULATION FUNCTION #
                #                                #
                ##################################


def input_set_calculation(dataset, column_to_explore, lower_bound, upper_bound):

    set_of_entries = set()
    for temporal_entry in set(dataset[column_to_explore][lower_bound:upper_bound]):
        set_of_entries=set_of_entries.union(set(str(temporal_entry)))

    return (set_of_entries)


######################################################################################################



                ########################################
                #                                      #
                # INPUT CHARACTER CALCULATION FUNCTION #
                #                                      #
                ########################################


def input_character_calculation(dataset, column_to_explore, lower_bound, upper_bound):

    found_words=[]
    token_to_search=input("Please enter the character you would like to find: ")

    for temporal_entry in dataset[column_to_explore][lower_bound:upper_bound]:
        if token_to_search in set(str(temporal_entry)):
            found_words.append(str(temporal_entry))

    set_found_words=set(found_words)

    return found_words, set_found_words, token_to_search


######################################################################################################



                ####################################
                #                                  #
                # INPUT ENTRY CALCULATION FUNCTION #
                #                                  #
                ####################################


def input_string_calculation(dataset, column_to_explore, lower_bound, upper_bound):

    found_words=[]
    token_to_search=input("Please enter the entry you would like to find: ")

    for temporal_entry in dataset[column_to_explore][lower_bound:upper_bound]:
        if token_to_search == str(temporal_entry):
            found_words.append(str(temporal_entry))

    return found_words, token_to_search


######################################################################################################



                ########################
                #                      #
                # DISPLAY DATASET MENU #
                #                      #
                ########################


def display_dataset_menu (dataset):

    print()
    print("         ############################")
    print("         ##                        ##")
    print("         ##  DISPLAY DATASET MENU  ##")
    print("         ##                        ##")
    print("         ############################")


    exit_variable=0

    while exit_variable==0:
        print()
        print("Which rows would you like to display:")
        print()
        print("1) First n rows.")
        print("2) Last n rows.")
        print("3) Rows by interval.")
        print("4) Rows by input.")
        print("0) Return to Main Menu")
        print()
        visualization_choice=input("Enter your choice: ")

        if visualization_choice=="1":
            print()
            number_to_show=int(input("Enter the number of lines you would like to see: "))
            if number_to_show<1:
                print("Please enter a positive number.")
            else:
                display_dataset(dataset, 0, int(number_to_show))


        elif visualization_choice=="2":
            print()
            number_to_show=int(input("Enter the number of lines you would like to see: "))
            if number_to_show<1:
                print("Please enter a positive number.")
            else:
                display_dataset(dataset, -int(number_to_show), len(dataset))


        elif visualization_choice=="3":
            print()
            lower_bound_to_show=int(input("Enter the first line you would like to see (starting in 1): "))
            upper_bound_to_show=int(input("Enter the last line you would like to see (starting in 1): "))
            if lower_bound_to_show>upper_bound_to_show:
                print()
                print("The visualization cannot be done unless the first line you would like to see is smaller (or equal) than the last line you would like to see.")

            elif lower_bound_to_show<1:
                print("Please enter positive numbers.")

            else:
                lower_bound_to_show=lower_bound_to_show-1
                display_dataset(dataset, lower_bound_to_show, upper_bound_to_show)


        elif visualization_choice=="4":
            print()
            print("To display rows with an specific input, please answer the following questions. Remember that only rows with the same input will be display, e.g. '1' is different to '1.0'")
            print()
            column_to_explore=input("In which column is the input you want to use? ")

            data_columns=obtaining_dataset_columns(dataset)
            if column_to_explore not in data_columns:
                print()
                print(column_to_explore, "is not a column of the dataset.")

            else:
                valid_input=1
                all_thedataset_choice=input("Do you want to display the input over all the dataset (y/n)? ")
                if all_thedataset_choice=="y":
                    lower_bound_to_show=0
                    upper_bound_to_show=len(dataset)

                else:
                    print()
                    print("Please define the subdataset.")
                    lower_bound_to_show=int(input("Enter the first line of the subdataset (starting in 0): "))
                    upper_bound_to_show=int(input("Enter the last line of the subdataset (starting in 1): "))

                    if lower_bound_to_show>=upper_bound_to_show:
                        print()
                        print("The visualization cannot be done unless the first line of the subdataset is smaller than the last line of the subdataset.")
                        valid_input=0

                    elif lower_bound_to_show<0:
                        print("Please enter a non-negative number.")
                        valid_input=0

                if valid_input==1:
                    sub_dataset=sub_dataset_by_input(dataset, column_to_explore, lower_bound_to_show, upper_bound_to_show).copy()
                    display_dataset(sub_dataset, 0, len(sub_dataset))





        elif visualization_choice=="0":
            exit_variable=1


        else:
            print()
            print("Please enter a valid choice.")


######################################################################################################



                ####################
                #                  #
                # DISPLAY FUNCTION #
                #                  #
                ####################


def display_dataset(dataset, lower_bound_to_show, upper_bound_to_show):

    pd.set_option('display.max_rows', None)

    print()
    print(dataset[lower_bound_to_show:upper_bound_to_show])

    return ()


######################################################################################################



                #################################
                #                               #
                # SUB-DATASET BY INPUT FUNCTION #
                #                               #
                #################################


def sub_dataset_by_input(dataset, column_to_explore, lower_bound_to_show, upper_bound_to_show):

    token_to_search=input("Please enter the input you would like use: ")

    sub_dataset=dataset[lower_bound_to_show:upper_bound_to_show].copy()
    initial_type=sub_dataset.dtypes[column_to_explore]

    sub_dataset=change_type_by_column(sub_dataset, column_to_explore, "str")

    sub_dataset=sub_dataset[sub_dataset[column_to_explore]==token_to_search]

    sub_dataset=change_type_by_column(sub_dataset, column_to_explore, initial_type)

    return (sub_dataset)


######################################################################################################



                ################################
                #                              #
                # CHANGE TYPE COLUMN FUNCTION  #
                #                              #
                ################################


def change_type_by_column(dataset, column_to_change, desire_type):

    new_dataset=dataset.copy()
    new_dataset[column_to_change]=new_dataset[column_to_change].astype(desire_type)


    return (new_dataset)


######################################################################################################



                #####################
                #                   #
                # CHANGE TYPES MENU #
                #                   #
                #####################


def change_type_menu (dataset):

    print()
    print("         #########################")
    print("         ##                     ##")
    print("         ##  CHANGE TYPES MENU  ##")
    print("         ##                     ##")
    print("         #########################")


    print()
    data_columns=obtaining_dataset_columns(dataset)

    exit_variable=0

    while exit_variable==0:

        for column in data_columns:
            print("The column ", column, "has type", dataset.dtypes[column])
            print()

        column_to_change=input("To which column would you like to change the type: ")

        if column_to_change not in data_columns:
            print(column_to_change, "is not a column of the dataset.")
            print()
            want_to_leave=input("Would yo like to return to the main menu (y/n)? ")
            if want_to_leave=="y":
                exit_variable=1

        else:

            print()
            print("The column ", column_to_change, "has type", dataset.dtypes[column_to_change])
            print("It can be change to one of the folloowing types:")
            print()
            print("1) object.")
            print("2) int64.")
            print("3) float64.")
            print("4) bool.")
            print("5) datetime64.")
            print("0) return to main menu.")
            print()
            type_choice=input("Enter your choice: ")

            if type_choice=="1":
                dataset=change_type_by_column(dataset, column_to_change, 'object').copy()

            elif type_choice=="2":
                dataset=change_type_by_column(dataset, column_to_change, 'int64').copy()

            elif type_choice=="3":
                dataset=change_type_by_column(dataset, column_to_change, 'float64').copy()

            elif type_choice=="4":
                dataset=change_type_by_column(dataset, column_to_change, 'bool').copy()

            elif type_choice=="5":
                date_time_format=date_time_format_function()

                datetime_fixed=change_date_time_arrange(dataset, column_to_change, date_time_format)
                print("The change is in progress.")
                dataset=exchange_column_dateset(dataset, column_to_change, datetime_fixed, data_columns).copy()
                print()
                print("The change is complete.")

            elif type_choice=="0":
                exit_variable=1

            else:
                print()
                print("Please enter a valid choice.")

    return dataset


######################################################################################################



                #########################
                #                       #
                # DATE FORMAT FUNCTIONS #
                #                       #
                #########################



                ####################
                #                  #
                # WEEKDAY FUNCTION #
                #                  #
                ####################



def weekday_function():

    print("In which format is the weekday:")
    print("1) Weekday as abbreviated name.")
    print("2) Weekday as full name.")
    print("3) Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.")
    week_format=int(input("Enter your choice: "))

    if week_format==1:
        return "%a"
    elif week_format==2:
        return "%A"
    elif week_format==3:
        return "%w"
    else:
        print("That was not a valid choice, the weekday format is set by default to the full name.")
        return "%A"


                #################
                #               #
                # YEAR FUNCTION #
                #               #
                #################



def year_function():

    print("In which format is the year:")
    print("1) Year without century number (00 - 99).")
    print("2) Year with century number (0000 - 9999).")
    year_format=int(input("Enter your choice: "))

    if year_format==1:
        return "%y"
    elif year_format==2:
        return "%Y"
    else:
        print("That was not a valid choice, the year format is set by default with century.")
        return "%Y"


                ##################
                #                #
                # MONTH FUNCTION #
                #                #
                ##################



def month_function():

    print("In which format is the month:")
    print("1) Month as abbreviated name.")
    print("2) Month as full name.")
    print("3) Month as number (01 - 12).")
    month_format=int(input("Enter your choice: "))

    if month_format==1:
        return "%b"
    elif month_format==2:
        return "%B"
    elif month_format==3:
        return "%m"
    else:
        print("That was not a valid choice, the month format is set by default to number of the month.")
        return "%m"


                ################
                #              #
                # DAY FUNCTION #
                #              #
                ################



def daynumber_function():

    print("In which format is the day:")
    print("1) Day of the month (01 - 31).")
    print("2) Day of the year (001 - 366).")
    day_format=int(input("Enter your choice: "))

    if day_format==1:
        return "%d"
    elif day_format==2:
        return "%j"
    else:
        print("That was not a valid choice, the day format is set by default to day of the month.")
        return "%d"


                #################
                #               #
                # HOUR FUNCTION #
                #               #
                #################



def hour_function():

    print("In which format is the hour:")
    print("1) 24-hour clock.")
    print("2) 12-hour clock.")
    hour_format=int(input("Enter your choice: "))

    if hour_format==1:
        return "%H"
    elif hour_format==2:
        return "%I"
    else:
        print("That was not a valid choice, the hour format is set by default to 24-hour.")
        return "%H"


                ######################
                #                    #
                # DATE TIME FUNCTION #
                #                    #
                ######################



def date_time_format_function():

    date_format_complete=0
    dateformat=""
    date_symbols={"Weekday", "Year", "Month", "Day", "Hour", "Minute", "Second", "PM/AM"}
    format_for_user=""
    print("Please indicate the format of the date in the dataset.")
    print()
    while date_format_complete<7:
        message_options=""
        lenght_message=0
        for option_date in date_symbols:
            message_options=message_options+option_date
            lenght_message=lenght_message+1
            if lenght_message!=len(date_symbols):
                message_options=message_options+", "

        if date_format_complete==0:
            local_date_format=input("Which information appears first ("+message_options+")? ")
            if local_date_format == "Weekday":
                interpretator=weekday_function()
            elif local_date_format == "Year":
                interpretator=year_function()
            elif local_date_format == "Month":
                interpretator=month_function()
            elif local_date_format == "Day":
                interpretator=daynumber_function()
            elif local_date_format == "Hour":
                interpretator=hour_function()
            elif local_date_format == "Minute":
                interpretator="%M"
            elif local_date_format == "Second":
                interpretator="%S"
            elif local_date_format == "PM/AM":
                interpretator="%p"
            else:
                break

        else:
            local_date_format=input("What appears next ("+message_options+")? ")
            if local_date_format == "Weekday":
                interpretator=weekday_function()
            elif local_date_format == "Year":
                interpretator=year_function()
            elif local_date_format == "Month":
                interpretator=month_function()
            elif local_date_format == "Day":
                interpretator=daynumber_function()
            elif local_date_format == "Hour":
                interpretator=hour_function()
            elif local_date_format == "Minute":
                interpretator="%M"
            elif local_date_format == "Second":
                interpretator="%S"
            elif local_date_format == "PM/AM":
                interpretator="%p"
            else:
                break

        format_for_user=format_for_user+local_date_format
        dateformat=dateformat+interpretator


        if date_format_complete<6:
            is_format_complete=input("Is the format equal to '"+format_for_user+"' (y/n)? ")
            if is_format_complete=="y":
                break
            else:
                separator_date_format=input("What separator appears next (:, -, /, etc)? ")
                dateformat=dateformat+separator_date_format
                format_for_user=format_for_user+separator_date_format

        date_format_complete=date_format_complete+1
        date_symbols=date_symbols-{local_date_format}

    return dateformat


######################################################################################################



                ##############################
                #                            #
                # CHANGE DATE TIME FUNCTION  #
                #                            #
                ##############################


def change_date_time_arrange(dataset, column_to_change, date_time_format):

    datetime_fixed=[]

    for date_time_to_fix in dataset[column_to_change]:
        datetime_fixed.append(datetime.strptime(date_time_to_fix, date_time_format))


    return (datetime_fixed)


######################################################################################################



                #############################
                #                           #
                # EXCHANGE COLUMN FUNCTION  #
                #                           #
                #############################


def exchange_column_dateset(dataset, column_to_change, new_arrange_column, data_columns):

    df_new_data=pd.DataFrame(columns=data_columns)
    for column in data_columns:
        if column==column_to_change:
            df_new_data[column]=new_arrange_column
        else:
            df_new_data[column]=dataset[column]

    return df_new_data


######################################################################################################



                ##########################
                #                        #
                # CHANGING ENCODING MENU #
                #                        #
                ##########################


def changing_encoding_menu(dataset):

    print()
    print("         ##############################")
    print("         ##                          ##")
    print("         ##  CHANGING ENCODING MENU  ##")
    print("         ##                          ##")
    print("         ##############################")


    exit_variable=0

    while exit_variable==0:
        print()
        continue_encoding=input("Only the encoding of strings can be modified, would you like to proceed to re-encode a column (y/n)? ")
        if continue_encoding=="y":
            dataset=encoding_function(dataset).copy()

        leave_answer=input("Would you like to return to the main menu (y/n)? ")
        if leave_answer=="y":
            exit_variable=1

    return dataset


######################################################################################################



                ##############################
                #                            #
                # CHANGING ENCODING FUNCTION #
                #                            #
                ##############################


def encoding_function (dataset):

    print()
    data_columns=obtaining_dataset_columns(dataset)

    example_word=input("Please enter an example word of the error (case-sensitive): ")
    example_word_right=input("Please enter the example word correctly written (case-sensitive): ")

    encoding_samples(example_word, example_word_right)

    print()

    print("Please choose the right endocing and decoding from the previous list.")

    encoding=input("Enter encoding: ")
    decoding=input("Enter decoding: ")
    column_error=input("Enter the column with the encoding error: ")

    no_typo_entry=new_encoding_of_words(dataset, column_error, encoding, decoding)

    df_no_typos=exchange_column_dateset(dataset, column_error, no_typo_entry, data_columns).copy()

    print()
    print("The columns", column_error, "of the dataset has  been modified.")
    print("No other column was modified. You can modify other column or return to the main menu.")
    print()

    return df_no_typos


######################################################################################################



                ###############################
                #                             #
                # SAMPLE OF ENCODING FUNCTION #
                #                             #
                ###############################


def encoding_samples(example_word, example_word_right):

    codecs_options=["ascii", "big5", "big5hkscs", "cp037", "cp273", "cp424", "cp437",
                    "cp500", "cp720", "cp737", "cp775", "cp850", "cp852", "cp855", "cp856",
                    "cp857", "cp858", "cp860", "cp861", "cp862", "cp863", "cp864", "cp865", "cp866",
                    "cp869", "cp874", "cp875", "cp932", "cp949", "cp950", "cp1006", "cp1026", "cp1125",
                    "cp1140", "cp1250", "cp1251", "cp1252", "cp1253", "cp1254", "cp1255", "cp1256", "cp1257",
                    "cp1258", "euc_jp", "euc_jis_2004", "euc_jisx0213", "euc_kr", "gb2312", "gbk", "gb18030", "hz",
                    "iso2022_jp", "iso2022_jp_1", "iso2022_jp_2", "iso2022_jp_2004", "iso2022_jp_3", "iso2022_jp_ext",
                    "iso2022_kr", "latin_1", "iso8859_2", "iso8859_3", "iso8859_4", "iso8859_5", "iso8859_6",
                    "iso8859_7", "iso8859_8", "iso8859_9", "iso8859_10", "iso8859_11", "iso8859_13", "iso8859_14",
                    "iso8859_15", "iso8859_16", "johab", "koi8_r", "koi8_t", "koi8_u", "kz1048", "mac_cyrillic",
                    "mac_greek", "mac_iceland", "mac_latin2", "mac_roman", "mac_turkish", "ptcp154", "shift_jis",
                    "shift_jis_2004", "shift_jisx0213", "utf_32", "utf_32_be", "utf_32_le", "utf_16", "utf_16_be",
                    "utf_16_le", "utf_7", "utf_8", "utf_8_sig", "unicode_escape"]

    print()
    for option_1 in codecs_options:
        for option_2 in codecs_options:
            new_example_word=example_word.encode(option_1, 'ignore')
            new_encoding_word=new_example_word.decode(option_2, 'ignore')
            if new_encoding_word==example_word_right:
                print("The following codecs write the example word correct. Encoding = ",
                        option_1, ", decoding =", option_2, ", example word = ", new_encoding_word)
                print()

    return ()


######################################################################################################



                ##########################
                #                        #
                # RE - ENCODING FUNCTION #
                #                        #
                ##########################


def new_encoding_of_words(dataset, column_error, encoding, decoding):

    no_typo_entry=[]
    for entry_element in range(len(dataset[column_error])):
        entry_typo=dataset[column_error][entry_element]

        if type(entry_typo)==str:
            newstr=entry_typo.encode(encoding, 'ignore')
            entry_clean=newstr.decode(decoding, 'ignore')

        else:
            entry_clean=entry_typo

        no_typo_entry.append(entry_clean)

    return (no_typo_entry)


######################################################################################################



                #############
                #           #
                # MAIN MENU #
                #           #
                #############


while running_variable!=0:
    print()
    print("         #################")
    print("         ##             ##")
    print("         ##  MAIN MENU  ##")
    print("         ##             ##")
    print("         #################")

    print()
    print("What would you like to do :")
    print()
    print("1) Load or export a dataset.")
    print("2) Display basic information of the dataset.")
    print("3) Display lines of the dataset.")
    print("4) Change the type of a column.")
    print("5) Fix encoding errors in a column ('Ä' appears as 'Ã„').")
    print("6) Take care of missing data.")
    print("7) Modify data.")
    print("8) Select relevant data.")
    print("9) Help/About.")
    print("0) Exit.")
    print()
    choose_desire=input("Enter your choice: ")

    if choose_desire=="1":
        if dataset_iterated!=0:
            df_to_work=load_export_menu(df_to_work).copy()

        else:
            df_to_work=load_dataset(dataset_iterated).copy()
            dataset_iterated=1

        if df_to_work.columns[0]=='Error_message':
            dataset_iterated=0


    elif choose_desire=="2":
        if dataset_iterated!=0:
            info_dataset(df_to_work)
        else:
            print("No datset is loaded, please load a dataste first.")


    elif choose_desire=="3":
        if dataset_iterated!=0:
            display_dataset_menu(df_to_work)
        else:
            print("No datset is loaded, please load a dataste first.")


    elif choose_desire=="4":
        if dataset_iterated!=0:
            df_to_work=change_type_menu(df_to_work).copy()
        else:
            print("No datset is loaded, please load a dataste first.")


    elif choose_desire=="5":
        print()
        print("To fix encoding errors you must have and example word of the error and how it should appear. You can visualize some rows of the dataset to find examples.")
        have_an_example=input("Do you have an example of the error (y/n)? ")
        if have_an_example=="y":
            if dataset_iterated!=0:
                df_to_work=changing_encoding_menu(df_to_work).copy()
            else:
                print("No datset is loaded, please load a dataste first.")




    elif choose_desire=="0":
        continue_exit=input("Remember to export your dataset, any change made before the last export wont be saved. Do you want to exit (y/n)? ")
        if continue_exit=="y":
            running_variable=0

    else:
        print()
        print("Please enter a valid choice.")
