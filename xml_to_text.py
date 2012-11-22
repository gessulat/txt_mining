import xml.sax
from xml.sax.saxutils import unescape
 
class Xml_to_abstract(xml.sax.ContentHandler):
	def __init__(self, outFile):
		xml.sax.ContentHandler.__init__(self)
		self.stack = []
		self.record_count = 0
		self.out = outFile
	def startElement(self, entering_element, attrs):
		self.stack.append(entering_element)
		if( entering_element == 'record'):
			self.abstract_array = []
	def endElement(self, element_name):
		leaving_element = self.stack.pop()
		if( leaving_element == 'record'):
			self.record_count += 1
			print "parsed "+str(self.record_count)+" records"
			out_string = " ".join(self.abstract_array).encode('utf8')
			self.out.write(out_string)
	def characters(self, content):
			if( self.stack[-1] == "dc:description" ):
				content_string = unescape( content )
				for t in content_string.split(): self.abstract_array.append(t)


def main(sourceFilePath, outFilePath):
	source = open(sourceFilePath)
	out = open(outFilePath, 'w')

	xml.sax.parse(source, Xml_to_abstract( out ) )


if __name__ == "__main__":
	main("../citeseer.xml", "../abstracts2.txt" )