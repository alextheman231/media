from manim import Code


def create_code_window(code_string: str) -> Code:
    return Code(
        code_string=code_string,
        language="bash",
        background="rectangle",
        paragraph_config={"font": "Monospace"},
    )
