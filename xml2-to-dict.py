import xmltodict

with open('lab.xml') as data:
 xml_data = data.read()

xml_odict = xmltodict.parse(xml_data)

print(xml_odict)
