import os
from os import path
import string

class FilePathManager:

  def __init__(self, root_path, batch_name, intermediate_saves=False, keep_unsharp=False) -> None:
    self.root_path = root_path
    self.batch_name = batch_name

    self.allPaths = []

    # general paths
    self.initDirPath = f'{self.root_path}/init_images'
    self.outDirPath = f'{self.root_path}/images_out'
    self.modelPath = f'{self.root_path}/models'
    self.batchFolder = f'{self.outDirPath}/{batch_name}'
    
    self.allPaths.append(self.initDirPath)
    self.allPaths.append(self.modelPath)
    self.allPaths.append(self.outDirPath)
    self.allPaths.append(self.batchFolder)

    self.partialFolder = f'{self.batchFolder}/partials'
    if intermediate_saves:
      self.allPaths.append(self.partialFolder)
    self.unsharpenFolder = f'{self.batchFolder}/unsharpened'
    if keep_unsharp:
      self.allPaths.append(self.keep_unsharp)

    self.createPaths()

  def createPaths(self):
    for path in self.allPaths:
      self.createPath(path)

  def allPaths(self):
    paths = [
      self.initDirPath,
      self.outDirPath,
      self.modelPath,
      self.batchPath
    ]

  def move_files(self, batch_num, start_num, end_num, old_folder, new_folder):
    for i in range(start_num, end_num):
        old_file = old_folder + f'/{self.batch_name}({batch_num})_{i:04}.png'
        new_file = new_folder + f'/{self.batch_name}({batch_num})_{i:04}.png'
        os.rename(old_file, new_file)

  # Simple create paths taken with modifications from Datamosh's Batch VQGAN+CLIP notebook
  def createPath(filepath):
      if path.exists(filepath) == False:
        os.makedirs(filepath)
        print(f'Made {filepath}')
      else:
        print(f'filepath {filepath} exists.')

# def initPaths(root_path='./output'):
#     initDirPath = f'{root_path}/init_images'
#     createPath(initDirPath)
#     outDirPath = f'{root_path}/images_out'
#     createPath(outDirPath)

#     model_path = f'{root_path}/models'
#     createPath(model_path)