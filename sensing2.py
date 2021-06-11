from sense_hat import SenseHat #imports the SenseHat

sense= SenseHat() #sets the command

sense.set_pixel(2,2,(101,67,33)) #creates a pixel in a certain place, in a certain color
sense.set_pixel(4,2,(101,67,33))
sense.set_pixel(3,4,(100,0,0))
sense.set_pixel(1,5,(0,200,100))
sense.set_pixel(2,6,(0,200,100))
sense.set_pixel(3,6,(0,200,100))
sense.set_pixel(4,6,(0,200,100))
sense.set_pixel(5,5,(0,200,100))

