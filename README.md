# ShinyProxy Dash Demo Image

This repository explains how to run Dash apps in ShinyProxy. When running Dash 1.3 or later, you will need to use at least ShinyProxy 2.5.0.

Dash requires the knowledge of the path used to access the app. ShinyProxy makes this path available as an environment variable, therefore you do not have to hard-code this path in your Python code.
For example, you can use:

```python

app = dash.Dash()

# ...

app.config.update({
    'routes_pathname_prefix': os.environ['SHINYPROXY_PUBLIC_PATH'],
    'requests_pathname_prefix': os.environ['SHINYPROXY_PUBLIC_PATH']
})

```

or

```python

app = dash.Dash(
    __name__,
    requests_pathname_prefix=os.environ['SHINYPROXY_PUBLIC_PATH']
    routes_pathname_prefix=os.environ['SHINYPROXY_PUBLIC_PATH'],
)
```

To pull the image made in this repository from Docker Hub, use

```
sudo docker pull openanalytics/shinyproxy-dash-demo
```

The relevant Docker Hub repository can be found at


https://hub.docker.com/r/openanalytics/shinyproxy-dash-demo


To build the image from the Dockerfile, navigate into the root directory of this repository and run


```
sudo docker build -t openanalytics/shinyproxy-dash-demo .
```

For deployment on ShinyProxy the port must be set to 8050, e.g.:

```yaml
specs:
- id: dash-demo
  display-name: Dash Demo Application
  port: 8050
  container-image: openanalytics/shinyproxy-dash-demo
```


(c) Copyright Open Analytics NV, 2018-2019.
