import capsta as cp

state = input("Enter state name: ")
st = state.upper()
result = cp.capital.get(st)
print(f"{st} : {result}")