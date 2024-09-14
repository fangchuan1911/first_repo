__23__knicks = {"Brunson", "Anunoby", "Robinson", "Bridges", "Hart"}
__24__knicks = {"Brunson", "Anunoby", "Hartenstein", "DiVincenzo", "Hart"}

# print(__23__knicks.difference(__24__knicks))

less_knicks = __24__knicks.pop()
# print(less_knicks)
# print(__24__knicks)

more_knicks = __23__knicks.union(__24__knicks)
# print(more_knicks)

# print(help(more_knicks))
print(len(more_knicks))






