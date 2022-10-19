from zipfile import ZipFile
x=input("Enter filename")
file_name = x
with ZipFile(file_name, 'r') as zip:
    zip.printdir()
    print('Extracting')
    zip.extractall()
    print('Done!')
