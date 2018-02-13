This exercise is about programming. 
The program includes topic regarding Data Abstraction, Encapsulation, Polymorphism and Inheritance.
1.Create an aircraft object which contains the following object variables:
   a.x, and y both initialized to zero (default value).  However, the class must be capable of overriding these values of      passed in. These variables will reflect the aircrafts starting position.
   b.An acceleration attribute initialized to 1
   c.An aircraft-model attribute initialized to nil.This will be a mandatory parameter (it has to be passed in)
2.Create aircraft object methods for "moving" the aircraft (x, and y)
   a.Positive/Negative movement in the x-axis moves the aircraft to the right/left respectively.
   b.Positive/Negative movement in the y-axis moves the aircraft to the up/down respectively
3.As part of the aircraft object, calculate the flight path algorithm
   a.Create a function  which then calculates the flight path between the starting point and the destination point.  This can     be explained using  the following example:
   
   
Consider an aircraft which starts from x, y (12, 10) and has a destination x, y (17, 80).  The slop-intercept formula can be used to determine the points 'touched' by the line between these two points; call them (x1, y1) and (x2, y2).  The slop-intercept formula is defined as: y = mx + b where m is the slope of the line and b is the point where the line intercepts the y axis.

The slope of the line is then calculates using the formula: slope = (y2 -y1) / (x2 -x1)
m = slope = ( 80 -10) / (17 -12) = 70/5 = 14
We need to figure out the value of b.  To do this we take y = mx + b and solve for b which yields: b = y -mx; then b = y1 -m * x1 == 10 -14 * 12 = -158

We now have enough information to calculate the y values using the formula: y = mx+b


The flight-path for this aircraft can then be described as follows:  Starting from (12, 10) the aircraft will pass through the points (13,24), (14, 38), (15, 52), (16, 66), and finally reaches it destination at (17, 80).

Your task for this part of the exercise will be to transcribe this algorithm into a function and programmatically calculate the flight path.  Store these values in a list data structure.  HINT:  The example above used whole numbers.  In reality, whole numbers will not describe all of the possibilities.

4.Create an Boeing-747 Class which inherits from the aircraft object
   a.Create the following object variables:
     i.Range (Boing 747 range is about 6100 miles)
     ii.Speed (Boing top speed is about 610 miles per hour)
     iii.Destination coordinates (some random value)
    b.Create methods to retrieve all valuesb.
 
5.Create a new class of aircraft called Private-jet which also inherits from the aircraft object with an acceleration constant of 6 (private jets can accelerate faster than 747s).  Create methods to return attributes.  These values, when printed, should then reflect the values based on the type of aircraft.   Use Google to find the range and max-speed for your favorite private jet.

6.Create a fleet of 10 aircraft.
    a.Seven Boeing and three Private-Jet.
    b.Print the following attributes of each aircraft along with the flight path according to the following format:
    
   Aircraft-Model: Boeing-747
   Aircraft-Range: 6100A
   Aircraft-Max-Speed: 610
   Aircraft-Acceleration: 1
   FLIGHT-PATH(x, y): (12.0, 10.0), (13.0, 24.0), (14.0, 38.0), (15.0, 52.0), (16.0, 66.0), (17.0, 80.0)
