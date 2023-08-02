
# FPN - XML Tagger

This small Python script sanitizes input .XML files, adding and removing information that is necessary for proper processing and uploading of these public notice files into FloridaPublicNotices.com

Currently, it generates a new folder containing new and separate files that contain only the PDF layout file; but sometimes a system can use a single file to upload individual notices AND the PDF file.

## Overall workflow:

1. First compares filenames located in user_root/directories/subdirs against list of potential matches.
2. If a match is found, then the match is duplicated and manipulated into a new file.
3. This new dupe file is properly named, has its username/password fields removed, and is placed in the same dir as the original match.
   - At the same time, another XML file is generated in a new dir on the root of the user-provided folder.
   - This other XML file (solo layout file) has the same proper name as before, but only contains the single layout object 
   - They need to be separated in order to have the same exact name and avoid duplicate name error
4. Repeats from **Step 1** until all potential files have been processed
