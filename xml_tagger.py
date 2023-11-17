# Ernesto Rendon

# These libraries import necessary functions
import os
import sys

# Counties paired with their respective information
county_codes = {
    "Manatee.xml" :{
        "ID" : "270",
        "username": "BusObsMan",
        "password" : "qgcU8a8D"
    },

    "Lee.xml" :{
        "ID" : "271",
        "username": "BusObsLee",
        "password" : "4H2bMjVM"
    },

    "Collier.xml" :{
        "ID" : "272",
        "username": "BusObsCol",
        "password" : "98m2HmbM"
    },

    "Charlotte.xml" :{
        "ID" : "273",
        "username": "BusObsCha",
        "password" : "5KupMNm5"
    },

    "Pinellas.xml" :{
        "ID" : "274",
        "username": "BusObsPin",
        "password" : "7wh4FSpA"
    },

    "Hillsborough.xml" :{
        "ID" : "275",
        "username": "BusObsHil",
        "password" : "fRAZc293"
    },

    "Pasco.xml" :{
        "ID" : "276",
        "username": "BusObsPas",
        "password" : "5NG6kCYy"
    },

    "Polk.xml" :{
        "ID" : "277",
        "username": "BusObsPol",
        "password" : "8UkG6R3n"
    },

    "Orange.xml" :{
        "ID" : "278",
        "username": "BusObsOra",
        "password" : "eMzH2V92"
    },

    "Volusia.xml" :{
        "ID" : "329",
        "username": "O1omAoDh",
        "password" : "Wjjq4ygU"
    },

    "Flagler.xml" :{
        "ID" : "330",
        "username": "kVMopEwF",
        "password" : "YGtp3LNH"
    },

    "Sarasota.xml" : {
        "ID" : "134",
        "username": "gulfcoast",
        "password" : "busleagals"
    },
}

# This function takes in old XML, and delivers a properly named copy, with respective username/password and respective display ad XML tag at the end
def file_writer(old_file, old_location, county_file, file_month, file_day, file_year):
    
    county_name = county_file.rstrip(".xml")

    new_file_ALPHA = os.path.join(old_location, "fpn_upload_" + county_codes[county_file]["ID"] + "." + file_year + file_month + file_day + ".xml")

    # Create new file with county code that matches name via dictionary lookup
    new_file_object = open(new_file_ALPHA, "w")


    # Open existing XML file in READ mode
    old_file_object = open(old_file, "r")
    # Priming read for first line in existing XML file
    old_file_line = old_file_object.readline()

    # While current line is NOT empty
    while old_file_line != '':

        # If its reached the end of text ad notices, append the display ad PDF notice
        if ("</xml>" in old_file_line):
            new_file_object.write("  <notice>\n")
            new_file_object.write("    <subcategory_id>17</subcategory_id>\n")
            new_file_object.write("    <date>" + file_month + "/" + file_day + "/" + file_year + "</date>\n")
            new_file_object.write("    <text>Business Observer - " + county_name + " " + file_month + "/" + file_day + "/" + file_year + "</text>\n")
            new_file_object.write("    <image>" + file_year + "-" + file_month + "-" + file_day + "-" + county_name + ".pdf</image>\n")
            new_file_object.write('</notice>\n')

        # Typically, default username is "gulfcoast"...
        elif (("<username>gulfcoast</username>" in old_file_line)):
            new_file_object.write("<username>" + county_codes[county_file]["username"] + "</username>\n")
            old_file_line = old_file_object.readline()
            continue

        # Typically, default password is "legals"...
        elif ("<password>legals</password>" in old_file_line):
            new_file_object.write("<password>" + county_codes[county_file]["password"] + "</password>\n")
            old_file_line = old_file_object.readline()
            continue

        # Some files default for some reason is ObserverMediaGroup, and those files also don't have a password line in the OG XML
        elif ("<username>ObserverMediaGroup</username>" in old_file_line):
            new_file_object.write("<username>" + county_codes[county_file]["username"] + "</username>\n")
            new_file_object.write("<password>" + county_codes[county_file]["password"] + "</password>\n")
            old_file_line = old_file_object.readline()
            continue

        # Otherwise, copy info to NEW XML file, line by line
        new_file_object.write(old_file_line)
        old_file_line = old_file_object.readline()

    old_file_object.close()
    new_file_object.close()
    
    # Confirm to user 
    print('New XML file successfully created.')


# This function handles checking of files against potential matches and initializes the publication date once per program-run
def file_checker(user_directory):

    file_month = str(raw_input("Please input the month of the publication (MM): "))
    file_day = str(raw_input("Please input the day of the publication (DD): "))
    file_year = str(raw_input("Please input the year of the publication (YYYY): "))
    print
    
    # This tries to find matches for XML files that exist in all dirs and subdirs of user provided directory
    for root, dirnames, files in os.walk(user_directory):
        for county_file in files:
            if county_file in county_codes:
                
                # If any file is a match against the pre-determined naming conventions, trigger a new file in that location, 
                old_XML = os.path.join(root, county_file)

                # Subdirectory that the match was found in
                old_location = old_XML.rstrip(county_file)

                # Function will create copy of old XML file, removing the deprecated username/password tags at top of file
                file_writer(old_XML, old_location, county_file, file_month, file_day, file_year)

# If number of command line arguments is less than or greater than 2, program will quit. 
# Only 1 user-provided CLI argument is necessary for program
def read_args():
    if len(sys.argv) != 2:
        print("ERROR")
        print("Usage: python xml_tagger.py [directory]")
        exit()
    else:
        return {
            "live_directory": sys.argv[1]
        }

# Main function will call necessary subfunctions
def main():
    # sys.argv is a type LIST that stores input from terminal as soon as program is called in the first place
    # can be used to give program a directory to work in as soon as it's called 
    user_directory = read_args()
    if len(user_directory) == 1:
        print(str(len(user_directory)) + " directory argument detected.")
    else:
        print("Unknown error...")
        exit()    

    # Calling function that will start checking files against matches
    file_checker(user_directory["live_directory"])
    
# Start program by calling main function
main()