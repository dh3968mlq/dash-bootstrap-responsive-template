## Dash Bootstrap Responsive Template Boilerplate

A starter template app with boilerplate code for a responsive multi-page app using Dash Bootstrap components

Author: David Harris 2024, originally based on Snehil Vijay's dmc-docs app at https://github.com/snehilvj/dmc-docs 

[Dash](https://dash.plotly.com/) allows [multi-page web apps](https://dash.plotly.com/)
to be programmed (almost entirely) in Python

[Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/) wraps
the [Bootstrap toolkit](https://getbootstrap.com/docs/5.3/getting-started/introduction/) 

### This template

* Implements a basic responsive design
* Is implemented almost entirely in Python using
    * [Dash](https://dash.plotly.com/urls)
    * [Dash Pages](https://dash.plotly.com/urls) to create a multi-page app
    * [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/)
* Responds to screen size. On narrower screens:
    * The right sidebar disappears
    * The left sidebar is replaced by a pop-up drawer
    * The title becomes shorter and smaller
* Autogenerates content from Markdown files
* Shows a simple Plotly interactive graph
    * On narrow screens, controls can be moved to, or duplicated on, the pop-up sidebar 
* Is configured for deployment on Heroku
    * At time of writing (March 2024), it is running at https://dash-bootstrap-template-c3f1e794ed42.herokuapp.com/. (It uses eco dynos and may take a few seconds to wake up)
* Requires a one-line change for Bootstrap theme changes, including use of dark themes
