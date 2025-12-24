import xml.etree.ElementTree as ET
from DataClasses import *


def parseLocation(loc: str) -> Location:
    loc_res = loc.strip("(").strip(")").split(",")
    loc_res = (int(loc_res[0]), int(loc_res[1]))
    return loc_res


def parseFile(file: str):
    tree = ET.parse(file)

    root = tree.getroot()

    components: dict[str: XMLComp] = {}

    circuits = root.findall("circuit")
    for circuit in circuits:
        circuitName = circuit.attrib["name"]
        circuitComp = XMLCircuit(circuitName)
        components[circuitName] = circuitComp

        for wire in circuit.findall("wire"):
            from_loc = parseLocation(wire.attrib["from"])
            to_loc = parseLocation(wire.attrib["to"])

            newWire = XMLWire()
            newWire.startLoc = from_loc
            newWire.endLoc = to_loc

        for comp in circuit.findall("comp"):
            if comp.attrib["name"] == "Pin":
                attrs = {}

                for a in comp.findall("a"):
                    attrs[a.attrib["name"]] = a.attrib["val"]

                if attrs.get("output", "") == "true":
                    name = attrs.get("label", "")
                    width = int(attrs.get("width", "1"))
                    newPin = XMLOutputPin(name, width)
                    newPin.location = parseLocation(comp.attrib["loc"])

                    circuitComp.outputPorts.append(newPin)

                else:
                    name = attrs.get("label", "")
                    width = int(attrs.get("width", "1"))
                    newPin = XMLInputPin(name, width)
                    newPin.location = parseLocation(comp.attrib["loc"])

                    circuitComp.inputPorts.append(newPin)
            else:

                name = comp.attrib["name"]
                loc = parseLocation(comp.attrib["loc"])
                newComp = XMLComp(name)
                newComp.loc = loc

                circuitComp.comps.append(newComp)


parseFile("temp.circ")
