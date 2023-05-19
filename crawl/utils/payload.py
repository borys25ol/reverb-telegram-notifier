from pathlib import Path

from jinja2 import Template


def get_json_body_template() -> Template:
    with open(Path(__file__).parent.parent / "templates" / "body_template.jinja2") as f:
        template = f.read()

    return Template(template)
