# Running Dash apps inside ShinyProxy

This repository explains how to run Dash apps in ShinyProxy. When running Dash
1.3 or later, you will need to use at least ShinyProxy 2.5.0.

Dash requires the knowledge of the path used to access the app. ShinyProxy makes
this path available as an environment variable, therefore you do not have to
hard-code this path in your Python code. For example, you can use:

```python

app = dash.Dash(
    __name__,
    requests_pathname_prefix=os.environ['SHINYPROXY_PUBLIC_PATH'],
    routes_pathname_prefix=os.environ['SHINYPROXY_PUBLIC_PATH']
)
```

In order to ensure assets (e.g. css and js files, images ...) load correctly,
use the `dash.get_asset_url` function, e.g.:

```python
import dash

# ...
    html.Img(src=dash.get_asset_url("logo.png")),
# ...
```

Similarly, to link to other pages, use the `dash.get_relative_path` function, e.g.:

```python
dcc.Link(href=dash.get_relative_path('/page-1'))
```

## Building the Docker image

To pull the image made in this repository from Docker Hub, use

```bash
sudo docker pull openanalytics/shinyproxy-dash-demo
```

The relevant Docker Hub repository can be found
at [https://hub.docker.com/r/openanalytics/shinyproxy-dash-demo](https://hub.docker.com/r/openanalytics/shinyproxy-dash-demo)

To build the image from the Dockerfile, navigate into the root directory of this
repository and run

```bash
sudo docker build -t openanalytics/shinyproxy-dash-demo .
```

## ShinyProxy Configuration

Create a ShinyProxy configuration file (see [application.yml](application.yml)
for a complete file), containing:

```yaml
proxy:
  specs:
  - id: dash-demo
    display-name: Dash Demo Application
    port: 8050
    container-image: openanalytics/shinyproxy-dash-demo
    target-path: "#{proxy.getRuntimeValue('SHINYPROXY_PUBLIC_PATH')}"
```

**(c) Copyright Open Analytics NV, 2018-2024.**
