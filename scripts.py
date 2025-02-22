import logging
import os
import pathlib
import sys

import black
from django.core.management import execute_from_command_line
from isort import main as isort_main
from mypy.main import main as mypy_main

keyboard_top_level_dir = pathlib.Path(__file__).parent
keyboard_pyproject_dir = keyboard_top_level_dir / "pyproject.toml"
keyboard_source_dir = keyboard_top_level_dir / "keyboard_project"

KEYBOARD_SOURCE_DIR = str(keyboard_source_dir)
KEYBOARD_PYPROJECT_FILE = str(keyboard_pyproject_dir)

logging.basicConfig(
    level=logging.INFO, format="%(levelname)-7s %(message)s", stream=sys.stdout
)
logger = logging.getLogger(__name__)


def lint() -> None:
    logger.info("Running isort in %s", KEYBOARD_SOURCE_DIR)
    sys.argv = [
        "isort",
        KEYBOARD_SOURCE_DIR,
        "--check-only",
        "--diff",
    ]
    isort_main.main()
    logger.info("Isort check passed")

    logger.info("Running black in %s", KEYBOARD_SOURCE_DIR)
    sys.argv = [
        "black",
        KEYBOARD_SOURCE_DIR,
        "--config",
        KEYBOARD_PYPROJECT_FILE,
        "--check",
        "--diff",
        "--color",
    ]
    try:
        black.patched_main()
    except SystemExit as e:
        if e.code != 0:
            raise
    logger.info("Black check passed")

    logger.info("Running mypy in %s", KEYBOARD_SOURCE_DIR)

    mypy_main(
        args=[
            KEYBOARD_SOURCE_DIR,
            "--config-file",
            KEYBOARD_PYPROJECT_FILE,
        ],
        clean_exit=True,
    )

    logger.info("Mypy check passed")


def test():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "keyboard_project.settings")
    sys.argv = ["manage.py", "test"]
    execute_from_command_line(sys.argv)
