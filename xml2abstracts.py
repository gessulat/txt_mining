import xml.sax, argparse, pickle
from xml.sax.saxutils import unescape
from datetime import datetime
import time


class Xml_to_abs(xml.sax.ContentHandler):

	def __init__(self, outFile=False):
		xml.sax.ContentHandler.__init__(self)
		self.deadline = time.strptime("2010-01-01", "%Y-%m-%d")
		self.stack = []
		self.abs_pickle = {}
		self.record_count = 0
		self.out = outFile
		self.abstract_array = [] # safety first!
		self.doc_id = ""
		self.recent_date = False
		if( outFile ):
			print str(datetime.now())+" starting to read abstracts!\n"		

	def startElement(self, entering_element, attrs):
		self.stack.append(entering_element)
		if( entering_element == 'record'):
			self.abstract_array = [] # reset
			self.doc_id = ''

	def characters(self, content):
			if( self.stack[-1] == "identifier"):
				self.doc_id = content.split(":")[-1]
			if( self.stack[-1] == "dc:description" ):
				content_string = unescape( content )
				for t in content_string.split(): self.abstract_array.append(t)
			if( self.stack[-1] == "datestamp"):
				try:
					self.recent_date = time.strptime(content, "%Y-%m-%d")
				except ValueError:
					self.recent_date = time.strptime("2013-01-01", "%Y-%m-%d")


	def endElement(self, element_name):
		leaving_element = self.stack.pop()
		if( leaving_element == 'record'):
			if self.deadline > self.recent_date:
				self.record_count += 1
				self.abs_pickle[self.doc_id] = self.abstract_array
	
	def endDocument(self):
		print str(datetime.now())+' starting to persist abstracts to: '+outFile.name
		pickle.dump(self.abs_pickle, self.out)


def main():
	source = open("../citeseer.xml")
	out = open('../abstracts.pickle', 'w')

	print "xml2abstracts.py - extracts abstracts from '"+source.name+"' and writing it to '"+out.name+"'"
	xml.sax.parse(source, Xml_to_abs( out ) )
	source.close()
	out.close()

if __name__ == "__main__":
	main()



