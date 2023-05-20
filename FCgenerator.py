import matplotlib.pyplot as plt
import numpy as np
from astroquery.skyview import SkyView
from astropy.io.fits import getheader
from astropy.utils.data import get_pkg_data_filename

# Read the configuration file
file = open('config.txt', 'r')
# Read info in the top
print('Required info in the config file:')
for i in range(0,6):
    a = file.readline()
    #print(a, end="")
file.readline()
nfcs = int(file.readline())
print('Number of finding charts: ',nfcs)
fov = float(file.readline())
RunID = file.readline()
PI = file.readline()
file.readline()
file.readline()
Object = []
RAtxt = []
DECtxt = []
for i in range(0,nfcs):
    line = file.readline()
    columns = line.split()
    Object.append(columns[0])
    RAtxt.append(columns[1])
    DECtxt.append(columns[2])

xsize = 282  #hardwired 8 arcmin
ysize = 282
cm = 1/2.54

for i in range(0,nfcs):
#Get the image
   img = SkyView.get_images(position=RAtxt[i]+','+DECtxt[i],survey=['DSS'],pixels=str(xsize)+','+str(ysize),coordinates='J2000',grid=True,gridlabels=True)

   tmp = img[0][0].data
   img2 = np.zeros((ysize+71,xsize),float)
   img2[71:282+71,0:282] = tmp[0:282,0:282]

   plt.figure(figsize=(19*cm,19*cm*(282.+71.)/282.), dpi=600)
   plt.tight_layout()
   plt.imshow(img2, cmap='gray_r',vmax=np.max(img[0][0].data)*.65,vmin=np.min(img[0][0].data)*.45)
   ax = plt.gca()
   ax.xaxis.set_tick_params(labelbottom=False)
   ax.yaxis.set_tick_params(labelleft=False)
   ax.set_xticks([])
   ax.set_yticks([])
   #Draw arrow to center
   ax.annotate("", xy=(141, 141+71), xytext=(121, 121+71),
               arrowprops=dict(arrowstyle="->", color='r'), color='white')
   #Scale of image 
   plt.axhline(y=70.5, linestyle='-', color='black')
   plt.annotate('60 arcsec',  xy = (7,(282+71)-307), fontsize=9)
   plt.plot( [5,5+35] , [(282+71)-305, (282+71)-305], color='black')
   plt.plot( [5,5] , [(282+71)-305-2, (282+71)-305+2], color='black')
   plt.plot( [5+35,5+35] , [(282+71)-305-2, (282+71)-305+2], color='black')
   #Write text 
   plt.annotate('RA(J2000.0)  ='+RAtxt[i], xy = (180,(282+71)-340), fontsize=9)
   plt.annotate('Dec(J2000.0)  ='+DECtxt[i], xy = (180,(282+71)-330), fontsize=9)
   plt.annotate('Run ID: '+RunID, xy = (5,(282+71)-340), fontsize=9)
   plt.annotate('PI: '+PI, xy = (5,(282+71)-330), fontsize=9)
   plt.annotate('Target: '+Object[0],  xy = (5,(282+71)-320), fontsize=9)
   plt.annotate('8x8 armin^2, East left, North up',  xy = (5,(282+71)-290), fontsize=9)
   #Draw field of view
   length = fov*60./1.7
   plt.plot( [141-length/2, 141+length/2], [141+70.5-length/2,141+70.5-length/2], linestyle='dashed', color='red')
   plt.plot( [141-length/2, 141+length/2], [141+70.5+length/2,141+70.5+length/2], linestyle='dashed', color='red')
   plt.plot( [141-length/2, 141-length/2], [141+70.5-length/2,141+70.5+length/2], linestyle='dashed', color='red')
   plt.plot( [141+length/2, 141+length/2], [141+70.5-length/2,141+70.5+length/2], linestyle='dashed', color='red')
   #Save to file
   plt.savefig('FC_'+Object[i]+'.jpg', format='jpg')
