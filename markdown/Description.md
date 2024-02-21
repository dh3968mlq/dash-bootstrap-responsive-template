## Template description

Author: David Harris 2024

Code on [Gitgub](https://github.com/dh3968mlq/dash-mantine-starter-kit)

[Dash](https://dash.plotly.com/) allows [multi-page web apps](https://dash.plotly.com/)
to be programmed (almost entirely) in Python

[Dash Mantine Components](https://www.dash-mantine-components.com/)
wraps the [Mantine](https://mantine.dev/) React components library

### This template

* Implements a basic responsive design
* Draws on the much more complex [code for the Dash Mantine Components Documentation](https://github.com/snehilvj/dmc-docs)
* Is implemented entirely in Python (except for a one-line example of a Javascript clientside callback) using
    * [Dash](https://dash.plotly.com/urls)
    * [Dash Pages](https://dash.plotly.com/urls) to create a multi-page app
    * [Dash Mantine Components](https://www.dash-mantine-components.com/)
* Uses the Dash Mantine Components default light theme
    * A one-line change is needed to change it to the dark theme
* Responds to screen size. On narrower screens:
    * The right sidebar disappears
    * The left sidebar is replaced by a pop-up drawer
    * The title becomes shorter and smaller
* Autogenerates content from Markdown files
    * This uses [DH's fork of markdown2dash](https://github.com/dh3968mlq/markdown2dash),
included as a Git submodule at present
* Is configured for deployment on Heroku

### Outstanding challenges

* Rendering from files held as static HTML
* Exact vertical alignment if using an icon as a list item symbol

### This page

The content of this page is stored as *markdown/description.md* and is automatically 
converted for display by *pages/autogenerate.py*, execution of which is 
triggered on load by the Dash multi-page mechanism.


