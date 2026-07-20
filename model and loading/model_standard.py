# This file write to produce a biphase Ni alloy model along 001 direction

def addAB(a):
	a=a+1
	if a==2:
		a=0
	return (a)

import numpy as np
n_width=20              # gama phase_channel width *2
Mat = {
	'lat_1':3.52,		# lattice parameter for gama phase
	'lat_2':3.57135,	# lattice parameter for gama1 phase
	}

Mat['n2']=round(Mat['lat_1']/(Mat['lat_2']-Mat['lat_1']))
Mat['n1']=Mat['n2']+1+n_width
len_NiAl=(Mat['n2']*Mat['lat_2']+(Mat['n2']+1)*Mat['lat_1'])/2
Mat['lat_1']=len_NiAl/(Mat['n2']+1)
Mat['lat_2']=len_NiAl/Mat['n2']
len_entire=Mat['n1']*Mat['lat_1']
vol=len_NiAl**3/len_entire**3
print(vol,Mat['n1'],Mat['n2'])

p_0 = {				#list store the information of the first plane
	'no_Ni':0,
	'ar_Ni':np.zeros((3000000,3)),
	}

for i in range(0,Mat['n1']):
	for j in range(0,Mat['n1']):
		p_0['ar_Ni'][p_0['no_Ni']][0]=i*Mat['lat_1']
		p_0['ar_Ni'][p_0['no_Ni']][1]=j*Mat['lat_1']
		p_0['no_Ni']=p_0['no_Ni']+1

		p_0['ar_Ni'][p_0['no_Ni']][0]=(i+0.5)*Mat['lat_1']
		p_0['ar_Ni'][p_0['no_Ni']][1]=(j+0.5)*Mat['lat_1']
		p_0['no_Ni']=p_0['no_Ni']+1


no_Ni_out=0
ar_Ni_out=np.zeros((3000000,3))
jundge=0
disk_z=0
da=n_width/2
dw=da*Mat['lat_1']-0.01
up=len_entire-(da+0.5)*Mat['lat_1']+0.01
a=0
while jundge == 0:
	for i in range(0,p_0['no_Ni']):

		x=p_0['ar_Ni'][i][0]+a*0.5*Mat['lat_1']
		y=p_0['ar_Ni'][i][1]
		z=disk_z
		if x>=len_entire:
			x=x-len_entire

		if (	x > up or x < dw or
				y > up or y < dw or
				z > up or z < dw ):
			ar_Ni_out[no_Ni_out][0]=x
			ar_Ni_out[no_Ni_out][1]=y
			ar_Ni_out[no_Ni_out][2]=z
			no_Ni_out=no_Ni_out+1

	disk_z=disk_z+0.5*Mat['lat_1']
	a=addAB(a)
	if disk_z > len_entire:
		jundge=1

p_1 = {				#list store the information of the first plane
	'no_Ni':0,
	'no_Al':0,
	'ar_Ni':np.zeros((3000000,3)),
	'ar_Al':np.zeros((3000000,3)),
	}

p_2 = {				#list store the information of the second plane
	'no_Ni':0,
	'ar_Ni':np.zeros((3000000,3)),
	}

for i in range(0,Mat['n2']):
	for j in range(0,Mat['n2']):
		p_1['ar_Al'][p_1['no_Al']][0]=i*Mat['lat_2']
		p_1['ar_Al'][p_1['no_Al']][1]=j*Mat['lat_2']
		p_1['no_Al']=p_1['no_Al']+1
		
		if (	(i+0.5)*Mat['lat_2'] < len_NiAl and
			(j+0.5)*Mat['lat_2'] < len_NiAl ):
			p_1['ar_Ni'][p_1['no_Ni']][0]=(i+0.5)*Mat['lat_2']
			p_1['ar_Ni'][p_1['no_Ni']][1]=(j+0.5)*Mat['lat_2']
			p_1['no_Ni']=p_1['no_Ni']+1

for i in range(0,Mat['n2']):
	for j in range(0,Mat['n2']):
		if (j+0.5)*Mat['lat_2'] < len_NiAl :
			p_2['ar_Ni'][p_2['no_Ni']][0]=i*Mat['lat_2']
			p_2['ar_Ni'][p_2['no_Ni']][1]=(j+0.5)*Mat['lat_2']
			p_2['no_Ni']=p_2['no_Ni']+1
			
		if (i+0.5)*Mat['lat_2'] < len_NiAl :
			p_2['ar_Ni'][p_2['no_Ni']][0]=(i+0.5)*Mat['lat_2']
			p_2['ar_Ni'][p_2['no_Ni']][1]=j*Mat['lat_2']
			p_2['no_Ni']=p_2['no_Ni']+1
			

no_Ni_in=0
no_Al_in=0
ar_Ni_in=np.zeros((3000000,3))
ar_Al_in=np.zeros((3000000,3))
jundge=0
disk_z=0
layer_no=1
a=0
dis=da*Mat['lat_1']
while jundge==0:
	if a == 0:
		for i in range(0,p_1['no_Ni']):
			no_Ni_in=no_Ni_in+1
			ar_Ni_in[no_Ni_in-1][0]=p_1['ar_Ni'][i][0]+dis
			ar_Ni_in[no_Ni_in-1][1]=p_1['ar_Ni'][i][1]+dis
			ar_Ni_in[no_Ni_in-1][2]=disk_z+dis
		for i in range(0,p_1['no_Al']):
			no_Al_in=no_Al_in+1
			ar_Al_in[no_Al_in-1][0]=p_1['ar_Al'][i][0]+dis
			ar_Al_in[no_Al_in-1][1]=p_1['ar_Al'][i][1]+dis
			ar_Al_in[no_Al_in-1][2]=disk_z+dis

	else:
		for i in range(0,p_2['no_Ni']):
			no_Ni_in=no_Ni_in+1
			ar_Ni_in[no_Ni_in-1][0]=p_2['ar_Ni'][i][0]+dis
			ar_Ni_in[no_Ni_in-1][1]=p_2['ar_Ni'][i][1]+dis
			ar_Ni_in[no_Ni_in-1][2]=disk_z+dis

	if disk_z > len_NiAl-Mat['lat_2']+0.1:
		jundge=1
	disk_z=disk_z+0.5*Mat['lat_2']
	a=addAB(a)

print(no_Ni_out,no_Ni_in,no_Al_in)
# write down the data file
# orientation_misfit_V
filename = '001_14_47'

with open(filename,'w') as fid:
	fid.write('#LAMMPS Ni/Ni3Al at 001 direction;x axis is 100 direction and y axis is 010 direction\n')
	fid.write(str(no_Ni_out+no_Ni_in+no_Al_in)+' atoms\n\n')
	fid.write('3 atom types\n\n')
	fid.write(str('%e'%0)+'  '+str('%e'%len_entire)+'  '+'xlo xhi\n')
	fid.write(str('%e'%0)+'  '+str('%e'%len_entire)+'  '+'ylo yhi\n')
	fid.write(str('%e'%0)+'  '+str('%e'%len_entire)+'  '+'zlo zhi\n\n')
	fid.write('Masses\n\n')
	fid.write('1 '+str('%e'%58.6934)+'\n')
	fid.write('2 '+str('%e'%58.6934)+'\n')
	fid.write('3 '+str('%e'%26.9815)+'\n\n')
	fid.write('Atoms\n\n')
	for i in range(0,no_Ni_out):
		fid.write(str(i+1)+' 1 '+str('%e'%ar_Ni_out[i][0])+' '+str('%e'%ar_Ni_out[i][1])+' '+str('%e'%ar_Ni_out[i][2])+'\n')    
	for i in range(0,no_Ni_in):
		fid.write(str(i+no_Ni_out+1)+' 2 '+str('%e'%ar_Ni_in[i][0])+' '+str('%e'%ar_Ni_in[i][1])+' '+str('%e'%ar_Ni_in[i][2])+'\n')    
	for i in range(0,no_Al_in):
		fid.write(str(i+1+no_Ni_out+no_Ni_in)+' 3 '+str('%e'%ar_Al_in[i][0])+' '+str('%e'%ar_Al_in[i][1])+' '+str('%e'%ar_Al_in[i][2])+'\n')    
fid.close()    





