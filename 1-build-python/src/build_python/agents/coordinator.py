from build_python.tools import web_search
from build_python.tools.calculator import add


def run(a: int, b: int) -> None:
    result = add(a, b)
    if result < 50:
        print(web_search.search(f"searching for additional tool {result}"))
    else:
        print(f"Result: {result}")
