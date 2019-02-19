
import math
from math import sqrt as sqrt


# Calculate the digits of pi using the ridiculous method of balls bouncing off walls. 



#print(ball1['mass'])

def addmass(ball1, ball2):
	return ball1['mass'] + ball2['mass']



def collision(ball1, ball2):
        
    if (ball1['velocity']<0):
        ball1['velocity'] = -ball1['velocity']
        ball1['collisionNum'] +=1
        ball2['collisionNum'] +=1

    elif (ball1['velocity']<=ball2['velocity']):
        print ('how are we here?')
        
    else:
        v1 = ball1['velocity']
        v2 = ball2['velocity']
        m1 = ball1['mass']
        m2 = ball2['mass']
        E = m1*v1**2 + m2*v2**2
        P = m1*v1 + m2*v2
        M = m1 + m2
        m = m1/m2
        #print('E = ', E) 
        #print('P=', P)
        

        
        if (v2>(P/(m2+m1))):
            v2 = (P-sqrt(P**2 - (1+ m1/m2)*(P**2 - E * m1))) / (m2 + m1)
            #ball2['velocity'] = v2
            #print ('done')
            
        else:
            
            # Error Checking
            if ((P**2 - (1+ m1/m2)*(P**2 - E * m1)) <= 0):
                print("Here's the Math Domain Error, collision number", ball1['collisionNum'])
                print('Discrimanant = ', (P**2 - (1+ m1/m2)*(P**2 - E * m1)))
                if (ball1['collisionNum']<3):
                    print('v1 = ', v1)
                    print('v2 = ', v2)
                    print('P = ', P)
                    print('E = ', E)
                
#            v2 = (P+sqrt(P**2 - (1+ m1/m2)*(P**2 - E * m1)) ) / (m2 + m1)
            v2 = (m2*P+sqrt(m2**2 * P**2 - (m2**2+ m1 * m2)*(P**2 - E * m1)) ) / (m2**2 + m1* m2)
            ball2['velocity'] = v2

        
        v1 = (P - m2 * v2) / m1
        ball2['velocity'] = v2
        ball1['velocity'] = v1
        #print ('v1 = ', v1)
        
        ball1['collisionNum'] +=1
        ball2['collisionNum'] +=1


#print(ball1['collisionNum'])
# E = v_1^2 + v_2^2
# P = m_1 v_1 + m_2 v_2
# v_1 = (+/-)sqrt(v_2^2-E)
# v_1 = (P - m_2 v_2 )/m_1
#       (P - m_2 v_2)^2 / m_1^2 = v_2^2-E 
