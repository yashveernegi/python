import argparse

from build_python.agents.coordinator import run


def main() -> None:
    parser = argparse.ArgumentParser(prog="build-python")
    parser.add_argument("a", nargs="?", type=int, default=10, help="first operand")
    parser.add_argument("b", nargs="?", type=int, default=20, help="second operand")
    args = parser.parse_args()
    run(args.a, args.b)


if __name__ == "__main__":
    main()
