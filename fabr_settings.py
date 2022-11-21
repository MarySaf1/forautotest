import os.path
from pathlib import Path


PROJECT_DIR = str(Path(__file__).parent)
TEST_TXT_FILE = os.path.join(PROJECT_DIR, "file_example.txt")