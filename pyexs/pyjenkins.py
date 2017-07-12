#-*- coding:utf-8 -*-
import jenkins
import sys

server = jenkins.Jenkins('http://192.168.20.244:8080/',username = 'zongting' , password = 'zongting')
user = server.get_whoami()
print ('hello %s from Jenkins' % (user['fullName']))

jobs = server.get_jobs()
print jobs[0]

myjob = server.get_job_config('Unity_Branch_Tap_channel3')
print myjob

mynode = server.get
print mynode



