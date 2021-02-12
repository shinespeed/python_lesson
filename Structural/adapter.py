class XMLdata:
    def request(self):
        return "XMLdata: The default XML data"


class JSONdata:
    def specific_request(self):
        return "data in the form JSON"


class Adapter(XMLdata, JSONdata):
    def request(self):
        return f"Adapter: (TRANSLATED) {self.specific_request()} + now it is applicable for xml"


def client_code(xmlData: "XMLdata"):
    print(xmlData.request(), end="")


if __name__ == "__main__":
    xmlData = XMLdata()
    client_code(xmlData)
    print("\n")

    jsonData = JSONdata()

    print(f"JSONdata: {jsonData.specific_request()}", end="\n\n")

    adapter = Adapter()
    client_code(adapter)