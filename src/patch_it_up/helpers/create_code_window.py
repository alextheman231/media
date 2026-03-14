from manim import Code


def create_code_window(code_string: str, language: str | None = "bash") -> Code:
    code = Code(
        code_string=code_string,
        language=language,
        background="rectangle",
        paragraph_config={"font": "Monospace"},
    )

    code.background.set_fill("#161b22", opacity=1)
    code.background.set_stroke("#30363d", width=2)

    return code
