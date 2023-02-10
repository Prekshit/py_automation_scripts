import pandas as pd
import matplotlib.pyplot as plt

# Read test data from a CSV file
data = pd.read_csv("test_data.csv")

# Calculate the pass rate of the tests
pass_rate = (data["status"] == "pass").mean()

# Plot a bar chart showing the number of passes and failures
data["status"].value_counts().plot(kind="bar")
plt.title("Test Results")
plt.xlabel("Status")
plt.ylabel("Count")

# Print the overall pass rate
print("Overall pass rate: {:.2f}%".format(pass_rate * 100))

# Save the report as a PDF file
plt.savefig("test_report.pdf")
