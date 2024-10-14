def get_vector_input(prompt):
    while True:
        try:
            vector = list(map(float, input(prompt).split()))
            return vector
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")

def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def main():
    print("Enter the elements of the first vector:")
    vector1 = get_vector_input("Vector 1: ")

    vector2 = get_vector_input("Vector 2: ")

    if len(vector1) != len(vector2):
        print("Error: Vectors must be of the same length.")
        return

    result = dot_product(vector1, vector2)
    print("Dot Product:")
    print(f"{result}")

if __name__ == "__main__":
    main()
