from config import *
from astroML.correlation import two_point 

def tp_corr (out_count,rbin_N):
    path_dir = parent_dir+'output/'
    if os.path.isfile(path_dir+'particle_'+str(out_count)+'.npy'):
        out_data = np.load(path_dir+'particle_'+str(out_count)+'.npy')
        out_info = np.load(path_dir+'info_'+str(out_count)+'.npy',allow_pickle=True).item()
        
        rbin = np.logspace(0.5,2.5,num=rbin_N)

        posn = out_data[:,1:4]
        corr = two_point(posn,rbin)
        
        print(np.shape(corr))
        print(corr)
        rbin = rbin[:-1]
        print(np.shape(rbin))

        plt.figure()
        plt.xscale('log')
        plt.yscale('log')
        plt.plot(rbin,corr)
        plt.title('With expansion: 10000 particles')
        plt.xlabel(r'r (in code units)')
        plt.ylabel(r'$\xi$(r)')
        plt.savefig(parent_dir+'two_point_corr_'+str(out_count)+'.png')
        plt.close()

tp_corr(180,100)
