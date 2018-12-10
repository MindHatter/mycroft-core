import sys
import io
from .text_client import (
        start_log_monitor
    )

sys.stdout = io.StringIO()
sys.stderr = io.StringIO()


def main():
    # Monitor system logs
    start_log_monitor()


if __name__ == "__main__":
    main()
