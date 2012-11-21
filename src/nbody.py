#!/usr/bin/env python

import numpy as np
import array

class nbody():
    def __init__(self, data, n):
        # Input data information
        # * masses
        # * positions
        # * velocities
        self.m  = data[:,0]
        self.rx = data[:,1]
        self.ry = data[:,2]
        self.rz = data[:,3]
        self.vx = data[:,4]
        self.vy = data[:,5]
        self.vz = data[:,6]

        # Amounf of particles
        self.n = n

        # Energy
        self.ekin   = None
        self.epot   = None

    def get_masses(self):
        return self.m

    def get_positions(self):
        return (self.rx, self.ry, self.rz)

    def get_velocities(self):
        return (self.vx, self.vy, self.vz)

    def get_ekin(self):
        self.ekin = 0.0
        for i in range(0, self.n):
            dvx = self.vx[i] * self.vx[i]
            dvy = self.vy[i] * self.vy[i]
            dvz = self.vz[i] * self.vz[i]
            v2  = dvx + dvy + dvz
            self.ekin += 0.5 * self.m[i] * v2
        return self.ekin

    def get_epot(self):
        self.epot = 0.0
        for i in range(self.n):
            tmp_epot = 0.0
            for j in range(i+1, self.n):
                drx = self.rx[j] - self.rx[i]
                dry = self.ry[j] - self.ry[i]
                drz = self.rz[j] - self.rz[i]
                r2  = drx * drx + dry * dry + drz * drz
                tmp_epot -= (self.m[i] * self.m[j])/np.sqrt(r2)
            self.epot += tmp_epot
        return self.epot

    def get_energy(self):
        if self.ekin == None:
            self.ekin = self.get_ekin()
        if self.epot == None:
            self.epot = self.get_epot()

        return self.ekin+self.epot

    def get_density_centre(self):
        nj = 6  # neighbours amount
        p = 0.0
        p_c = np.array([0.0,0.0,0.0])
        dsum = 0.0
        for i in range(self.n):
            d = array.array('d')
            for j in range(0, self.n):
                if i == j: continue
                drx = self.rx[j] - self.rx[i]
                dry = self.ry[j] - self.ry[i]
                drz = self.rz[j] - self.rz[i]
                r = np.sqrt(drx*drx + dry*dry + drz*drz)
                d.append(r)
            d_sort = np.argsort(d)
            radius = d[d_sort[nj-1]]
            aa = (nj - 1) * self.m[i]
            bb = (4.0 * np.pi *  radius**3)/3.0
            p = aa/bb
            dsum += p
            p_c += np.array([self.rx[i], self.ry[i], self.rz[i]]) * p
        p_c /= dsum
        return p_c

    def get_half_mass_radius(self):
        pass

    def get_core_radius(self, p_c):
        mc = 0.4
        d = np.zeros(self.n)
        for i in range(self.n):
            drx = self.rx[i] - p_c[0]
            dry = self.ry[i] - p_c[1]
            drz = self.rz[i] - p_c[2]
            r   = np.sqrt(drx*drx + dry*dry + drz*drz)
            d[i] = r
        d_sort = np.argsort(d)
        core_mass = 0.0
        for i in range(self.n):
            if core_mass > mc:
                i -= 1
                break
            core_mass += self.m[d_sort[i]]
        return d[d_sort[i]]

    def get_relaxation_time(self):
        pass

    def get_crossing_time(self):
        pass

    def get_core_collapse_time(self):
        pass
