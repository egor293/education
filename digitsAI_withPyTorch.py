import torch as pt
import torch.nn as nn

digits = pt.tensor([
[1,1,1, 1,0,1, 1,0,1, 1,0,1, 1,1,1],  # 0
[0,1,0, 1,1,0, 0,1,0, 0,1,0, 1,1,1],  # 1
[1,1,1, 0,0,1, 1,1,1, 1,0,0, 1,1,1],  # 2
[1,1,1, 0,0,1, 1,1,1, 0,0,1, 1,1,1],  # 3
[1,0,1, 1,0,1, 1,1,1, 0,0,1, 0,0,1],  # 4
[1,1,1, 1,0,0, 1,1,1, 0,0,1, 1,1,1],  # 5
[1,1,1, 1,0,0, 1,1,1, 1,0,1, 1,1,1],  # 6
[1,1,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1],  # 7
[1,1,1, 1,0,1, 1,1,1, 1,0,1, 1,1,1],  # 8
[1,1,1, 1,0,1, 1,1,1, 0,0,1, 1,1,1],  # 9
], dtype=pt.float32)

targets = pt.arange(10)
epochs = 2001

model = nn.Sequential(
    nn.Linear(15, 20),
    nn.ReLU(),
    nn.Linear(20, 10)
)

criterion = nn.CrossEntropyLoss()
optimizer = pt.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(epochs):
    optimizer.zero_grad()
    output = model(digits)
    loss = criterion(output, targets)
    loss.backward()
    optimizer.step()

    if epoch % 500 == 0:
        print(f"epoch {epoch}  loss {loss.item():.4f}")        







# GUI
