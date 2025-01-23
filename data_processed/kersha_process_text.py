# Example Metric: Count the number of lines
text_file = 'fetch_scripts/data.txt'  # Replace with your actual text file path
with open(text_file, 'r') as file:
    lines = file.readlines()

line_count = len(lines)

# Save Result
with open('data_processed/processed_text.txt', 'w') as file:
    file.write(f"Line Count: {line_count}\n")

print("Text file processed and saved in data_processed/processed_text.txt")
