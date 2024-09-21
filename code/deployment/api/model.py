import torch.nn as nn

class CNNClassificationModel(nn.Module):
    def __init__(self, num_classes=2):
        super(CNNClassificationModel, self).__init__()

        self.model = nn.Sequential(
            nn.Conv2d(3, 6, 5),
            nn.BatchNorm2d(6),
            nn.LeakyReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(6, 12, 5),
            nn.BatchNorm2d(12),
            nn.LeakyReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(12, 12, 5),
            nn.BatchNorm2d(12),
            nn.LeakyReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(12, 6, 5),
            nn.BatchNorm2d(6),
            nn.LeakyReLU(inplace=True),
            nn.Flatten(),
            nn.Linear(1596, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(inplace=True),
            nn.Linear(256, 32),
            nn.BatchNorm1d(32),
            nn.LeakyReLU(inplace=True),
            nn.Linear(32, 8),
            nn.BatchNorm1d(8),
            nn.LeakyReLU(inplace=True),
            nn.Linear(8, 1)
        )


    def forward(self, x):
        return self.model(x)
