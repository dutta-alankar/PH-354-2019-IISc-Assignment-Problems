# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 06:17:43 2018

@author: Alankar
"""

import numpy as np

M_sun = 1.989e30 #in kg
G = 6.67e-11

def ecc(vmax,rmin):
    e = (vmax**2*rmin)/(G*M_sun)-1
    return e
    
def apph(e,vmax,rmin):
    c = (vmax*rmin)**2/(G*M_sun)
    rmax = c/(1-e)
    return rmax

def v_app(vmax,rmin,rmax):
    vmin = (vmax*rmin)/rmax
    return vmin

def time_p(vmax,rmin,e):
    c = (vmax*rmin)**2/(G*M_sun)
    a = c/(1-e**2)
    T = np.sqrt((((2*np.pi)**2)/(G*M_sun))*a**3)
    return T/(365*24*60**2) #in yr

print('-----------------------------------------------------------')
print('Demo Output:\n\nEarth')
vmax, rmin = 3.0287e4, 1.4710e11
e = ecc(vmax,rmin)
rmax = apph(e,vmax,rmin)
vmin = v_app(vmax,rmin,rmax)
T = time_p(vmax,rmin,e)
#1 m = 6.685e-12 AU
print('\nOrbital Eccentricity: %.4f\nAphelion Distance(m): %.3e\nAphelion Velocity(m/s): %.3e\nOrbital period(yr): %.2f'%(e,rmax,vmin,T))  
print('\nHalley\'s Comet')
vmax, rmin = 5.4529e4, 8.7830e10
e = ecc(vmax,rmin)
rmax = apph(e,vmax,rmin)
vmin = v_app(vmax,rmin,rmax)
T = time_p(vmax,rmin,e)
print('\nOrbital Eccentricity: %.4f\nAphelion Distance(m): %.3e\nAphelion Velocity(m/s): %.3e\nOrbital period(yr): %.2f'%(e,rmax,vmin,T))  
print('-----------------------------------------------------------')
    
vmax = float(input('Enter velocity at perihelion(m/s): '))
rmin = float(input('Enter distance from Sun at perihelion(m): '))
e = ecc(vmax,rmin)
rmax = apph(e,vmax,rmin)
vmin = v_app(vmax,rmin,rmax)
T = time_p(vmax,rmin,e)
print('\nOrbital Eccentricity: %.4f\nAphelion Distance(m): %.3e\nAphelion Velocity(m/s): %.3e\nOrbital period(yrs): %.2f'%(e,rmax,vmin,T))
