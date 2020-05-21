
import numpy as np
import pandas as pd
import astropy


def logN2_metallicity(N2):
    iterable = ((8.92+(0.57*np.log10(N2[i]))) for i in range(len(N2)))
    N2_metallicity=np.fromiter(iterable, np.float64)
    return N2_metallicity





gal_info="/Users/sahasika/Dropbox/IGM_spectra/CGMSQ_SFH/python_AG/galaxyinfo.xlsx"
df=pd.read_excel(gal_info)

df.replace(-99, np.nan, inplace=True)
df.replace(99,np.nan,inplace=True)



print('Number of non zero flux values for NII are',np.count_nonzero(~np.isnan(df.NII_flux)))
print('Number of non zero flux values for Halpha are',np.count_nonzero(~np.isnan(df.Halpha_flux)))




print('Indices with nonzero flux values in both are:\n\n ',np.where((~np.isnan(df.Halpha_flux)) & (~np.isnan(df.NII_flux))))

print('\n\nHowever, we need the line quality=1 overlap.')

print('Indices with LQ=1 in both are slghtly less :\n\n',np.where((df.Halpha_LQ==1) & (df.NII_LQ==1)))



#where flux is not nan for either, calculate the ratio, else assign them both nan in this new column N2
df['N2']=np.where((df.NII_LQ ==1) & (df.Halpha_LQ ==1), df['NII_flux']/df['Halpha_flux'],np.nan)


np.count_nonzero(~np.isnan(df.N2))

np.count_nonzero((~np.isnan(df.N2)) & (df.NII_LQ ==1) & (df.Halpha_LQ ==1))



#^same number. this is a good sign that everything is working well.



np.where((~np.isnan(df.N2)) & (df.NII_LQ ==1) & (df.Halpha_LQ ==1))



np.where((~np.isnan(df.N2)))



#onto the check. Simply calculating the value as a basic dataframe operation
df['Z_N2']=(8.92+(0.57*np.log10(df.N2))) 



#for comparison, lets create another column that uses the switchboard func
df['Z_N2_func']=logN2_metallicity(df.N2)

#print the direct result
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df.Z_N2)

#print the switchboard func result
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df.Z_N2_func)


#looks the same to me






