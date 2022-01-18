# switch
Documentation for the process of archiving the journal SWITCH published by SJSU's CADRE Laboratory for New Media in SJSU ScholarWorks, SJSU's institutional repository, which uses the bepress Digital Commons platform. The process is intenended to transform the journal into an accessible PDF format with article-level metadata.

A local copy of the journal was created using HTTrack (https://www.httrack.com/). HTTrack collected the site starting from the URL http://switch.sjsu.edu/archive/archives/index.html. This resulted in a directory of HTML files, including a folder which contained most articles that appeared in volumes 1-18. The first stage of the project focuses on those items.

This repository contains Python scripts which were used to process the html files

- rewrite-encoding.py edits the HTML file to reflect the correct text encoding (windows-1252). This addresses issues with diacritics and other special characters that are present on the current production site 
- switch-metadata-engine.py extracts basic metadata from the HTML files
- rewrite-accessible-colors.py simplifies the HTML structure of the files in order to enable the creation of acceessible PDF files. It replaces the nested table structure of the legacy HTML with a simpler structure and new CSS. It also changes the colors of certain elements to ensure sufficient contrast to meet WCAG 2.1 standards. The contrast improvements were made to graphic elements that are shared across the files - there are still contrast issues in individual files due to the use of inline CSS styles unique to individual articles.

After running these scripts on the files, the resulting HTML files were batch-converted into PDF using Adobe Acrobat.



