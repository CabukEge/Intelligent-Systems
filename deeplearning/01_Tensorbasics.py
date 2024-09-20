import torch
import numpy as np

#1:

th_tensor = torch.tensor([[1.], [2.], [3.]])
#Begin eurer Lösung:
print("Tensor dim: ", th_tensor.dim(), "Tensor shape: ", th_tensor.shape, "Tensor dtype: ", th_tensor.dtype)

#2:

th_batched_matrices = torch.arange(1,91).reshape([10,3,3])
# Begin eurer Lösung:
print("1:")
print(th_batched_matrices[0])
print(th_batched_matrices[-1])

print("2:")
print(th_batched_matrices[0])
print(th_batched_matrices[1])

print("3:")
print(th_batched_matrices[0:91,0:2,0:2])

print("4:")
print(th_batched_matrices[0:91,0:3,2:3])

#3:

th_batched_matrices = torch.arange(-45,45).reshape([10,3,3])

# Begin eurer Lösung:
print(th_batched_matrices[4])
print(th_batched_matrices[5])

mask = th_batched_matrices < 0
print("Form der Maskeneinträge:", mask.shape)
print("Datentyp der Maskeneinträge:", mask.dtype)

th_batched_matrices[mask] = 0

print(th_batched_matrices[4])
print(th_batched_matrices[5])


#4:

th_batched_matrices = torch.arange(-45,45).reshape([10,3,3])

# Begin eurer Lösung:
mask = th_batched_matrices % 2 == 0

y = th_batched_matrices[mask]
y = y.reshape([5,3,3])
print(y)


#5:

th_tensor1 = torch.ones([2,2])
th_tensor2 = torch.full([2,2], 2)
constant = 10.0

#Begin eurer Lösung

print(th_tensor1[0:3] + th_tensor2[0:3])
print(th_tensor1[0:3] + constant)

print(-th_tensor1[0:3] + th_tensor2[0:3])
print(-th_tensor1[0:3] + constant)

print(th_tensor1[0:3] * th_tensor2[0:3])
print(th_tensor1[0:3] * constant)

print(th_tensor1[0:3] / th_tensor2[0:3])
print(th_tensor1[0:3] / constant)

