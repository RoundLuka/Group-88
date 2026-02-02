def number(bus_stops):
    
    passengers = 0
    
    for stop in bus_stops:
        
        got_on = stop[0]
        got_off = stop[1]
        
        passengers = passengers + got_on - got_off

    return passengers

print(number([ [3, 0], [4, 2]]))