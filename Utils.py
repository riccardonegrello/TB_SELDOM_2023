
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import scipy.optimize as opt
import copy
import os
import h5py

def gaus(x, A, mu, sigma):

    return A*np.exp(-(x-mu)**2/(2*sigma**2)) 

def myGauss(x, a, mu, sigma):
    return a * np.exp(- (x-mu)**2 / (2*sigma**2))

# def project_to_z_pos(z1,z2,z4):
def proiettaDistZ(z):
    mx = (x2-x1)/dizi["d_12"]
    xProj = x1 + mx * z
    
    my = (y2-y1)/dizi["d_12"]
    yProj = y1 + my * z
    
    return (xProj, yProj)


def Average(lst):
    return sum(lst) / len(lst)
    
def align(x1, y1, x2, y2, d, plotter):
    # Allineo usando 1 come riferimento
    
    nBins = 1000


    c = [x1,x2,y1,y2] 
    div = []
    offset_lst = []
    lst_ax = ["x","y"]
    
    if plotter:
        fig, ax = plt.subplots(1,2)
        fig.subplots_adjust(hspace=.4)
        fig.set_size_inches(9,7)
    
    for i in range(2):
        
        theta = np.arctan((c[2*i+1]-c[2*i])/d) 
        h_theta, b_thetas = np.histogram(theta, bins = nBins)
    
        b_theta = b_thetas[:-1] + (b_thetas[1]-b_thetas[0])/2
        
        
        # Cerco gli starting points per il fit
        sigma = np.std(theta)
        mu = np.mean(theta)
        a = np.max(h_theta)

        p0 = [a, mu, sigma]

        # Seleziono i dati per il fit e fitto
        #logi = (b_theta > (mu - 2*sigma)) & (b_theta < (mu + 2*sigma))
        logi = (b_theta > (mu - 1.5*sigma)) & (b_theta < (mu + 1.5*sigma))
        x_fit = b_theta[logi]
        y_fit = h_theta[logi]
        oP, pC = opt.curve_fit(gaus, xdata = x_fit, ydata = y_fit, sigma=np.sqrt(y_fit), p0 = p0, absolute_sigma=True)

        # Calcolo lo shift da applicare al secondo telescopio per avere a zero la distribuzione angolare
        y_mu = gaus(oP[1],*oP)
        mu = oP[1]
        offset = d*np.tan(mu)
        offset_lst.append(offset)
        div.append(oP[2])
        
        if plotter:
            ax[i].plot(b_theta, h_theta, ds = 'steps-mid', color = 'hotpink', label = 'Not aligned')

            
            ax[i].plot(x_fit, gaus(x_fit,  *oP), c ='k',ls = '--')

            testo = f'$\mu = $ {mu:.2e} rad \n $\sigma$ = {oP[2]:.2e} \n offset_x = {offset:.2e} cm'
            ax[i].plot(mu, y_mu,  '*', color = 'k', ms = 11, label = testo)

            # Sottraggo e riplotto per correggere
            theta = np.arctan(((c[2*i+1]-offset)-c[2*i])/d)

            h_theta,b_theta = np.histogram(theta,bins = nBins)
            b_theta = b_theta[0:-1] + (b_theta[1]-b_theta[0])/2
            ax[i].plot(b_theta, h_theta, ds = 'steps-mid', color = 'steelblue', label = 'Aligned')
            stringa = r"$\theta$" + lst_ax[i] + " [rad]"
            ax[i].set_xlabel(stringa)
            ax[i].set_ylabel('Entries')
            ax[i].grid()
            ax[i].legend()
            
    if plotter:
        plt.show()
        
    return offset_lst, div