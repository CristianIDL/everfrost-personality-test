'''
src.create_dataset.py: generate a dataset of personality vectors based ranges defined in vector_config.py 
'''

from src.vector_config import ASTROFUSIONER, ESSENTROMANCER, INTERGRAPH, QUESTIONS
import os
import pandas as pd
import random

# Function to generate a personality vector based on target profile
def generate_personality_vector(target):
    vector = []
    # Iterate through each question and generate a value within the specified bounds
    for key in QUESTIONS.keys():
        bounds = target[key]
        value = round(random.uniform(bounds[0], bounds[1]), 2)
        vector.append(value)
    print(vector)
    return vector

def create_dataset(num_samples=30):
    class_profiles = {
        "Astrofusioner": ASTROFUSIONER,
        "Essentromancer": ESSENTROMANCER,
        "Intergraph": INTERGRAPH
    }

    data_rows = []

    for class_name, profile in class_profiles.items():
        for _ in range(num_samples):
            # Generate personality vector for the given profile
            vector = generate_personality_vector(profile)
            # Append the vector and class label at the end
            row = vector + [class_name]
            # Append to data rows
            data_rows.append(row)

    # Create DataFrame column names
    feature_names = list(QUESTIONS.keys())
    columns = feature_names + ["class_label"]

    # Create DataFrame
    df = pd.DataFrame(data_rows, columns=columns)
    return df

if __name__ == "__main__":
    print("Generating dataset...")

    df = create_dataset(num_samples=30)

    # Create folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Save to CSV
    df.to_csv("data/personality_dataset.csv", index=False)

    print(df.head())
    print("Dataset saved to data/personality_dataset.csv")
