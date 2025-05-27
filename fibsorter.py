import os
import shutil

def fibonacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def sort_music_fibonacci(path):
    files = [f for f in os.listdir(path) if f.endswith('.mp3') or f.endswith('.wav')]
    files.sort()  # Sort alphabetically first

    fib_seq = fibonacci(len(files))
    sorted_files = [x for _, x in sorted(zip(fib_seq, files))]

    for i, file in enumerate(sorted_files):
        new_name = f"{i+1:03d}_{file}"
        shutil.move(os.path.join(path, file), os.path.join(path, new_name))

    print("Files sorted in Fibonacci order.")

# Example: Sort files in the "music" folder
sort_music_fibonacci(r"Music")
