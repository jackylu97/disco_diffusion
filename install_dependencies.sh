git clone https://github.com/openai/CLIP
git clone https://github.com/crowsonkb/guided-diffusion
git clone https://github.com/assafshocher/ResizeRight.git
pip install -e ./CLIP
pip install -e ./guided-diffusion
pip install lpips datetime timm
# apt install imagemagick
git clone https://github.com/CompVis/latent-diffusion.git
git clone https://github.com/CompVis/taming-transformers
pip install -e ./taming-transformers
pip install omegaconf>=2.0.0 pytorch-lightning>=1.0.8 torch-fidelity einops wandb

pip install opencv-python