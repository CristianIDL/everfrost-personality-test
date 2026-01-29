'''
src.create_dataset.py: generate a dataset of personality vectors based ranges defined in vector_config.py 
'''

from src.vector_config import ASTROFUSIONER, ESSENTROMANCER, INTERGRAPH, QUESTIONS
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


if __name__ == "__main__":
    print("Generating personality dataset...")
    print("Generating Astrofusioner personality vector:")
    generate_personality_vector(ASTROFUSIONER)
    print("Generating Essentromancer personality vector:")
    generate_personality_vector(ESSENTROMANCER)
    print("Generating Intergraph personality vector:")
    generate_personality_vector(INTERGRAPH)