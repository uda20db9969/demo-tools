"""Scratch module."""

def flatten(xs):
    return [y for x in xs for y in x]

def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]

if __name__ == "__main__":
    print(clamp(6, 0, 6))
