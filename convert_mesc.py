import h5py
import tifffile
import numpy as np
from pathlib import Path

def convert_mesc_to_tiff(mesc_path, output_dir="processed"):
    #to make a dir for outs
    Path(output_dir).mkdir(exist_ok=True)
    
    with h5py.File(mesc_path, 'r') as f:
        session = f['MSession_0']
        
        for unit_name, unit in session.items():
            if not isinstance(unit, h5py.Group):
                continue
            
            if 'Channel_0' in unit:
                data = unit['Channel_0'][()]
                output_path=f"{output_dir}/{unit_name}_Channel_0.tiff"
                
                if data.dtype != np.uint16:
                    data=(data-data.min())/ (data.max()-data.min()) * 65535
                    data = data.astype(np.uint16)
                
                tifffile.imwrite(output_path,data)
                print(f"Saved {output_path} (Shape: {data.shape})")
if __name__ == "__main__":
    convert_mesc_to_tiff("2025-07-02-Amouse-invivo-GCaMP6f.mesc")
    
    