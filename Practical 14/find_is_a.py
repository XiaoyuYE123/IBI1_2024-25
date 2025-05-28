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
    "biological_process": {
        "count": 0,
        "t": []
    },
    "molecular_function": {
        "count": 0,
        "t": []
    },
    "cellular_component": {
        "count": 0,
        "t": []
    }
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
        if ns in max_terms:
            if is_a_count > max_terms[ns]["count"]:
        # find a new max, update the term
                max_terms[ns]["count"] = is_a_count
                max_terms[ns]["t"] = [{"id": term_id, "name": term_name}]
            elif is_a_count == max_terms[ns]["count"]:
        # if the count is the same, append the term to the list
                max_terms[ns]["t"].append({"id": term_id, "name": term_name})
    except:
        continue  
# skip the term if it has no id, name or namespace
# print the term with most is_a in each namespace

end_time = time.time()
# print the term with most is_a in each namespace
print("DOM Results:")
for ns in ["biological_process", "molecular_function", "cellular_component"]:
    data = max_terms[ns]
    print(f"{ns} (the greatest number of is_a = {data['count']}):")
    for t in data["t"]:
        print(f"  {t['id']} <{t['name']}>")
# print the running time
print("DOM running time:", end_time - start_time)

# use sax to parse xml
import xml.sax
class MaxIsAHandler(xml.sax.ContentHandler):
    # This class handles the SAX parsing of the XML file
    # It keeps track of the current state and the maximum number of is_a terms for each namespace.
    # initialize the handler
    def __init__(self):
        self.in_term = False
        self.current_tag = ""
        self.current_id = ""
        self.current_name = ""
        self.current_namespace = ""
        self.temp_is_a_count = 0

        # Dictionary to store the maximum number of is_a terms for each namespace
        self.max_terms = {
            "biological_process": {"count": 0, "t": []},
            "molecular_function": {"count": 0, "t": []},
            "cellular_component": {"count": 0, "t": []},
        }

    def startElement(self, tag, attr):
        self.current_tag = tag
        if tag == "term":
            # When we encounter a term, reset the current state
            self.in_term = True
            # Reset current values for temporary storage
            self.current_id = ""
            self.current_name = ""
            self.current_namespace = ""
            self.temp_is_a_count = 0

    def characters(self, content):
        text = content.strip()
        if not self.in_term or not text:
            return
        if self.current_tag == "id":
            self.current_id += text
        elif self.current_tag == "name":
            self.current_name += text
        elif self.current_tag == "namespace":
            self.current_namespace += text
        elif self.current_tag == "is_a":
            self.temp_is_a_count += 1

    def endElement(self, tag):
        if tag == "term":
            ns = self.current_namespace
            if ns in self.max_terms:
                if self.temp_is_a_count > self.max_terms[ns]["count"]:
                    # find a new max, update the term
                    self.max_terms[ns]["count"] = self.temp_is_a_count
                    self.max_terms[ns]["t"] = [{
                        "id": self.current_id,
                        "name": self.current_name
                    }]
                elif self.temp_is_a_count == self.max_terms[ns]["count"]:
                    # if the count is the same, append the term to the list
                    self.max_terms[ns]["t"].append({
                        "id": self.current_id,
                        "name": self.current_name
                    })
            self.in_term = False
        self.current_tag = ""

# Parse the XML file using SAX
start_time1 = time.time()
parser = xml.sax.make_parser()
handler = MaxIsAHandler()
parser.setContentHandler(handler)
parser.parse("go_obo.xml")
end_time1 = time.time()
elapsed = end_time1 - start_time1
# Print the results from SAX parsing
print("\nSAX Parsing Results:")
for ns in ["biological_process", "molecular_function", "cellular_component"]:
    data = handler.max_terms[ns]
    print(f"\n{ns} (the greatest number of is_a = {data['count']}):")
    for t in data["t"]:
        print(f"  {t['id']} <{t['name']}>")

print("SAX running time:", elapsed)


# Compare the running times of DOM and SAX
if end_time - start_time < elapsed:
    print("DOM is faster than SAX")
else:
    print("SAX is faster than DOM")