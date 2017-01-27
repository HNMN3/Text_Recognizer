#Keep Coding And change the world and do not forget anything... Not Again..
import pyocr
import pyocr.builders
from PIL import Image
import sys

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'

txt = tool.image_to_string(
    Image.open('skit.jpg'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
print txt