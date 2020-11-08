# dwarfnova.py
# simulates a dwarf nova system

from vpython import*
from math import*
from random import*

autoscale = 0

starA = sphere(pos= vec(0, 0, 0), radius=6.6e6, mass=1.5e30, color=color.white)
starB = sphere(pos= vec(5.80e8, 0, 0), radius=1.5e8, mass=3.75e29, color=color.red)
center = (starA.pos*starA.mass+starB.pos*starB.mass)/(starA.mass+starB.mass)
print (center)
CM = sphere(pos = center, radius=2e6, color=color.green)

P = 7.8719e3  #orbital period from Olech
L = 2e8     
G=6.67e-11   # gravitational constant

xaxis=curve(pos=[(center.x,0,0), (L-center.x,0,0)], color= vec(0.5,0.5,0.5))
yaxis=curve(pos=[(center.x,0,0), (center.x,L,0)], color= vec(0.5,0.5,0.5))
zaxis=curve(pos=[(center.x,0,0), (center.x,0,L)], color= vec(0.5,0.5,0.5))

starB.velocity=4.0*vector(0,+6.78e4,0)
starA.velocity=4.0*vector(0,-6.78e4,0)*0.25


dt=e-1
h = dt
t=0
starA.trail=curve(color=starA.color)
starB.trail=curve(color=starB.color)

L1=3.69e8  #distance from starA to Lagrange point L1
L2= 2.11e8
Omega = 2.0*pi/P
unit = vector(0,1,1)
t = 0

particle_list = []

def particle_release():
    if t < 750:
        for i in range(2):
            particle = sphere(color=color.orange, radius = 4e6, mass = 2.0e10)
            particle.pos = starA.pos +0.6367*(starB.pos-starA.pos)
            particle.velocity = vector(0,0,0)
            particle.velocity.x = -particle.pos.x*Omega*(1.0 + random())
            particle.velocity.y = particle.pos.y*Omega*(1.0 + random())
            particle.velocity.z = particle.pos.z*Omega*(1.0 + random())
            particle_list.append(particle)
    for particle in particle_list:
        rA = mag(particle.pos - starA.pos)
        rB = mag(particle.pos - starB.pos)
        if rA > L1/200 and rB > L2/100: 
            acc_p = G*starA.mass*(starA.pos - particle.pos)/rA**3 + G*starB.mass*(starB.pos - particle.pos)/rB**3
            k1v = dt*acc_p
            k1x = dt*particle.velocity
            k2v = dt*(G*starA.mass*(starA.pos - (particle.pos+k1x/2.0))/rA**3 + G*starB.mass*(starB.pos - (particle.pos+k1x/2.0))/rB**3)
            k2x = dt*(particle.velocity + k1v/2.0)
            k3v = dt*(G*starA.mass*(starA.pos - (particle.pos+k2x/2.0))/rA**3 + G*starB.mass*(starB.pos - (particle.pos+k2x/2.0))/rB**3)
            k3x = dt*(particle.velocity + k2v/2.0)
            k4v = dt*(G*starA.mass*(starA.pos - (particle.pos+k3x/2.0))/rA**3 + G*starB.mass*(starB.pos - (particle.pos+k3x/2.0))/rB**3)            
            k4x = dt*(particle.velocity + k3v)
            particle.velocity += (k1v + 2.0*k2v + 2.0*k3v + k4v)/6.0
            particle.pos += (k1x + 2.0*k2x + 2.0*k3x + k4x)/6.0
                                                                                   
def acc(starpos):
    return -G*starother.mass*(starpos-starother.pos)/r**3

def rk4(star):
    k1v = h*acc(star.pos)
    k1x = h*star.velocity

    k2v = h* acc(star.pos + k1x/2.0)
    k2x = h*(star.velocity + k1v/2.0)

    k3v = h*acc(star.pos + k2x/2.0)
    k3x = h*(star.velocity + k2v/2.0)

    k4v = h*acc(star.pos + k3x)
    k4x = h*(star.velocity + k3v)

    star.velocity += (k1v + 2.0*k2v + 2.0*k3v + k4v)/6.0
    star.pos += (k1x + 2.0*k2x + 2.0*k3x + k4x)/6.0

while True:
    r = mag(starA.pos - starB.pos) 
    for i in range (0,2):
        if i == 1:
            starother= starB
            rk4(starA)
        else:
            #r = mag(starA.pos - starB.pos) 
            starother= starA
            rk4(starB)

    starA.trail.append(pos=starA.pos)
    starB.trail.append(pos=starB.pos)
    particle_release()
    t +=dt
