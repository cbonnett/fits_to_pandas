from astropy.io import fits
import pandas as pd 
import numpy as np
def fits_to_pandas(fits_file):
    """
    """
    fits_data = fits.open(fits_file)
    names = fits_data[1].columns.names
    nrow = len(fits_data[1].data[fits_data[1].columns.names[0]])
    df = pd.DataFrame(columns = names)
    for name in names:
        df[name] = fits_data[1].data[name].byteswap().newbyteorder()
    df_final = pd.concat([df[ser] for ser in df.columns], axis=1).reset_index()
    return df_final