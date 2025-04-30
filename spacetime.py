import math
class sphere():
    def space(X,Y,Z,Radius,theta,fai):
         this.X = Radius * cos(theta)
         this.Y = Radius * sin(fai)
         this.Z = Radius * cos(theta) * cos(fai)
    def time(x,y,z,t):
        return [
            a * sin(x + t) + b * cos(x - t) + c * sin(y + t) + d * cos(y - t) + e * sin(z + t) + f * cos(z - t),       #t123
            a * asin(x + t) + b * acos(x - t) + c * asin(y + t) + d * acos(y - t) + e * asin(z + t) + f * acos(z - t), #t456
            a * sinh(x + t) + b * cosh(x - t) + c * sinh(y + t) + d * cosh(y - t) + e * sinh(z + t) + f * cosh(z - t), #t789
            a * tan(x + t) + b * atan(x - t) + c * tan(y + t) + d * atan(y - t) + e * tan(z + t) + f * atan(z - t) #t101112
        ]   
