from src.vector_config import QUESTIONS

def get_user_answers():

    user_answers = {}
    for key, value in list(QUESTIONS.items()):
        print(f"Which term suits you best: {value}")
        user_answers[key] = float(input("Enter a value from -1 to 1 (e.g. 0.5): "))
    
    return user_answers

def vector_converter(answers_dict):
    vector = []
    for key in QUESTIONS.keys():
        vector.append(answers_dict[key])
    return vector

if __name__ == "__main__":

    print(f"This version of the test contains {len(QUESTIONS)} questions.")
    answers = get_user_answers()
    vector = vector_converter(answers)

    print("Your answers:", answers)
    print("Your personality vector:", vector)