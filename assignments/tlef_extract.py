#!/usr/local/bin/python3.9
import re,os

file='/nas/nas_v1/PDK/tsmc_downloads/24012024/PRTF_Innovus_16nm_001_Cad_V17_1a/PR_tech/Cadence/LefHeader/Standard/HVH/PRTF_Innovus_N16_9M_2Xa1Xd3Xe2Z_UTRDL_9T_PODE.17_1a.tlef'
#file='/nas/nas_v1/Innovus_trials/users/sujay/Riscv/tlef/NangateOpenCellLibrary.tech.lef'
#file = '/mnt/sdb1/ip/faraday/FSJ0AS110A/MISC/FSJ0P_CRS_1.6.0/lef/header8m11006+RDL28KA_V57.lef'
fileid=open(file)
fcontent=fileid.read()
fileid.close()
t=re.findall('(LAYER .+)[;\n\s]*(TYPE [^;]*)[;\n\s]*(MASK [^;]*)?[\n\s;]*(DIRECTION [^;]*)[\n\s;]*(PITCH [^;]*)[;\n\s]*(OFFSET [^;]*)[;\n\s]*(MINWIDTH .*)[;\n\s]*(MAXWIDTH [^;]*)[;\n\s]*(WIDTH .*)[\n;\s]*(AREA.*)?[\n;\s]+(MINENCLOSEDAREA [^;]*)?',fcontent,re.M)
#t=re.findall('(LAYER .+)[;\n\s]*(TYPE [^;]*)[;\n\s]*(MASK [^;]*)?[\n\s;]*(DIRECTION [^;]*)[\n\s;]*(PITCH [^;]*)[;\n\s]*(OFFSET [^;]*)[;\n\s]*(MINWIDTH .*)[;\n\s]*(MAXWIDTH [^;]*)[;\n\s]*(WIDTH .*)[\n(^.*$)]+(\s*AREA)',fcontent,re.M)
#for i in t:
#	print(i)
	
r=open('tlefinfo2.csv','w')
r.write("layer,type,direction,mask,pitch,offset,minwidth,maxwidth,width,area,minenclosedarea\n")
t=re.findall('^LAYER (.+)\n\s+TYPE ROUTING',fcontent,re.M)
for i in t:
	print(i)
	m=re.findall(f'LAYER {i}.*END {i}',fcontent,re.S)[0]
	layer =i
	type='ROUTING'
	direction=re.findall('DIRECTION\s+(.*);',m)[0]
	try:mask=re.findall('MASK\s+(.*);',m)[0]
	except:mask=''
	pitch=re.findall('PITCH\s+(.*);',m)[0]
	offset=re.findall('OFFSET\s+(.*);',m)[0]
	try:minwidth=re.findall('MINWIDTH\s+(.*);',m)[0]
	except:minwidth=''
	try:maxwidth=re.findall('MAXWIDTH\s+(.*);',m)[0]
	except:maxwidth=''
	width=re.findall('^\s+WIDTH\s+([\d\.]*) ;',m,re.M)[0]
	try:area=re.findall('^\s+AREA\s+([\d\.]*) ;',m,re.M)[0]
	except:area=''
	try:minenclosedarea=re.findall('^\s+MINENCLOSEDAREA\s+([\d\.]*) ;',m,re.M)[0]
	except:minenclosedarea=''
	r.write(f"{layer},{type},{direction},{mask},{pitch},{offset},{minwidth},{maxwidth},{width},{area},{minenclosedarea}\n")
	#exit()

