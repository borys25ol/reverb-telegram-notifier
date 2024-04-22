from pathlib import Path

from jinja2 import Template


def get_product_json_body_template() -> Template:
    with open(
        Path(__file__).parent.parent / "templates" / "product_template.jinja2"
    ) as f:
        template = f.read()

    return Template(template)


def get_search_json_body_template() -> Template:
    with open(
        Path(__file__).parent.parent / "templates" / "search_template.jinja2"
    ) as f:
        template = f.read()

    return Template(template)
