from typing import List
import os
import os.path as osp
import re
import torch
from torch_geometric.data import Dataset, Data

class Alphafold(Dataset):
    def __init__(self, root: str):
        self.root = root
        self.split_file = '/content/drive/MyDrive/protein-DATA/dataset-indices.pt'
        super().__init__(root)

    @property
    def processed_file_names(self) -> List[str]:
        return sorted(
            [f for f in os.listdir(self.root) if f.endswith('.pt')],
            key=lambda x: int(re.findall(r'\d+', x)[0])
        )

    def __len__(self):
        return len(self.processed_file_names)

    def __getitem__(self, idx):
        data_path = osp.join(self.root, self.processed_file_names[idx])
        data = torch.load(data_path)
        return data

    def get_idx_split(self):
        split_dict = torch.load(self.split_file)
        return split_dict