# dash-bootstrap-starter-kit

A starter template app for a responsive multi-page app using Dash Bootstrap components

Author: David Harris 2024, based on Snehil Vijay's dmc-docs app at https://github.com/snehilvj/dmc-docs 

[Dash](https://dash.plotly.com/) allows [multi-page web apps](https://dash.plotly.com/)
to be programmed (almost entirely) in Python

### This template

* Implements a basic responsive design
* Is implemented entirely in Python (except for a one-line example of a Javascript clientside callback) using
    * [Dash](https://dash.plotly.com/urls)
    * [Dash Pages](https://dash.plotly.com/urls) to create a multi-page app
    * [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/)
* Responds to screen size. On narrower screens:
    * The right sidebar disappears
    * The left sidebar is replaced by a pop-up drawer
    * The title becomes shorter and smaller
* Autogenerates content from Markdown files
* Is configured for deployment on Heroku
