import subprocess

# Run checkstyle on a Java file
result = subprocess.run(["checkstyle", "example.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Extract the output from checkstyle
output = result.stdout.decode("utf-8")

# Write the output to a file
with open("checkstyle_report.txt", "w") as f:
    f.write(output)

# Print the number of linting issues found
issues = output.count("\n")
print("Number of linting issues found:", issues)
