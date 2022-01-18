import os
directory = os.path.expanduser('~/Desktop/front test')





for file in os.listdir(directory):
    doc=open(os.path.join(directory,file),'r')
    filedata = doc.read()
    # Replace the target string
    filedata = filedata.replace('UTF-8', 'windows-1252').replace('iso-8859-1', 'windows-1252')
    # Write the file out again
    with open(os.path.join(directory,file), 'w') as file:
        file.write(filedata)
