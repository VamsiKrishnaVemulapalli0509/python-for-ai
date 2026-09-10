# Complete Python script demonstrating list operations and safe modifications

def main():

    # --- Task List Initialization & Modification ---

    tasks = ["Install Python", "Create venv", "Learn lists", "Practice Python"]

    print(f"Initial tasks: {tasks}")

    # Append a new task

    tasks.append("Build Project")

    

    # Insert a task at a specific index

    tasks.insert(1, "Setup IDE")

    

    # Remove a specific task

    removed_task = tasks.pop(tasks.index("Create venv"))

    

    print(f"Updated tasks: {tasks}")

    print(f"Removed task: {removed_task}")

    # --- List Inspection ---

    print(f"List Length: {len(tasks)}")

    print(f"Contains 'Learn lists': {'Learn lists' in tasks}")

    if "Learn lists" in tasks:

        print(f"Index of 'Learn lists': {tasks.index('Learn lists')}")

    

    # Repeated item count

    sample_items = ["python", "ai", "python", "data"]

    print(f"Count of 'python': {sample_items.count('python')}")

    # --- Copy Experiment ---

    scores = [88, 92, 75, 99, 61]

    scores.sort()

    scores.reverse()

    

    scores_copy = scores.copy()

    scores_copy.append(100)

    

    print(f"Original Scores: {scores}")

    print(f"Copied Scores: {scores_copy}")

if __name__ == "__main__":

    main()
