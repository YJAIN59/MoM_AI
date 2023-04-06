import docx2txt
import pandas as pd

# Read the docx file using docx2txt library
text = docx2txt.process(r"D:\ML\MoM_AI\sample_data\Communication_Training.docx")

# print(text)
# Split the text into lines
lines = text.split('\n')

# Create an empty dataframe with three columns
df = pd.DataFrame(columns=["start_time", "end_time", "Speaker", "Text"])

# Loop through the lines and extract the information
for i in range(0, len(lines), 4):
    # Extract the timestamp, speaker, and text information
    timestamp = lines[i]
    speaker = lines[i + 1]
    text = lines[i + 2]

    # Split the timestamp into start and end times
    start_time, end_time = timestamp.split(" --> ")

    # Add the information to the dataframe
    df = df.append({"start_time": start_time.strip(), "end_time": end_time.strip(), "Speaker": speaker.strip(),
                    "Text": text.strip()}, ignore_index=True)

# Print the dataframe
df.to_csv("D:\ML\MoM_AI\sample_data\converted_data\converted.csv")
print(df)