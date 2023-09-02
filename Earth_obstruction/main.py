from module import  actual_tme
class EarthCore:

    def __init__( self , speed, distance) :

        self.speed = speed
        self.distance = distance


    def check_obstruction( self, expected_time):

        actual_time = actual_tme(self.speed, self.distance)

        if actual_time > expected_time + 60:

            return True
            
        else:
            return False


        
    

        

            
        


          