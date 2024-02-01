import os
from PIL import Image
from torch.utils.data import Dataset

class PigpenDatasetClass(Dataset):
    def __init__(self, directory, transform=None):
        self.directory = directory
        self.transform = transform
        self.classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-']
        self.images = []
        for cls in self.classes:
            cls_dir = os.path.join(directory, cls)
            self.images += [(os.path.join(cls_dir, img), cls) for img in os.listdir(cls_dir) if os.path.isfile(os.path.join(cls_dir, img))]

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path, cls = self.images[idx]
        image = Image.open(img_path).convert('L')
        if self.transform:
            image = self.transform(image)
        return image, self.classes.index(cls)
