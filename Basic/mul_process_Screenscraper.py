from atexit import register
from re import compile
from threading import Thread
from time import ctime
import urllib2

REGEX = compile ('#([\d,]+) in Books ')
openner = urllib2.build_opener()
openner.addheaders = [('User-Agent','Mozilla/6.0')]
AMZN = 'http://www.amazon.com/dp/'


ISBNs= {
	'0132269937':'Core Python Programming',
	'0132356139':'Python Web Development with Django',
	'0137143419':'Python Fundamentals',
	}
def getRanking(isbn):
	page = openner.open('%s%s'% (AMZN,isbn)) # or str.format()
	data = page.read()
	#print data
	page.close()
	print REGEX.findall(data)[0]
	return REGEX.findall(data)[0]

def _showRanking(isbn):
	
	print '- %r ranked %s'%(
		ISBNs[isbn],getRanking(isbn))

def _main():
	for isbn in ISBNs:
		Thread(target = _showRanking,args=(isbn,)).start()

@register
def _atexit():
	print 'all Done at:',ctime()

if __name__ == '__main__':
	_main()