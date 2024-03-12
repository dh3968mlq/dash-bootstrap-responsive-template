## Template Description

Code on [Gitgub](https://github.com/dh3968mlq/dash-bootstrap-responsive-template)

![Example image](/static/pexels-pixabay-147411_cropped.png)   

[Dash](https://dash.plotly.com/) allows [multi-page web apps](https://dash.plotly.com/)
to be programmed (almost entirely) in Python

[Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
wraps the [Bootstrap](https://getbootstrap.com/docs/3.4/components/) components library

### This Template

* Implements a basic responsive design
    * Further suggestions and contributions are welcome - please feel free to raise an [issue](https://github.com/dh3968mlq/dash-bootstrap-responsive-template/issues)
* Draws on the much more complex [code for the Dash Mantine Components Documentation](https://github.com/snehilvj/dmc-docs)
* Is implemented almost entirely in Python using
    * [Dash](https://dash.plotly.com/urls)
    * [Dash Pages](https://dash.plotly.com/urls) to create a multi-page app
    * [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
* Responds to screen size. On narrower screens:
    * The right sidebar disappears
    * The left sidebar is replaced by a pop-up drawer
    * The title becomes shorter and smaller
    * The navigation in the header is replaced by a dropdown menu
* Allows flexible control of the sidebar content
    * The left sidebar can share some, all or none of its content with the pop-up that replaces it on a small screen
    * Pages can have customised left or right sidebars and/or pop-ups
* Shows a simple Plotly interactive graph
    * On narrow screens, controls can be moved to, or duplicated on, the pop-up sidebar 
* Autogenerates content from Markdown files
* Is configured for deployment on Heroku
* Is not released as a package on PyPI
    * Just download the code and make any changes you want
* Has navigation both in the header and in the left sidebar (and two hamburger buttons on a small screen)
    * It's expected one of these would be removed if it's used as the basis of a real application

### This Page

The content of this page is stored as *posts/Template-Description.md* and is automatically 
converted for display by *pages/autogenerate.py*, execution of which is 
triggered on load by the Dash multi-page mechanism.


