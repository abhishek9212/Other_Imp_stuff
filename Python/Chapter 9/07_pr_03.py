for i in range(2, 21):
    for j in range(1, 11):
        if j == 1:
            with open(f'tables/{i}_table.txt', 'w') as f:
                f.write(f'{i} x {j} = {i*j}')
        else:
             with open(f'tables/{i}_table.txt', 'a') as f:  # tables/ to go inside the folder
                f.write(f'\n{i} x {j} = {i*j}')