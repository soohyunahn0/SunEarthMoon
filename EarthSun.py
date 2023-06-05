from vpython import *

def main():
    # simulate the motion of the Earth around the Sun
    
    # define gravitational constant
    G = 6.67408e-11
    
    # mass of the sun(kg)
    m_sun = 1.9891e30 
    
    # radius of the sun(meters)
    # r_sun_actual = 6.9634e8
    r_sun = 5e10
    
    # mass of the Earth
    m_earth = 5.97e24
    
    # r_earth_actual = 6.367e6
    r_earth = 1e10
    
    # mass of the moon
    m_moon = 7.34767309e22
    
    # radius of the moon
    r_moon = 5e9
    
    # create the sun object
    sun = sphere(pos=vector(0,0,0), radius=r_sun, color=color.yellow)

    Sm = 3.48e8
    Se = 1.5e11
    
    we = sqrt(G*m_sun/Se**3)
    wm = sqrt(G*m_earth/Sm**3)
    
    tmonth=28*24*60*60
    
    # create the earth object
    earth = sphere(pos=vector(1.496e11,0,0), radius=r_earth, color=color.blue)
    
    earth.velocity = vector(0, Se* m_earth *we, 0)
    
    #create the moon object
    moon = sphere(pos=vector(1.8e11,0,0), radius=r_moon, color=color.gray(0.5))

    moon.velocity = m_moon * (earth.velocity/m_earth + vector(0, -Sm*wm, 0))
    
    # define the initial time 
    t = 0
    
    # define a time interval
    dt = 500
    
    while (t < 1e10):
        rate (3000)

        re = earth.pos - sun.pos
        rem = moon.pos - earth.pos
        res = moon.pos - sun.pos

        F_grav = ((-G * m_sun * m_earth * norm(re))/(mag(re)**2)) + G * m_earth * m_moon * norm(rem)/ (mag(rem)**2)
        M_grav = ((-G * m_sun * m_moon * norm(re))/(mag(re)**2)) + G * m_earth * m_moon * norm(rem)/ (mag(rem)**2)

        earth.velocity = earth.velocity + F_grav*dt
        moon.velocity = moon.velocity + M_grav*dt

        earth.pos = earth.pos + earth.velocity * dt/m_earth
        moon.pos = moon.pos + moon.velocity * dt/m_moon
        
        #earth.pos = earth.pos + earth.velocity * dt
        #moon.pos = moon.pos + moon.velocity * dt
        #moon.pos = moon.pos + 100 * (earth.pos - moon.pos)
        
        #r_vector = earth.pos - sun.pos
        #m_vector = moon.pos - sun.pos
        
        #F_grav = - (G * m_sun * m_earth / (mag(r_vector)**2) * norm(r_vector)) # norm = direction
        #earth.velocity = earth.velocity + (F_grav / m_earth) * dt
        
        #M_grav = - (G * m_sun * m_moon / (mag(m_vector)**2) * norm(m_vector)) # norm = direction
        #moon.velocity = moon.velocity + (M_grav / m_moon) * dt
        
        t += dt
        
main()
        
        
        
