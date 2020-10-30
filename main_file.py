from vpython import *
from star_data import eccentricity, p_radius, s_radius, p_mass, s_mass

G = 6.67E-11
AU = 1.5E11
Year = 365.25*24*60*60

p_star = sphere(pos = vec(-AU, 0,0), mass = 2E30, radius = p_radius, color = color.yellow)
s_star = sphere(pos = vec(AU, 0,0), mass = 2E30, radius = s_radius, color = color.red)

p_star.vel = vec(0,1.1E4, 0)
s_star.vel = vec(0, -1.1E4,0)

p_star.trail = curve(pos = p_star.pos, color = p_star.color)
s_star.trail = curve(pos = s_star.pos, color = s_star.color)

counter = 0 #for printing values now and then
L = vec(0,0,0) #angular momentum of sys
A = vec(0,0,0) #Laplace-Rung-Lenz vector
M = p_star.mass + s_star.mass
mu = p_star.mass*s_star.mass/M
rmin = AU
rmax = 0
h = 1E5
scene.autoscale = 1

while True:
    r = mag(p_star.pos - s_star.pos)
    F = -G*p_star.mass*s_star.mass*(p_star.pos-s_star.pos)/r**3 #force on star A
    #force on secondary star is neg of above
    if r>rmax:
        rmax = r
    if r <rmin:
        rmin = r
    a = (rmin+rmax)/2 #SEMI MAJOR AXIS
    #period keplers 3rd law
    P = sqrt(4*pi**2*a**3/(G*M))/Year
    L = mu*cross((p_star.pos - s_star.pos), (p_star.vel - s_star.vel))
    A = cross((p_star.vel-s_star.vel),(L/mu))- G*M*(p_star.pos-s_star.pos)/r
    #accentricity
    E = eccentricity
    ecc1 = mag(A)/(G*M) #method 1
    ecc2 = sqrt(1 + 2*mag2(L)*E/((G*M)**2*mu**3))
    ecc3 = (rmax-rmin)/(2*a)#geometrically
    #implement euler
    p_star.vel += F/p_star.mass*h
    s_star.vel -= F/s_star.mass*h
    
    p_star.pos += p_star.vel*h
    s_star.pos += s_star.vel*h
    p_star.trail.append(pos = p_star.pos)
    s_star.trail.append(pos = s_star.pos)
    
    #print occasionally
    if counter >=100:
        print('Ang mom = {0:4.2E}, Energy = {1:4.2E}, Period = {2:4.2E}'.format(mag(L), E, P))
        print('ecc1 = {0:4.2E}, ecc2 = {1:4.2E}, ecc3 = {2:4.2E}'.format(ecc1, ecc2, ecc3))
        counter = 0
    counter += 1

    
    rate(100)