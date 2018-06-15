import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

root = ET.Element('ExtrinsicParameters')

tvec = ET.SubElement(root, 'tvec')

tvec_x = ET.SubElement(tvec, 'tvec_x')
tvec_x.text = 'x'
tvec_y = ET.SubElement(tvec, 'tvec_y')
tvec_y.text = 'y'
tvec_z = ET.SubElement(tvec, 'tvec_z')
tvec_z.text = 'z'



string = ET.tostring(root, 'utf-8')
pretty_string = minidom.parseString(string).toprettyxml(indent='  ')

with open('test.xml', 'w') as f:
    f.write(pretty_string)

