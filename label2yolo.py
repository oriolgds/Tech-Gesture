import subprocess

# Running a simple command
result = subprocess.run('labelme2yolo --json_dir datasets/coco/labels', capture_output=True, text=True, shell=True)

# Capturing the output and error messages
print(result.stdout)
print("Errors:")
print(result.stderr)
