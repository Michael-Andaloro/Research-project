from vpython import *
'''
binarystars.py
simulates binary stars 10AU and 1AU apart
'''
#define constants
G = 6.67E-11 #gravitational constant
AU = 1.5E11 #one astronomical distance, Earth-Sun average distance
YEAR = 365.25*24*60*60 # a year in seconds
sunMass = 2E30
calcAB = 1
calcCD = 1



#create objects for Stars
massA = 2*sunMass
massB = 1*sunMass

starAInitial = vec(10*AU,0,0)
starBInitial = vec(0,0,0)

starA= sphere(pos=starAInitial, mass = massA, radius = 1E10, color = color.orange)
starB = sphere(pos=starBInitial, mass = massB, radius = 1E10, color = color.red)

opp1 = sphere(pos=vec(0,0,0), mass = 0, radius = 1E10, color = color.orange)
opp2 = sphere(pos=vec(0,0,0), mass = 0, radius = 1E10, color = color.red)


#inital condistions
starA.vel = vec(0, 0.25E4,0)
#starB.vel = -starA.vel
starB.vel = vec(0, -0.5E4,0)
print("Red/Orange = 10 AU apart, starA.vel = vec(0,0.25E4,0) and starB.vel = vec(0,-0.5E4,0)")

starA.trail = curve(pos=starA.pos,color = starA.color)
starB.trail = curve(pos=starB.pos,color = starB.color)
aTrailMax = 10000
bTrailMax = 10000

aMax = 0
bMax = 0
aSemMinVal = 0
bSemMinVal = 0
aM = 1

aSemi = curve(pos = [vec(0,0,0),vec(0,0,0)], color=color.orange)
bSemi = curve(pos = [vec(0,0,0),vec(0,0,0)], color=color.red)

#time step
h = 1E5
scene.autoscale = 1

#def acceleration as a function
while True: #loop through the calculations to animate

    r = mag(starA.pos - starB.pos)
    if( calcAB == 1):
        check = mag(starA.pos - starAInitial)
        if( aMax < check ):
            aMax = check
        if( check < aMax ):
            aMax = starA.pos.x
            bMax = starB.pos.x

            opp1.pos = vec(aMax, 0, 0)
            opp2.pos = vec(bMax, 0, 0)

            aSemVal = mag(opp1.pos - starAInitial)/2.0 # Semi-Major Axis A
            bSemVal = mag(opp2.pos - starBInitial)/2.0 # Semi-Major Axis B

            #Draw Semi-Major Axis for each orbit
            aSemi.clear()
            bSemi.clear()
            aSemi.append([starAInitial, vec(starAInitial.x - aSemVal, 0, 0)])
            bSemi.append([starBInitial, vec(starBInitial.x + bSemVal, 0, 0)])

            # Calculate orbital period of A and B
            abP = sqrt(4.0*pi*pi*(aSemVal + bSemVal)**3/(G*(starA.mass + starB.mass)))

            # Calculate eccentricity using e = distance from center of orbit to foci / Semi-Major Axis Length
            aList = []
            for x in range(starA.trail.npoints):
                aList.append(mag(vec(starAInitial.x - aSemVal, 0, 0) - starA.trail.point(x).pos))
            aSemMinVal = min(aList) #Calculate Semi Minor Axis

            bList = []
            for x in range(starB.trail.npoints):
                bList.append(mag(vec(starBInitial.x + bSemVal, 0, 0) - starB.trail.point(x).pos))
            bSemMinVal = min(bList) #Calculate Semi Minor Axis

            fociA = sqrt(aSemVal**2 - aSemMinVal**2)
            fociB = sqrt(bSemVal**2 - bSemMinVal**2)

            aEcc = fociA/aSemVal
            bEcc = fociB/bSemVal

            aTrailMax = starA.trail.npoints
            bTrailMax = starB.trail.npoints
            print('Orange Orbit\nPeriod: {0:8.3E} \nSemiMajor Axis: {1:8.3E}\nEccentricity: {2:8.3E}\n'.format(abP,aSemVal, aEcc))
            print('\nRed Orbit\nPeriod: {0:8.3E}\nSemiMajor Axis: {1:8.3E}\nEccentricity: {2:8.3E}\n'.format(abP, bSemVal, bEcc))
            calcAB = 0

    if(starA.trail.npoints < aTrailMax*2):
        starA.trail.append(pos=starA.pos)
    if(starB.trail.npoints < bTrailMax*2):
        starB.trail.append(pos=starB.pos)

    F = -G*starA.mass*starB.mass*(starA.pos - starB.pos)/r**3 #force on star A
    #Force on starB is -F

    starA.vel = starA.vel + F/starA.mass*h
    starB.vel = starB.vel - F/starB.mass*h
    starA.pos = starA.pos + starA.vel * h
    starB.pos = starB.pos + starB.vel * h

    rate(200)
