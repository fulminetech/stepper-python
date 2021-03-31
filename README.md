# stepper-python

APIs:

1. Commands: http://192.168.1.101:5000/stepper/<val>
val:

status
forward
reverse
stop
loop

2. Set: http://192.168.1.101:5000/set/:parameter/:value
parameters:

pps_fwd
pps_rev
fwd_timer
rev_timer
fwd_halt
rev_halt
counter_set