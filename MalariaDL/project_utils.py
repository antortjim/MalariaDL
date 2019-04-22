import os
import glob
import numpy as np
import pandas as pd
np.random.seed(42)

from MalariaDL import ROOT_DIR
print(ROOT_DIR)


def build_dataframe(images_dir='cell_images'):
    base_dir = os.path.join(ROOT_DIR, images_dir)
    infected_dir = os.path.join(base_dir,'Parasitized')
    healthy_dir = os.path.join(base_dir,'Uninfected')
    print(infected_dir)
    
    infected_files = glob.glob(infected_dir+'/*.png')
    healthy_files = glob.glob(healthy_dir+'/*.png')
    print(
    len(infected_files), len(healthy_files)
    )
    
    files_df = pd.DataFrame({
        'filename': infected_files + healthy_files,
        'label': ['malaria'] * len(infected_files) + ['healthy'] * len(healthy_files)
    }).sample(frac=1, random_state=42).reset_index(drop=True)
    
    return files_df
