import math
class sphere():
    def space(X,Y,Z,Radius,theta,fai):
         this.X = Radius * cos(theta)
         this.Y = Radius * sin(fai)
         this.Z = Radius * cos(theta) * cos(fai)
    def time(x,y,z,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12):
        return [
            a * sin(x + t1) + b * cos(x - t1) + c * sin(y + t2) + d * cos(y - t2) + e * sin(z + t3) + f * cos(z - t3),       #t123
            a * asin(x + t4) + b * acos(x - t4) + c * asin(y + t5) + d * acos(y - t5) + e * asin(z + t6) + f * acos(z - t6), #t456
            a * sinh(x + t7) + b * cosh(x - t7) + c * sinh(y + t8) + d * cosh(y - t8) + e * sinh(z + t9) + f * cosh(z - t9), #t789
            a * tan(x + t10) + b * atan(x - t10) + c * tan(y + t11) + d * atan(y - t11) + e * tan(z + t12) + f * atan(z - t12) #t101112
        ]   
