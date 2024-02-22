from dash import register_page, dcc
from lib.lorem import lorem

register_page(__name__, title='Another Page')

layout = dcc.Markdown('''

# This is another page

This page has been rendered from markdown 
using dcc.Markdown()

## A sample image
                      
This is held as static content within this app
                      
![Example image](/static/sample_image.png)   
                      
## Repeated text to show scrolling

''' + 
" ".join([lorem + "\n\n" for _ in range(30)])
)