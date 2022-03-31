import h5py
import numpy as np
from core.helpers import *

class HDF5:
    def __init__(self, filepath):
        if (not os.path.exists(filepath)):
            self.hdf = h5py.File(filepath, "w")
        self.hdf = h5py.File(filepath, "a")
        self.filepath = filepath

    def save_text_items(self, data_path, kv_items):
        """Stores items from dictionary in hdf5

        Args:
            data_path (string): Path to dataset in hdf5
            kv_items (dict): Key value dictionary
        """
        dt = h5py.string_dtype(encoding='utf-8')
        
        if (data_path not in self.hdf):
            dset = self.hdf.create_dataset(data_path, (100,100), dtype=dt)
        else:
            dset = self.hdf[data_path]
        
        for k, v in kv_items.items():
            if (v):
                binary_blob = bytes(v, encoding='utf-8')
                dset.attrs[k] = np.void(binary_blob)
        
    def get_text_item(self, data_path, attr):
        dset = self.hdf[data_path]
        out = dset.attrs[attr]
        binary_blob = out.tostring()
        return str(binary_blob)
    