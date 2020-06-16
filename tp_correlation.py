from config import *
from astroML.correlation import two_point 

def tp_corr (out_count,rbin_N):
    path_dir = parent_dir+'output/'
    if os.path.isfile(path_dir+'particle_'+str(out_count)+'.npy'):
        out_data = np.load(path_dir+'particle_'+str(out_count)+'.npy')
        out_info = np.load(path_dir+'info_'+str(out_count)+'.npy',allow_pickle=True).item()
        
        rbin = np.linspace(0.01,x_end,num=rbin_N)

        L = x_end-x_start

        posn = np.transpose(out_data[:,1:4])
        corr = two_point(posn,rbin)
        
        print(np.shape(corr))
        print(corr)

        #plt.figure()
        #plt.scatter(out_data[:,1],out_data[:,2],s=100./N_particles)
        #plt.title('t = '+str(np.round(out_info['t'],4))+' code units')
        #plt.xlim(x_start+wind,x_end-wind)
        #plt.ylim(y_start+wind,y_end-wind)
        #plt.savefig(parent_dir+'Plots/position_'+str(out_count)+'.png')
        #plt.close()

tp_corr(5,10)
