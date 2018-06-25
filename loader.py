import torch.utils.data
import os


class FontLoader(torch.utils.data.Dataset):
  def __init__(self, transform = None):
    self.transform = transform
    for path, dir, files in os.walk("C:\\windows\\fonts"):
      for file in files:
        if file.endswith(".ttf"):
            self.fonts.append(file) 

  def __len__(self):
    return len(self.fonts) * self.size

  def __getitem__(self, i):
    idx = i % len(self.fonts)
    word = self.texts[i]
    img = make_img(word, self.fonts[idx])
    if self.transform:
      img = self.transform(img)
    return img, idx
