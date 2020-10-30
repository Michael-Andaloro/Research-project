from vpython import *
from star_data import eccentricity

G = 6.67E-11
AU = 1.5E11
Year = 365.25*24*60*60

starA = sphere(pos = vec(-AU, 0,0), mass = 2E30, radius = 1E10, color = color.yellow)
starB = sphere(pos = vec(AU, 0,0), mass = 2E30, radius = 1E10, color = color.red)

starA.vel = vec(0,1.1E4, 0)
starB.vel = vec(0, -1.1E4,0)

starA.trail = curve(pos = starA.pos, color = starA.color)
starB.trail = curve(pos = starB.pos, color = starB.color)

counter = 0 #for printing values now and then
L = vec(0,0,0) #angular momentum of sys
A = vec(0,0,0) #Laplace-Rung-Lenz vector
M = starA.mass + starB.mass
mu = starA.mass*starB.mass/M
rmin = AU
rmax = 0
h = 1E5
scene.autoscale = 1

while True:
    r = mag(starA.pos - starB.pos)
    F = -G*starA.mass*starB.mass*(starA.pos-starB.pos)/r**3 #force on star A
    #force on starB is neg of above
    if r>rmax:
        rmax = r
    if r <rmin:
        rmin = r
    a = (rmin+rmax)/2 #SEMI MAJOR AXIS
    #period keplers 3rd law
    P = sqrt(4*pi**2*a**3/(G*M))/Year
    L = mu*cross((starA.pos - starB.pos), (starA.vel - starB.vel))
    A = cross((starA.vel-starB.vel),(L/mu))- G*M*(starA.pos-starB.pos)/r
    #accentricity
    E = eccentricity
    ecc1 = mag(A)/(G*M) #method 1
    ecc2 = sqrt(1 + 2*mag2(L)*E/((G*M)**2*mu**3))
    ecc3 = (rmax-rmin)/(2*a)#geometrically
    #implement euler
    starA.vel += F/starA.mass*h
    starB.vel -= F/starB.mass*h
    
    starA.pos += starA.vel*h
    starB.pos += starB.vel*h
    starA.trail.append(pos = starA.pos)
    starB.trail.append(pos = starB.pos)
    
    #print occasionally
    if counter >=100:
        print('Ang mom = {0:4.2E}, Energy = {1:4.2E}, Period = {2:4.2E}'.format(mag(L), E, P))
        print('ecc1 = {0:4.2E}, ecc2 = {1:4.2E}, ecc3 = {2:4.2E}'.format(ecc1, ecc2, ecc3))
        counter = 0
    counter += 1
    
    
    rate(100)