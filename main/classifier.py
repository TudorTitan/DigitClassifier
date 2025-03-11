import torch
import torch.nn as nn#images are 28x28
import numpy as np


class Flatten(torch.nn.Module):
    def forward(self, x):
        batch_size = np.prod(x.shape[1:])
        return x.view(-1,batch_size)


model = nn.Sequential(nn.Conv2d(in_channels=1,out_channels=64,kernel_size=(3,3),stride = (1,1)),
          nn.ReLU(),
          nn.MaxPool2d(2,2),
          nn.Dropout(0.3),
          nn.Conv2d(in_channels=64,out_channels=64,kernel_size=(3,3),stride = (1,1), padding = 1),
          nn.ReLU(),
          nn.MaxPool2d(2,2),
          nn.Dropout(0.3),
          nn.Conv2d(in_channels=64,out_channels=32,kernel_size=(3,3),stride = (1,1), padding = 1),
          nn.ReLU(),
          nn.MaxPool2d(2,2),
          nn.Dropout(0.3),
          Flatten(),
          nn.Linear(288,128),
          nn.ReLU(),
          nn.Linear(128,10),
          nn.LogSoftmax(),
)

def load_model():
    model.load_state_dict(torch.load("model",weights_only=True))
    model.eval()
    return model

#224*224 white on black image as input
def predict(image):
    image = image.reshape(28,8,28,8).mean(axis = 1).mean(axis = 2)
    im28_28 = np.array([[image/255]])
    with torch.no_grad():
        pred = model(torch.tensor(im28_28,dtype=torch.float32))
    return str(torch.argmax(pred).numpy()), str(np.exp(torch.max(pred).numpy()))