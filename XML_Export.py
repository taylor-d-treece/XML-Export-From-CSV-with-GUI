import csv
from GUI import xml_file_select

file_selected, dest_selected = xml_file_select()

# Function to generate XML with appropriate fields for XML file
def write_xml(image):

    with open(dest_selected + '\\' + image_name[6:14] + '.xml', 'w') as output:
        output.write('<ControlStatements xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance'
                     '" xmlns="http://dev.docuware.com/Jobs/Control">\n')
        output.write('\t<Page>\n')
        output.write('\t\t<Field dbName="Field1" type="Text" value="{}"/>\n'.format(field1))
        output.write('\t\t<Field dbName="Field2" type="Text" value="{}"/>\n'.format(field2))
        output.write('\t\t<Field dbName="Field3" type="Text" value="{}"/>\n'.format(field3))
        output.write('\t\t<Field dbName="Field4" type="Text" value="{}"/>\n'.format(field4))
        output.write('\t\t<Field dbName="Field5" type="Text" value="{}"/>\n'.format(field5))
        output.write('\t\t<Field dbName="Field6" type="Date" value="{}" culture="en-US" format="MMddyyyy"/>\n'.format(field6))
        output.write('\t\t<Field dbName="Field7" type="Text" value="{}"/>\n'.format(field7))
        output.write('\t\t<Field dbName="Field8" type="Text" value="{}"/>\n'.format(field8))
        output.write('\t\t<Field dbName="Field9" type="Text" value="{}"/>\n'.format(field9))
        output.write('\t\t<Field dbName="Field10" type="Text" value="{}"/>\n'.format(field10))
        output.write('\t</Page>\n')
        output.write('</ControlStatements>')

        output.close()


# Open CSV and assign variables, generate XML File for each item in CSV File
with open(file_selected, mode='r') as file:
    csvFile = csv.reader(file)
    my_list = list(csvFile)
    for i in range(len(my_list)):
        field1 = my_list[i][0]
        field2 = my_list[i][1]
        field3 = my_list[i][2]
        field4 = my_list[i][3]
        field5 = my_list[i][4]
        field6 = my_list[i][5]
        field7 = my_list[i][6]
        field8 = my_list[i][7]
        field9 = my_list[i][8]
        field10 = my_list[i][9]
        image_name = my_list[i][10]
        write_xml(image=image_name[6:14])

