import jinja2
from fastapi.templating import Jinja2Templates
from pathlib import Path
from backend.CONSTANTS import TEMPLATE_DIR

jenv = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
    autoescape=jinja2.select_autoescape(["html"])
)

jenv.globals = {"Path": Path} # let jinja2 templates access libraries

templates = Jinja2Templates(env=jenv)