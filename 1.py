import torch

# 检查CUDA是否可用
if torch.cuda.is_available():
    # 设置CUDA设备
    device = torch.device("cuda:0")  # 使用第一个GPU
    # 或者使用多个GPU：device = torch.device("cuda:0,1,2,3")
else:
    device = torch.device("cpu")

