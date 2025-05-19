import math
class spacetime():
    def space(X,Y,Z,Radius,theta,fai):
        this.X = Radius * cos(theta)
        this.Y = Radius * sin(fai)
        this.Z = Radius * cos(theta) * cos(fai)
    def time(x,y,z,t):
        return [
            a * sin(x + n) + b * cos(x - n) + c * sin(y + n) + d * cos(y - n) + e * sin(z + n) + f * cos(z - n),       
            a * asin(x + n) + b * acos(x - n) + c * asin(y + n) + d * acos(y - n) + e * asin(z + n) + f * acos(z - n), 
            a * sinh(x + n) + b * cosh(x - n) + c * sinh(y + n) + d * cosh(y - n) + e * sinh(z + n) + f * cosh(z - n), 
            a * tan(x + n) + b * atan(x - n) + c * tan(y + n) + d * atan(y - n) + e * tan(z + n) + f * atan(z - n) 
        ]   
