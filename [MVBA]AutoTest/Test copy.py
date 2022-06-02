from PIL import Image
from io import BytesIO
import base64
from Params.CaseDoc import *


print(SC.Pen_AdorneMenu)

data = '''R0lGODlhDwAPAKECAAAAzMzM/////wAAACwAAAAADwAPAAACIISPeQHsrZ5ModrLl
N48CXF8m2iQ3YmmKqVlRtW4MLwWACH+H09wdGltaXplZCBieSBVbGVhZCBTbWFydFNhdmVyIQAAOw=='''
im = Image.open(BytesIO(base64.b64decode(data)))
ig = Image.open(data)
""
