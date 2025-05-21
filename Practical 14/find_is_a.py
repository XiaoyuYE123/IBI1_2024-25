import xml.dom.minidom
import time
# use dom to parse xml
start_time = time.time()
# read the xml file
# parse the xml file
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
# save the term with most is_a in each namespace
max_terms = {
    "biological_process": {"id": "", "name": "", "count": 0},
    "molecular_function": {"id": "", "name": "", "count": 0},
    "cellular_component": {"id": "", "name": "", "count": 0},
}
# get the term with most is_a in each namespace
# iterate the term
for term in terms:
    try:
        # get the id, name, namespace and is_a
        ns = term.getElementsByTagName("namespace")[0].firstChild.nodeValue.strip()
        term_id = term.getElementsByTagName("id")[0].firstChild.nodeValue.strip()
        term_name = term.getElementsByTagName("name")[0].firstChild.nodeValue.strip()
        is_a_list = term.getElementsByTagName("is_a")
        is_a_count = len(is_a_list)
        # if the term has no is_a, continue
        # save the term with most is_a in each namespace
        if ns in max_terms and is_a_count > max_terms[ns]["count"]:
            max_terms[ns] = {
                "id": term_id,
                "name": term_name,
                "count": is_a_count
            }
    except:
        continue  # skip the term if it has no id, name or namespace
# print the term with most is_a in each namespace

end_time = time.time()
# print the term with most is_a in each namespace
print("DOM Results:")
for ns in ["biological_process", "molecular_function", "cellular_component"]:
    t = max_terms[ns]
    print(f"{ns}: {t['id']} <{t['name']}>, {t['count']} parent terms")
# print the running time
print("DOM running time:", end_time - start_time)
# use sax to parse xml
import xml.sax

class MaxIsAHandler(xml.sax.ContentHandler):
    # This class handles the SAX parsing of the XML file
    # It keeps track of the current state and the maximum number of is_a terms for each namespace.
    def __init__(self):
        self.in_term = False
        self.current_tag = ""
        self.current_id = ""
        self.current_name = ""
        self.current_namespace = ""
        self.temp_is_a_count = 0

        # Dictionary to store the maximum number of is_a terms for each namespace
        # The keys are the namespaces and the values are dictionaries with id, name, and count.
        self.max_terms = {
            "biological_process": {"id": "", "name": "", "count": 0},
            "molecular_function": {"id": "", "name": "", "count": 0},
            "cellular_component": {"id": "", "name": "", "count": 0},
        }
        # Initialize the current tag and term information

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "term":
            self.in_term = True
            self.current_id = ""
            self.current_name = ""
            self.current_namespace = ""
            self.temp_is_a_count = 0
        # if the tag is one of the ones we are interested in, set the current tag
    def characters(self, content):
        text = content.strip()
        if not self.in_term or not text:
            return
        # If we are in a term and the text is not empty, append it to the current tag
        if self.current_tag == "id":
            self.current_id += text
        elif self.current_tag == "name":
            self.current_name += text
        elif self.current_tag == "namespace":
            self.current_namespace += text
        elif self.current_tag == "is_a":
            self.temp_is_a_count += 1
        # If we are in a term and the tag is is_a, increment the count
        # If we are in a term and the tag is id, name, or namespace, set the current id, name, or namespace
    def endElement(self, tag):
        if tag == "term":
            ns = self.current_namespace
            if ns in self.max_terms:
                if self.temp_is_a_count > self.max_terms[ns]["count"]:
                    self.max_terms[ns] = {
                        "id": self.current_id,
                        "name": self.current_name,
                        "count": self.temp_is_a_count
                    }
            self.in_term = False
        self.current_tag = ""
        # Reset the current tag when we reach the end of a term
start_time1 = time.time()
# Create a SAX parser and set the content handler
parser = xml.sax.make_parser()
handler = MaxIsAHandler()
parser.setContentHandler(handler)
parser.parse("go_obo.xml")

end_time1 = time.time()
elapsed = end_time1 - start_time1
# print the term with most is_a in each namespace
# print the running time
print("SAX Results (Term with most is_a in each namespace):")
for ns, info in handler.max_terms.items():
    print(f"{ns}: {info['id']} <{info['name']}>, {info['count']} parent terms")
print("SAX running time:", elapsed)