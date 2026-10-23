import torch
import torch.nn as nn

class LinearRegression(nn.Module):
    def __init__(self, in_features: int, out_features: int):
        # TODO: call the parent constructor and register an nn.Linear as self.linear
        super().__init__()
        #self.W = nn.Parameter(torch.randn(out_features, in_features))
        #self.b = nn.Parameter(torch.randn(out_features))
        self.linear = nn.Linear(in_features, out_features)
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: return the output of the linear layer
        #return x @ self.W.T + self.b
        return self.linear(x)
