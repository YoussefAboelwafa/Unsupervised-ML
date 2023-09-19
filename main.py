import numpy as np
import pandas as pd

# Generate 200 2D points
np.random.seed(0)
n_points = 200
X = np.random.randint(0, 100, size=(n_points, 2))

# Create a DataFrame with the coordinates
df = pd.DataFrame(X, columns=['X', 'Y'])

# Save to a CSV file
csv_filename = 'points_coordinates.csv'
df.to_csv(csv_filename, index=False)

print(f'CSV file saved as {csv_filename}')
