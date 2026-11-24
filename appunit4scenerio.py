
import numpy as np
import pandas as pd

# Create patient details
patients = ["Rahul", "Priya", "Amit", "Sneha", "Riya"]
costs = np.array([15000, 25000, 18000, 35000, 22000])

# Calculate statistics
print("Mean Treatment Cost:", np.mean(costs))
print("Maximum Treatment Cost:", np.max(costs))
print("Minimum Treatment Cost:", np.min(costs))

# Create Pandas DataFrame
df = pd.DataFrame({
    "Patient Name": patients,
    "Treatment Cost": costs
})

print("\nHospital Treatment Details:")
print(df)

# Display patients with cost above 20000
print("\nPatients with Treatment Cost Above 20000:")
print(df[df["Treatment Cost"] > 20000])
