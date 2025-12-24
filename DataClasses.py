Location = tuple[int, int]


class XMLWire:
    def __init__(self):
        self.label: str = ""
        self.startLoc: Location = (0, 0)
        self.endLoc: Location = (0, 0)
        self.inputPin: XMLInputPin | None = None
        self.isOutput: XMLOutputPin = None


class XMLPin:
    def __init__(self, name: str = "", bitsSize: int = 1):
        self.name = name
        self.size = bitsSize
        self.location: Location = (0, 0)


class XMLInputPin(XMLPin):
    pass


class XMLOutputPin(XMLPin):
    pass


class XMLCircuit:
    def __init__(self, name=""):
        self.name = name
        self.inputPorts: list[XMLInputPin] = []
        self.outputPorts: list[XMLOutputPin] = []
        self.wires: list[XMLWire] = []

        self.comps: list[XMLComp] = []


class XMLComp:
    def __init__(self, name=""):
        self.name = name
        self.comp: XMLCircuit | None = None
        self.loc: Location = (0, 0)
