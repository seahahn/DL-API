from StarGAN.func import ResidualBlock, conv, deconv
import torch
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self, conv_dim=64, c_dim=5):
        super(Generator, self).__init__()

        # Input Data
        self.conv1 = conv(3+c_dim, conv_dim, 7, 1, 3)  # kernel_size, stride, padding

        # Down-Sampling layers
        self.conv2 = conv(conv_dim, conv_dim*2, 4, 2, 1)
        self.conv3 = conv(conv_dim*2, conv_dim*4, 4, 2, 1)

        # Bottleneck layers
        self.res1 = ResidualBlock(dim_in=conv_dim*4, dim_out=conv_dim*4)
        self.res2 = ResidualBlock(dim_in=conv_dim*4, dim_out=conv_dim*4)
        self.res3 = ResidualBlock(dim_in=conv_dim*4, dim_out=conv_dim*4)
        self.res4 = ResidualBlock(dim_in=conv_dim*4, dim_out=conv_dim*4)
        self.res5 = ResidualBlock(dim_in=conv_dim*4, dim_out=conv_dim*4)
        self.res6 = ResidualBlock(dim_in=conv_dim*4, dim_out=conv_dim*4)

        # Up-Sampling layers
        self.deconv1 = deconv(conv_dim*4, conv_dim*2, 4, 2, 1)
        self.deconv2 = deconv(conv_dim*2, conv_dim, 4, 2, 1)
        self.conv4 = conv(conv_dim, 3, 7, 1, 3, In=False, activation=None)
        self.tanh = nn.Tanh()


    def forward(self, x, c):
        c = c.view(c.size(0), c.size(1), 1, 1)
        c = c.repeat(1, 1, x.size(2), x.size(3))
        x = torch.cat([x, c], dim=1)

        # down
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.conv3(out)

        # res
        out = self.res1(out)
        out = self.res2(out)
        out = self.res3(out)
        out = self.res4(out)
        out = self.res5(out)
        out = self.res6(out)

        # up
        out = self.deconv1(out)
        out = self.deconv2(out)
        out = self.conv4(out)
        out = self.tanh(out)

        return out