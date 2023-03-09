# Sample dataset
x = [1, 2, 4, 4, 5]
y = [2, 4, 5, 4, 5]

# Calculate the means of x and y
mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

# Calculate the slope (m)
numerator = 0
denominator = 0
for i in range(len(x)):
    numerator += (x[i] - mean_x) * (y[i] - mean_y)
    denominator += (x[i] - mean_x) ** 2
m = numerator / denominator

# Calculate the y-intercept (b)
b = mean_y - m * mean_x

# Print the slope and y-intercept
print("Slope: ", m)
print("Y-intercept: ", b)
