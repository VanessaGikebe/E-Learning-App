import subprocess
import sys
import json
import os

def check_code_compiles():
    try:
        # Try running all .py files in the repo with "python -m py_compile"
        for root, _, files in os.walk("."):
            for file in files:
                if file.endswith(".py") and file != "rubric_checker.py":
                    subprocess.check_call([sys.executable, "-m", "py_compile", os.path.join(root, file)])
        return True
    except subprocess.CalledProcessError:
        return False

def main(rubric_file):
    with open(rubric_file) as f:
        rubric = json.load(f)

    results = {}
    for criterion in rubric["criteria"]:
        if criterion["id"] == 1:
            passed = check_code_compiles()
            results[criterion["description"]] = "PASS" if passed else "FAIL"

    print("Rubric Results:")
    for k, v in results.items():
        print(f"- {k}: {v}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rubric_checker.py rubric.json")
        sys.exit(1)
    main(sys.argv[1])
