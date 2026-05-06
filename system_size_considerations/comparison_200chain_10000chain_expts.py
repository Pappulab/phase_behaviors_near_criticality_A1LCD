import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import seaborn as sns
import os
import math
import sys

plt.rcParams.update({
    'font.family': "sans-serif",
    #'font.family':"DejaVu Sans",
    'font.size': 14,
    'axes.labelsize': 22,
    'axes.titlesize': 22,
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    'legend.fontsize': 14,
    'legend.frameon': False,
    'legend.framealpha': 0.8,
    'axes.linewidth': 2,
    'lines.linewidth': 2,
    #'xtick.direction': 'in',
    #'ytick.direction': 'in',
    #'xtick.top': True,
    #'ytick.right': True,
    'xtick.major.size': 8,
    'ytick.major.size': 8,
    'xtick.minor.size': 4,
    'ytick.minor.size': 4,
})

#Compare the binodals

temperature_float=[46.0, 48.0, 50.0, 52.0, 54.0, 55.0, 56.0, 57.0, 58.0, 58.50,58.75,59,59.25]
temperatures_200chains=[46.0,47.0,48.0,49.0,50.0,51.0,52.0,53.0,54.0]

dil_conc=[np.float64(7.81038419397809e-06), np.float64(5.703844263248188e-05), np.float64(0.00025932147341778877), np.float64(0.000981146897711008), np.float64(0.003048495355396287), np.float64(0.0053191993434376535), np.float64(0.009305273009179096), np.float64(0.016587042321587555), np.float64(0.028033962009164682), np.float64(0.041021187124248515), np.float64(0.04753890232613215), np.float64(0.06417498174818916), np.float64(0.0870886780461993)]

dense_conc=[np.float64(0.5883345897298464), np.float64(0.5465744127234157), np.float64(0.5021742761749471), np.float64(0.4526645195671732), np.float64(0.40104473026412274), np.float64(0.37239768877348595), np.float64(0.34009891610645876), np.float64(0.3042363436996948), np.float64(0.26083460540405884), np.float64(0.2326881697916967), np.float64(0.22300551856077602), np.float64(0.22212596096243162), np.float64(0.13734358455747384)]

dil_conc_10000=dil_conc
dense_conc_10000=dense_conc

dil_conc_200chains=np.array([1.92e-5,4.9e-5,1.12e-4,2.37e-4,4.66e-4,8.47e-4,1.60e-3,2.86e-3,5.17e-3])
dense_conc_200chains=np.array([6.63e-1,6.31e-1,5.97e-1,5.68e-1,5.41e-1,5.15e-1,4.89e-1,4.63e-1,4.37e-1])

temperature_float_celsius=np.array([(i*5.6)-273 for i in temperature_float])
temperature_float_kelvin=np.array([(i*5.6) for i in temperature_float])

temperatures_200chains_celsius=np.array([(i*5.6)-273 for i in temperatures_200chains])
temperatures_200chains_kelvin=np.array([(i*5.6) for i in temperatures_200chains])

temperature_expts_celsius=np.array([4,6,8,10,12,14,16,18,20,22,24,45.4,54.8643,56.0617,56.9,57.5314,57.7377,58.2641,59.2,64.0105,65.5435,73.8853,74.1317,5,10,12,18,20])
conc_expts=np.array([0.0000129,0.0000158,0.0000232,0.0000276606,0.0000468,0.0000529,0.0000579738,0.000077,0.000102,0.000124321,0.000146096,0.002081496,0.007564717,0.00683605,0.003141419,0.008658677,0.007543944,0.01042761,0.005361298,0.0133132,0.0133132,0.01096293,0.009747363,0.02997763,0.03400447,0.02158837,0.02724513,0.02603068])
temperature_expts_kelvin=temperature_expts_celsius+273

scaling_factor=0.06

def T_to_C(T):
    return T * 5.6 - 273

def T_to_K(T):
    return T * 5.6

def convert_to_simtemp(temps):
    return ((np.array(temps)+273)/5.6)

fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)

ax.plot(np.array(dil_conc_200chains),  temperatures_200chains_kelvin, ls='None', lw=1.0,
        marker='^', markersize=15, color='blue', alpha=0.5, label=r'$n=200$ (dilute)')
ax.plot(np.array(dense_conc_200chains), temperatures_200chains_kelvin, ls='None', lw=1.0,
        marker='^', markersize=15, color='red',  alpha=0.5, label=r'$n=200$ (dense)')

ax.plot(np.array(dil_conc_10000),  temperature_float_kelvin, ls='None', lw=1.0,
        marker='o', markersize=15, color='blue', alpha=0.5, label=r'$n=10^{4}$ (dilute)')
ax.plot(np.array(dense_conc_10000), temperature_float_kelvin, ls='None', lw=1.0,
        marker='o', markersize=15, color='red',  alpha=0.5, label=r'$n=10^{4}$ (dense)')

ax.plot(np.array(conc_expts)/scaling_factor, temperature_expts_kelvin, ls='None', marker='s', markeredgewidth=1,markersize=15,
        markerfacecolor='None', color='black', label='Exp. data')

ax.set_xlabel(r'$\phi$')
ax.set_xscale('log')
ax.set_xlim(1e-6,1e0)
ax.set_ylabel(r'$T\;(\mathrm{K})$')
ax.set_ylim(T_to_K(44), T_to_K(64))
c_ticks = np.arange(
    np.ceil(T_to_K(44)),
    np.floor(T_to_K(64)) +1,10
)
ax.set_yticks(c_ticks)
ax.set_yticklabels([f"{t:.1f}" for t in c_ticks])
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('comparison_binodals_200chain_10000chain_expts.pdf',bbox_inches='tight')


#Transfer free energies

temperature_expts_celsius = np.array([
    4,5,6,8,10,12,14,16,18,20,22,24,45.4,54.8643,56.0617,56.9,57.5314,
    57.7377,58.2641,59.2,64.0105,65.5435,73.8853,74.1317,5,10,12,18,20
])
conc_expts = np.array([
    0.0000129,0.00001435,0.0000158,0.0000232,0.0000276606,0.0000468,0.0000529,
    0.0000579738,0.000077,0.000102,0.000124321,0.000146096,0.002081496,
    0.007564717,0.00683605,0.003141419,0.008658677,0.007543944,
    0.01042761,0.005361298,0.0133132,0.0133132,0.01096293,0.009747363,
    0.02997763,0.03400447,0.02158837,0.02724513,0.02603068
])

temperature_expts_celsius_noncritical = [5,10,12,18,20]
diluteconc_expts_noncritical = [0.00001435,0.0000276606,0.0000468,0.000077,0.000102]
denseconc_expts_noncritical = [0.02997763,0.03400447,0.02158837,0.02724513,0.02603068]

R = 8.31446261815324  # J/mol/K

def partition_and_dG(c_dil, c_den, T_C):
    c_dil = np.asarray(c_dil, float)
    c_den = np.asarray(c_den, float)
    T_K   = np.asarray(T_C, float) + 273
    K = c_den / c_dil                        # dimensionless
    lnK = np.log(K)
    dG_kBT   = -lnK                          # per molecule (thermal units)
    dG_kJmol = -(R * T_K * lnK) / 1000.0     # kJ/mol
    return T_K, K, dG_kBT, dG_kJmol

T_K_200, K200, dG200_kBT, dG200_kJpermol = partition_and_dG(dil_conc_200chains,  dense_conc_200chains,  temperatures_200chains_celsius)
T_K_10k, K10k, dG10k_kBT, dG10k_kJpermol = partition_and_dG(dil_conc_10000,      dense_conc_10000,      temperature_float_celsius)
T_K_expt, Kexpt, dGexpt_kBT, dGexpt_kJpermol = partition_and_dG(diluteconc_expts_noncritical,denseconc_expts_noncritical,temperature_expts_celsius_noncritical)

fig2, axg = plt.subplots(figsize=(8.5,5.5), dpi=300)
axg.plot(temperatures_200chains_kelvin, dG200_kJpermol, '^', lw=2.0,color='k',markersize=14,alpha=0.5,markeredgewidth=1,label=r'$n=200$')
axg.plot(temperature_float_kelvin,dG10k_kJpermol, 'o', lw=2.0,color='k',markersize=14,alpha=0.5,markeredgewidth=1,label=r'$n=10^{4}$')
axg.plot(T_K_expt,dGexpt_kJpermol, ls='None',marker='s',markersize=14,markerfacecolor='None',markeredgewidth=1,color='black',label='Exp. data')
axg.set_xlabel(r'$T\;(\mathrm{K})$')
axg.set_ylabel(r'$\Delta G_\mathrm{tr} \; (\mathrm{kJmol^{-1}})$')
axg.axvline(49.73+273,ls='--',lw=2.0,color='k',label=r'$T_{\mathrm{crossover},\Delta}$')
axg.set_yticks([-25,-20,-15,-10,-5,0])
axg.text(285,-3,r'$\Delta G_\mathrm{tr} = -RT \; \ln \; \frac{\phi_\mathrm{dense}}{\phi_\mathrm{dilute}}$',fontsize=22)
axg.legend(loc='best',fontsize=14)
fig2.tight_layout()
plt.savefig('transferfreenergies_in_KJpermol_200chain_10000chain_expts_tempsinKelvin.pdf',bbox_inches='tight')
