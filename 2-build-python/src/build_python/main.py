import argparse

from build_python.agents.coordinator import run


def main() -> None:
    parser = argparse.ArgumentParser(prog="build-python")
    parser.add_argument(
        "message",
        nargs="?",
        default="my internet is slow",
        help="what the caller says",
    )
    args = parser.parse_args()
    run(args.message)


if __name__ == "__main__":
    main()
