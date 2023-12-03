# With using Built-in Methods.
a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

first_step = set(a)

second_step = list(first_step)

print(second_step)

# With using for Loop

a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
ans = []
for i in a:
  if i not in ans:
    ans.append(a)
print(ans)
