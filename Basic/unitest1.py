import unittest
def get_formatted_name(first,last):
	"""Generate a neatly formatted full name."""
	full_name = first +' '+last
	return full_name.title()

def get_name():
	while True:
		first = raw_input("\nPlease give me a first name:")
		if first == 'q':
			break
		last = raw_input("Please give me a last name:")
		if last == 'q':
			break
		print type(first),type(last)
		formatted_name = get_formatted_name(first,last)
		print '\tNeatly formatted name: '+ formatted_name+'.'

class NamesTestCase(unittest.TestCase):
	"""test get_formatted_name"""
	def test_first_last_name(self):

		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')

unittest.main()