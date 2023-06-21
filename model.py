import torch
import torch.nn as nn
import torch.nn.functional as F


class MainModel(nn.Module):
    def __init__(self,num_classes):
        super().__init__()
        self.num_classes=num_classes

        blocks = []
        for i in range(3):
            if i==0:
                in_ch_ = 1
                num_conv_filter = 64
                stride=1
            elif i==1:
                in_ch_ = 64
                num_conv_filter = 64
                stride=2
            elif i==2:
                in_ch_ = 64
                num_conv_filter = 64
                stride=3

            blocks.append(
                nn.Sequential(
                    nn.Conv2d(in_ch_, num_conv_filter,
                              kernel_size=(5, 3), padding=(0, 0), stride=stride),
                    nn.Dropout(p=0.5),
                    nn.BatchNorm2d(num_conv_filter),
                    nn.ReLU(),
                )
            )
        self.conv_blocks = nn.ModuleList(blocks)



        self.conv_out=nn.Conv2d(num_conv_filter, 1, kernel_size=1, stride=1, padding=0)
        
        self.relu=nn.ReLU()
        self.linear1=nn.Linear(20*32,64)
        self.linear2=nn.Linear(64,10)
        self.linear3=nn.Linear(10,self.num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        input: tensor (batch ,1, 256 , t)
        output: tensor (batch , num_classes)
        """

        for block in self.conv_blocks:
            x=block(x)
        
        x=self.conv_out(x)

        x=torch.reshape(x,(x.shape[0],-1))
        x=self.linear1(x)
        x=self.relu(x)
        x=self.linear2(x)
        # x=self.relu(x)
        # x=self.linear3(x)

        return x

