#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes a single warm, heartfelt family scene (1-2 lines) to
/output/entry.txt. The scene is a small domestic moment with a
specific, fresh detail and light, recognisable humour.
"""

import os

SCENE = "Mom always took the burnt edge of every birthday cake, swearing it was the best part \u2014 we only realized last year she was saving the good slices for us."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
