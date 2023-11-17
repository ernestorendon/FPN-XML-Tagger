
# FPN - XML Tagger

This small Python script sanitizes input .XML files, adding and removing information that is necessary for proper processing and uploading of these public notice files into FloridaPublicNotices.com

Currently, it generates a new folder containing new and separate files that contain only the PDF layout file; but sometimes a system can use a single file to upload individual notices AND the PDF file.

## Overall workflow:

1. First compares filenames located in user_root/directories/subdirs against list of potential matches.
2. If a match is found, then the match is duplicated and manipulated into a new file.
3. This new dupe file is properly named, has its username/password fields removed, and is placed in the same dir as the original match.
   - The new file will have one last additional xml object, which links and uploads a PDF layout to its respective county
4. Repeats from **Step 1** until all potential files have been processed
