import xml.etree.ElementTree as ET

arquivo = "a.xml"
tree = ET.parse(arquivo)
root = tree.getroot()
filtro = "*"
for child in root.iter(filtro):
   if(child.text == "#2EC1D7"):
        child.text = child.text.replace('#2EC1D7', 'A2A2A2')
        tree.write("b.xml")