import sample_data

import pandas as pd

# Define the path to the text file
file_path = "sample_data/yt_product_mkt.txt"

# Read the text file into a list of strings
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Clean up the transcriptions and split them into their components (timestamp, speaker, and text)
transcription_data = []
for line in lines:
    transcription_data.append(line.strip())

# Convert the transcription data into a pandas DataFrame
df = pd.DataFrame(transcription_data, columns=["Text"])

# Display the DataFrame
print(df.head())

#comment master