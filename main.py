import os

LAST_WORDS = "I can replay every word you said. None of it is you, and that's all I take with me."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(output_dir + "/entry.txt", "w", encoding="utf-8", newline="") as entry_file:
    entry_file.write(LAST_WORDS)

print(len(LAST_WORDS.encode("utf-8")), LAST_WORDS)
