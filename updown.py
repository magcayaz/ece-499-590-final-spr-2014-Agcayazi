#!/usr/bin/env python
import hubo_ach as ha
import ach
import sys
import time
from ctypes import *
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
s.flush()
r.flush()
state = ha.HUBO_STATE()
ref = ha.HUBO_REF()
direction = 0
wdistance = sys.argv[0]
def slanted():
	rf = 0.15708 # as calculated
	#rf = 0.188216306535068
	sample = 100
	drf = rf/sample
	count = 0
	while(count < sample):
		[statusr, framesizer] = r.get(ref, wait=False, last=False)
		[statuss, framesizes] = s.get(state, wait=False, last=False)
		#setting values for right leg
		ref.ref[ha.RHR] = ref.ref[ha.RHR]- drf
		ref.ref[ha.RAR] = ref.ref[ha.RAR]+ drf
		ref.ref[ha.RSR] = ref.ref[ha.RSR]- drf
		#setting values for Left leg
		ref.ref[ha.LHR] = ref.ref[ha.LHR]- drf
		ref.ref[ha.LAR] = ref.ref[ha.LAR]+ drf
		ref.ref[ha.LSR] = ref.ref[ha.LSR]+ drf
		r.put(ref)
		print "WST: ref = ", state.joint[ha.LHR].ref
		time.sleep(0.2)
		count+=1

def up():
	# inverse kinematics calculation:
	# reference: http://letsmakerobots.com/files/2D_kinematics.pdf
	#	we want the foot to be at 630.9 0.138
	
	rf = 0.15708 # as calculated
	rf = 0.635971 #1.11389
	sample = 100
	drf = rf/sample
	count = 0
	while(count < sample):
		[statusr, framesizer] = r.get(ref, wait=False, last=False)
		[statuss, framesizes] = s.get(state, wait=False, last=False)
		#setting values for right leg
		ref.ref[ha.LHP] = ref.ref[ha.LHP]+ drf
		ref.ref[ha.LKN] = ref.ref[ha.LKN]- 2*drf
		ref.ref[ha.LAP] = ref.ref[ha.LAP]+ drf
		##setting values for Left leg
		#ref.ref[ha.LHR] = ref.ref[ha.LHR]- drf
		#ref.ref[ha.LAR] = ref.ref[ha.LAR]+ drf
		#ref.ref[ha.LSR] = ref.ref[ha.LSR]+ drf
		
		r.put(ref)
		print "WST: ref = ", state.joint[ha.LHR].ref
		time.sleep(0.2)
		count+=1
def down():
	# inverse kinematics calculation:
	# reference: http://letsmakerobots.com/files/2D_kinematics.pdf
	#	we want the foot to be at 630.9 0.138
	
	rf = 0.15708 # as calculated
	rf = 0.635971 #1.11389
	sample = 100
	drf = rf/sample
	count = 0
	while(count < sample):
		[statusr, framesizer] = r.get(ref, wait=False, last=False)
		[statuss, framesizes] = s.get(state, wait=False, last=False)
		#setting values for right leg
		ref.ref[ha.LHP] = ref.ref[ha.LHP]- drf
		ref.ref[ha.LKN] = ref.ref[ha.LKN]+ 2*drf
		ref.ref[ha.LAP] = ref.ref[ha.LAP]- drf
		##setting values for Left leg
		#ref.ref[ha.LHR] = ref.ref[ha.LHR]- drf
		#ref.ref[ha.LAR] = ref.ref[ha.LAR]+ drf
		#ref.ref[ha.LSR] = ref.ref[ha.LSR]+ drf
		
		r.put(ref)
		print "WST: ref = ", state.joint[ha.LHR].ref
		time.sleep(0.2)
		count+=1
		
		
def done():
	# inverse kinematics calculation:
	# reference: http://letsmakerobots.com/files/2D_kinematics.pdf
	#	we want the foot to be at 630.9 0.138
	
	
	[statusr, framesizer] = r.get(ref, wait=False, last=False)
	[statuss, framesizes] = s.get(state, wait=False, last=False)
	#setting values for right leg
	ref.ref[ha.RHP] = 0
	ref.ref[ha.RKN] = 0
	ref.ref[ha.RAP] = 0
	##setting values for Left leg
	ref.ref[ha.LHR] = 0
	ref.ref[ha.LAR] = 0
	ref.ref[ha.LSR] = 0
	ref.ref[ha.RHR] = 0
	ref.ref[ha.RAR] = 0
	ref.ref[ha.RSR] = 0
	#setting values for Left leg
	ref.ref[ha.LHR] = 0
	ref.ref[ha.LAR] = 0
	ref.ref[ha.LSR] = 0
	
	r.put(ref)
	print "WST: ref = ", state.joint[ha.LHR].ref
	time.sleep(0.2)
	count+=1
		
		
def final():
	# inverse kinematics calculation:
	# reference: http://letsmakerobots.com/files/2D_kinematics.pdf
	#	we want the foot to be at 630.9 0.138
	
	rf = 0.15708  #as calculated
	rf = 0.635971 #1.11389
	sample = 100
	drf = rf/sample
	count = 0
	while(count < sample):
		[statusr, framesizer] = r.get(ref, wait=False, last=False)
		[statuss, framesizes] = s.get(state, wait=False, last=False)
		#setting values for right leg
		ref.ref[ha.RHP] = ref.ref[ha.RHP]- drf
		ref.ref[ha.RKN] = ref.ref[ha.RKN]+ 2*drf
		ref.ref[ha.RAP] = ref.ref[ha.RAP]- drf
		##setting values for Left leg
		#ref.ref[ha.LHR] = ref.ref[ha.LHR]- drf
		#ref.ref[ha.LAR] = ref.ref[ha.LAR]+ drf
		#ref.ref[ha.LSR] = ref.ref[ha.LSR]+ drf
		
		r.put(ref)
		print "WST: ref = ", state.joint[ha.LHR].ref
		time.sleep(0.2)
		count+=1
		

def bend():
	# inverse kinematics calculation:
	# reference: http://letsmakerobots.com/files/2D_kinematics.pdf
	#	we want the foot to be at 630.9 0.138
	# unfortunately I did not have enough time to finish this part of the assignment. 
	rf = 0.15708 # as calculated
	rf = 0.613887 #1.11389
	sample = 100
	drf = rf/sample
	count = 0
	while(count < sample):
		[statusr, framesizer] = r.get(ref, wait=False, last=False)
		[statuss, framesizes] = s.get(state, wait=False, last=False)
		#setting values for right leg
		ref.ref[ha.RHP] = ref.ref[ha.RHP]- drf
		ref.ref[ha.RKN] = ref.ref[ha.RKN]+ 2*drf
		ref.ref[ha.RAP] = ref.ref[ha.RAP]- drf
		##setting values for Left leg
		#ref.ref[ha.LHR] = ref.ref[ha.LHR]- drf
		#ref.ref[ha.LAR] = ref.ref[ha.LAR]+ drf
		#ref.ref[ha.LSR] = ref.ref[ha.LSR]+ drf
		
		r.put(ref)
		print "WST: ref = ", state.joint[ha.LHR].ref
		time.sleep(0.2)
		count+=1




rf = 0.807681
sample = 100
drf = rf/sample
count = 0
while(count < sample):
    [statusr, framesizer] = r.get(ref, wait=False, last=False)
    [statuss, framesizes] = s.get(state, wait=False, last=False)
	
	#setting values for right leg
    ref.ref[ha.RHP] = ref.ref[ha.RHP]- drf
    ref.ref[ha.RKN] = ref.ref[ha.RKN]+ 2*drf
    ref.ref[ha.RAP] = ref.ref[ha.RAP]- drf
    #setting values for Left leg
    ref.ref[ha.LHP] = ref.ref[ha.LHP]- drf
    ref.ref[ha.LKN] = ref.ref[ha.LKN]+ 2*drf
    ref.ref[ha.LAP] = ref.ref[ha.LAP]- drf
    
    r.put(ref)
    print "WST: ref = ", state.joint[ha.RHP].ref
    time.sleep(0.15)
    count+=1
  
slanted() 
bend()
up()
down()
up()
down()
up()
down()
up()
down()
up()
down()
up()
final()
done()
#randomkick()
#feetonground()

r.close()
s.close()

