# Sample dataset
x1 = [1, 2, 3, 4, 5]
x2 = [3, 5, 6, 8, 9]
y = [5, 7, 8, 9, 10]

# Calculate the means of x1, x2 and y
mean_x1 = sum(x1) / len(x1)
mean_x2 = sum(x2) / len(x2)
mean_y = sum(y) / len(y)

# Calculate the coefficients (m1, m2, b)
numerator = 0
denom_x1 = 0
denom_x2 = 0
for i in range(len(x1)):
    numerator += (x1[i] - mean_x1) * (y[i] - mean_y)
    denom_x1 += (x1[i] - mean_x1) ** 2
    denom_x2 += (x2[i] - mean_x2) ** 2
m1 = numerator / denom_x1
m2 = numerator / denom_x2
b = mean_y - (m1 * mean_x1) - (m2 * mean_x2)

# Print the coefficients
print("Coefficient 1: ", m1)
print("Coefficient 2: ", m2)
print("Intercept: ", b)
