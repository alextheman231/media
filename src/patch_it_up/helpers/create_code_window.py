from manim import Code


def create_code_window(code_string: str, language: str | None = "bash") -> Code:
    return Code(
        code_string=code_string,
        language=language,
        background="rectangle",
        paragraph_config={"font": "Monospace"},
    )
