# Ernesto Rendon

# These libraries import necessary functions
import os
import sys

sys.dont_write_bytecode = True

# Library of keyword Filenames we're looking for, as well as database of every county's FPN code
county_codes = {
    "Charlotte.xml": "273", 
    "Collier.xml": "272", 
    "Hillsborough.xml": "275", 
    "Lee.xml": "271",
    "Manatee.xml": "270", 
    "Orange.xml": "278", 
    "Pasco.xml": "276", 
    "Pinellas.xml": "274",
    "Polk.xml": "277", 
    "Sarasota.xml": "134", 
    "Flagler.xml": "301", 
    "Volusia.xml": "302",
    "Sarasota Observer.xml": "408", 
    "Longboat.xml": "409", 
    "East County.xml": "410"
}

# This function will handle writing of new layout XML file (only containing the layout object) in the new directory, on root of user-provided directory
# Will require the PATH, NAME of matching XML file, and user-provided month, day and year
def layout_file_writer(new_location, county_files, file_month, file_day, file_year):
    
    # Open new file, which will only contain layout notice object
    solo_xml_file = os.path.join(new_location, "fpn_upload_" + county_codes[county_files] + "." + file_year + file_month + file_day + ".xml")
    
    old_county = county_files.rstrip(".xml")

    # Create new file with county code that matches name via dictionary lookup
    new_solo_layout_xml = open(solo_xml_file, "w")
    
    # Write in the notice tag
    new_solo_layout_xml.write("<xml>\n")
    new_solo_layout_xml.write("  <notice>\n")
    new_solo_layout_xml.write("    <subcategory_id>17</subcategory_id>\n")
    new_solo_layout_xml.write("    <date>" + file_month + "/" + file_day + "/" + file_year + "</date>\n")
    new_solo_layout_xml.write("    <text>Business Observer - " + old_county + " " + file_month + "/" + file_day + "/" + file_year + "</text>\n")
    new_solo_layout_xml.write("    <image>" + file_year + "-" + file_month + "-" + file_day + "-" + old_county + ".pdf</image>\n")
    new_solo_layout_xml.write('</notice>\n')
    new_solo_layout_xml.write("</xml>\n")
    
    # Close the solo layout file
    new_solo_layout_xml.close()
    
    # Confirm to user 
    print('New LAYOUT XML file successfully created.')


# This function takes in old XML, and delivers a properly named copy, with the depricated username/password fields removed
def file_writer(old_file, old_location, county_files, file_month, file_day, file_year):
    

    new_file_ALPHA = os.path.join(old_location, "fpn_upload_" + county_codes[county_files] + "." + file_year + file_month + file_day + ".xml")

    # Create new file with county code that matches name via dictionary lookup
    new_file_object = open(new_file_ALPHA, "w")


    # Open existing XML file in READ mode
    old_file_object = open(old_file, "r")
    # Priming read for first line in existing XML file
    old_file_line = old_file_object.readline()

    # While current line is NOT empty
    while old_file_line != '':
    
    	# Removing username and password portion of XML files by ignoring input and not writing to new file
    	# if (old_file_line == '  <username>gulfcoast</username>\n') or (old_file_line == '  <password>legals</password>\n') or (old_file_line == '  <username>ObserverMediaGroup</username>\n'):
    	# 	old_file_line = old_file_object.readline()
    	# 	continue
    		
        # Copy info to NEW XML file, line by line
        new_file_object.write(old_file_line)
        old_file_line = old_file_object.readline()
    
    old_file_object.close()
    new_file_object.close()
    
    # Confirm to user 
    print('New XML file successfully created.\n')


# This function handles checking of files against potential matches and initializes the publication date once per program-run
def file_checker(user_directory):

    file_month = str(raw_input("Please input the month of the publication (MM): "))
    file_day = str(raw_input("Please input the day of the publication (DD): "))
    file_year = str(raw_input("Please input the year of the publication (YYYY): "))
    print
    
    # This tries to find matches for XML files that exist in all dirs and subdirs of user provided directory
    for root, dirnames, files in os.walk(user_directory):
        for county_files in files:
            if county_files in county_codes:
                
                # If any file is a match against the pre-determined naming conventions, trigger a new file in that location, 
                old_XML = os.path.join(root, county_files)

                # Subdirectory that the match was found in
                old_location = old_XML.rstrip(county_files)
                
                # This is the place we'd need to have a choice of whether to use separate or integrated XML PDF layout tags
                
                # IF SEPARATE:

                # Creates new directory at the root-level of user-provided folder 
                tag_dest_folder = os.path.join(user_directory,"layouts")
                if not os.path.exists(tag_dest_folder):
                    os.mkdir(tag_dest_folder)

                # Function will create new XML file with ONLY the layout tag, and place it within the newly created directory
                layout_file_writer(tag_dest_folder, county_files, file_month, file_day, file_year)

                # Function will create copy of old XML file, removing the deprecated username/password tags at top of file
                file_writer(old_XML, old_location, county_files, file_month, file_day, file_year)

# If number of command line arguments is less than or greater than 2, program will quit. 
# Only 1 user-provided CLI argument is necessary for program
def read_args():
    if len(sys.argv) != 2:
        print("ERROR")
        print("Usage: python -m XML_Auto_Tagger_ALPHA [directory]")
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