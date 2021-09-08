import xmltodict

xmlFile = open ('lab.xml')

xmlData = xmlFile.read()

xmlFile.close()

xml_dict = xmltodict.parse(xmlData)

print(xml_dict)

print(xml_dict['device']['interface'])
