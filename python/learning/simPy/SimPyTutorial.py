import simpy

def car(env):
    
# Infinite loop
    while True:
        
# New state, at current sim. time (env.now)
        print('Start parking at %d' % env.now)  
        parking_duration = 5
        
# Timeout event describes the point in time when
# the car is done parking (or driving)
        yield env.timeout(parking_duration)     

# By 'yielding' the event, we signal the sim. to wait for the event to occur

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)



# Now we create an instance of "Environment", and see how it behaves

# "Environment" instance is passed into our 'car' function
# This creates a process generator, which needs to be started
# and added to the environment via "Environment.process()"

env = simpy.Environment()
env.process(car(env))
env.run(until=15)
