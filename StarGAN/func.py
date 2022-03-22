import torch.nn as nn

### 코드 단순화를 위한 함수들을 정의

class ResidualBlock(nn.Module):
    def __init__(self, dim_in, dim_out):
        super(ResidualBlock, self).__init__()
        self.main = nn.Sequential(
            nn.Conv2d(dim_in, dim_out, kernel_size=3, stride=1, padding=1, bias=False),
            nn.InstanceNorm2d(dim_out, affine=True, track_running_stats=True),
            nn.ReLU(inplace=True),
            nn.Conv2d(dim_out, dim_out, kernel_size=3, stride=1, padding=1, bias=False),
            nn.InstanceNorm2d(dim_out, affine=True, track_running_stats=True))

    def forward(self, x):
        return x + self.main(x)


def conv(c_in, c_out, k_size, stride=2, pad=1, In=True, activation='relu'):
    layers = []

    # Conv.
    layers.append(nn.Conv2d(c_in, c_out, k_size, stride, pad, bias=False))

    # Instance Norm
    if In:
        layers.append(nn.InstanceNorm2d(c_out, affine=True, track_running_stats=True))

    # Activation
    if activation == 'lrelu':
        layers.append(nn.LeakyReLU(0.01))
    if activation == 'tanh':
        layers.append(nn.Tanh())
    if activation == 'relu':
        layers.append(nn.ReLU(inplace=True))
    if activation == 'none':
        pass

    return nn.Sequential(*layers)


def deconv(c_in, c_out, k_size, stride=2, pad=1, In=True, activation='relu'):
    layers = []

    # Deconv.
    layers.append(nn.ConvTranspose2d(c_in, c_out, k_size, stride, pad, bias=False))

    if In:
        layers.append(nn.InstanceNorm2d(c_out, affine=True, track_running_stats=True))

    # Activation
    if activation == 'lrelu':
        layers.append(nn.LeakyReLU(0.01))
    if activation == 'tanh':
        layers.append(nn.Tanh())
    if activation == 'relu':
        layers.append(nn.ReLU(inplace=True))
    if activation == 'none':
        pass

    return nn.Sequential(*layers)


def denorm(x):
    out = (x+1)/2
    return out.clamp_(0, 1)