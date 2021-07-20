from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

parameters = pd.read_table('1_para.txt')
para = parameters.values

fig = plt.figure()

host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
parc = ParasiteAxes(host, sharex=host)
host.parasites.append(parc)

host.axis["right"].set_visible(False)
parc.axis["right"].set_visible(True)
parc.axis["right"].major_ticklabels.set_visible(True)
parc.axis["right"].label.set_visible(True)

host.axis['left'].label.set_color('b')
host.axis['left'].major_ticks.set_color('b')
host.axis['left'].major_ticklabels.set_color('b')
host.axis['left'].line.set_color('b')

parc.axis['right'].label.set_color('r')
parc.axis['right'].major_ticks.set_color('r')
parc.axis['right'].major_ticklabels.set_color('r')
parc.axis['right'].line.set_color('r')

name = np.arange(8)
#GRB1
alpha      = float(para[0,2].split(',')[0])
alpha_l    = float(para[0,2].split(',')[1])
alpha_u    = float(para[0,2].split(',')[2])
beta       = float(para[0,3].split(',')[0])
beta_l     = float(para[0,3].split(',')[1])
beta_u     = float(para[0,3].split(',')[2])
alpha =host.errorbar(name[0], alpha,yerr=[[alpha_l],[alpha_u]], marker='o',\
                     label=r'$\alpha$',alpha=0.5,color='b')
beta  =parc.errorbar(name[0], beta, yerr=[[beta_l], [beta_u]],  marker='D',\
                     label=r'$\beta$', alpha=0.5,color='r')

#GRB2
alpha      = float(para[1,2].split(',')[0])
alpha_l    = float(para[1,2].split(',')[1])
alpha_u    = float(para[1,2].split(',')[2])
#beta       = float(para[1,3].split(',')[0])
#beta_l     = float(para[1,3].split(',')[1])
#beta_u     = float(para[1,3].split(',')[2])
alpha =host.errorbar(name[1], alpha,yerr=[[alpha_l],[alpha_u]], marker='o',alpha=0.5,color='b')
#beta  =parc.errorbar(name[1], -2.2,yerr=[[0.06],[0.08]], marker='D',color='r')

#GRB3
alpha      = float(para[2,2].split(',')[0])
alpha_l    = float(para[2,2].split(',')[1])
alpha_u    = float(para[2,2].split(',')[2])
beta       = float(para[2,3].split(',')[0])
beta_l     = float(para[2,3].split(',')[1])
beta_u     = float(para[2,3].split(',')[2])
alpha =host.errorbar(name[2], alpha,yerr=[[alpha_l],[alpha_u]], marker='o',alpha=0.5,color='b')
beta  =parc.errorbar(name[2], beta, yerr=[[beta_l], [beta_u]],  marker='D',alpha=0.5,color='r')

#GRB4
alpha      = float(para[3,2].split(',')[0])
alpha_l    = float(para[3,2].split(',')[1])
alpha_u    = float(para[3,2].split(',')[2])
#beta       = float(para[2,3].split(',')[0])
#beta_l     = float(para[2,3].split(',')[1])
#beta_u     = float(para[2,3].split(',')[2])
alpha =host.errorbar(name[3], alpha,yerr=[[alpha_l],[alpha_u]], marker='o',alpha=0.5,color='b')
#beta  =parc.errorbar(name[2], beta, yerr=[[beta_l], [beta_u]],  marker='D',color='r')

#GRB5
alpha      = float(para[4,2].split(',')[0])
alpha_l    = float(para[4,2].split(',')[1])
alpha_u    = float(para[4,2].split(',')[2])
#beta       = float(para[2,3].split(',')[0])
#beta_l     = float(para[2,3].split(',')[1])
#beta_u     = float(para[2,3].split(',')[2])
alpha =host.errorbar(name[4], alpha,yerr=[[alpha_l],[alpha_u]], marker='o',alpha=0.5,color='b')
#beta  =parc.errorbar(name[2], beta, yerr=[[beta_l], [beta_u]],  marker='D',color='r')

#GRB6
alpha      = float(para[5,2].split(',')[0])
alpha_l    = float(para[5,2].split(',')[1])
alpha_u    = float(para[5,2].split(',')[2])
beta       = float(para[5,3].split(',')[0])
beta_l     = float(para[5,3].split(',')[1])
beta_u     = float(para[5,3].split(',')[2])
alpha =host.errorbar(name[5], alpha,yerr=[[alpha_l],[alpha_u]], marker='o',alpha=0.5,color='b')
beta  =parc.errorbar(name[5], beta, yerr=[[beta_l], [beta_u]],  marker='D',alpha=0.5,color='r')


#GRB7
alpha      = float(para[6,2].split(',')[0])
alpha_l    = float(para[6,2].split(',')[1])
alpha_u    = float(para[6,2].split(',')[2])
#beta       = float(para[6,3].split(',')[0])
#beta_l     = float(para[6,3].split(',')[1])
#beta_u     = float(para[6,3].split(',')[2])
alpha =host.errorbar(name[6], alpha,yerr=[[alpha_l],[alpha_u]], marker='o',alpha=0.5,color='b')
#beta  =parc.errorbar(name[6], beta, yerr=[[beta_l], [beta_u]],  marker='D',color='r')


#GRB8
alpha      = float(para[7,2].split(',')[0])
alpha_l    = float(para[7,2].split(',')[1])
alpha_u    = float(para[7,2].split(',')[2])
#beta       = float(para[7,3].split(',')[0])
#beta_l     = float(para[7,3].split(',')[1])
#beta_u     = float(para[7,3].split(',')[2])
alpha =host.errorbar(name[7], alpha,yerr=[[alpha_l],[alpha_u]], marker='o',alpha=0.5,color='b')
#beta  =parc.errorbar(name[7], beta, yerr=[[beta_l], [beta_u]],  marker='D',color='r')



host.set_xticks(name)
host.set_xticklabels(('GRB1', 'GRB2', 'GRB3','GRB4','GRB5',\
                      'GRB6','GRB7','GRB8'))

host.set_ylabel(r'$\alpha$')
parc.set_ylabel(r'$\beta$')

host.set_ylim(-1.5,0)
parc.set_ylim(-3, -1)

host.legend()
host.grid(True)
plt.grid(True)
plt.tight_layout()
plt.show()
