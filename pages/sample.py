from dash import register_page, dcc
from defaultlayouts.lorem import lorem

register_page(module=__name__,
              name="Sample Page",
              title='Sample Page')

layout = dcc.Markdown('''

## Sample Page

This page has been rendered from markdown 
using dcc.Markdown()

## A sample image
                      
This is held as static content within this app
                      
![Example image](/static/pexels-pixabay-147411_cropped.png)   
                      
## Repeated text to show scrolling

''' + 
" ".join([lorem + "\n\n" for _ in range(30)])
)