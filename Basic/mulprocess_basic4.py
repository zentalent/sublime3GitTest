import threading
import mul_process_Screenscraper as mps
from time import sleep , ctime

loops = mps.ISBNs



def loop(nloop,nsec):
	print 'start loop',nloop,'at:',ctime()
	sleep(nsec)
	print 'loop',nloop,'done at:',ctime()

def main():

	print 'At', ctime(),'on Amazon...'
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = threading.Thread(target = mps_showRanking(), args=((isbn,)).start())
		threads.append(t)

	for i in nloops:
		threads[i].join()

	print 'all done at:',ctime()

if __name__ == '__main__':
	main()