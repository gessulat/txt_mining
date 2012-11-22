import xml.sax, argparse
from xml.sax.saxutils import unescape
 
class Xml_to_abstract(xml.sax.ContentHandler):
	"""
	Every line is in the output.txt is one document. The first word in the line is the document's Id, the rest the abstract's words
	"""
	def __init__(self, outFile=False):
		xml.sax.ContentHandler.__init__(self)
		self.stack = []
		self.record_count = 0
		self.out = outFile
		self.abstract_array = [] # safety first!
		self.out_string = "".encode('utf8')
		if( outFile ):
			print "\twriting output to "+outFile.name+ " - this can take a while, so please bear with me!\n"
			print "\t"+self.__doc__.strip()
		
	def startElement(self, entering_element, attrs):
		self.stack.append(entering_element)
		if( entering_element == 'record'):
			self.abstract_array = [] # reset
			self.out_string = "".encode('utf8')


	def characters(self, content):
		if( self.stack[-1] == "identifier"):
			self.out_string = content.split(":")[-1].encode('utf8') + " "
		if( self.stack[-1] == "dc:description" ):
			content_string = unescape( content )
			for t in content_string.split(): self.abstract_array.append(t)

	def endElement(self, element_name):
		leaving_element = self.stack.pop()
		if( leaving_element == 'record'):	
			self.out_string += " ".join(self.abstract_array).encode('utf8')
			if( self.out ):
				self.record_count += 1
				self.out.write(self.out_string)
			else:
				print self.out_string

class Xml_to_refs(xml.sax.ContentHandler):
	"""
	Every line is in the output.txt is one document. The first word in the line is the document's Id, the rest its relations (references)
	"""
	def __init__(self, outFile=False):
		xml.sax.ContentHandler.__init__(self)
		self.stack = []
		self.record_count = 0
		self.out = outFile
		self.abstract_array = [] # safety first!
		self.out_string = ""
		if( outFile ):
			print "\twriting output to "+outFile.name+ " - this can take a while, so please bear with me!\n"
			print "\t"+self.__doc__.strip()
		

	def startElement(self, entering_element, attrs):
		self.stack.append(entering_element)
		if( entering_element == 'record'):
			self.references = [] # reset
			self.out_string = ''

	def characters(self, content):
			if( self.stack[-1] == "identifier"):
				self.out_string = content.split(":")[-1].encode('utf8') + " "
			if( self.stack[-1] == "dc:relation" ):
				self.references.append( content )

	def endElement(self, element_name):
		leaving_element = self.stack.pop()
		if( leaving_element == 'record'):

			self.out_string += " ".join( self.references )
			if( self.out ):
				self.record_count += 1
				self.out.write(self.out_string)
			else:
				print self.out_string


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('part', choices=('refs', 'abs'), 
								help="What part of the xml file do you want to parse? Choose abstracts (abs) or references (refs).")
	parser.add_argument('input', help='input file path (citeseer xml file)')
	parser.add_argument('--out', default=False, help="file path of an output file. If not set, this writes to the console.")
	
	args = parser.parse_args()

	sourceFilePath = args.input
	source = open(sourceFilePath)
	
	if( args.out ):
		outFilePath = args.out
		out = open(outFilePath, 'w')
	else:
		out = False

	if( args.part == 'refs' ):
		xml.sax.parse(source, Xml_to_refs( out ) )
	if( args.part == 'abs' ):
		xml.sax.parse(source, Xml_to_abstract( out ) )
	source.close()
	out.close()

if __name__ == "__main__":
	main()



