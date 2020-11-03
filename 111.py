# rows = 5
# cols = 6

# tab = [[0] * cols for i in range(rows)]

# for row in range(rows):
#     for col in range(cols):
#         tab[row][col] = row * col

# for row in tab:
#     print('\t'.join(map(str, row)))

# _____________________________________________________

# rows = 5
# cols = 6

# tab = [[0] * cols for i in range(rows)]

# index = 0
# for row in range(rows):
#     if row % 2 == 0:
#         for col in range(0, cols):
#             index += 1
#             tab[row][col] = index
#     else:
#          for col in range(cols-1, -1, -1):
#             index += 1
#             tab[row][col] = index


# for row in tab:
#     print('\t'.join(map(str, row)))

# ______________________________________________

