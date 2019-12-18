# Tigre

Tigre was born to ease the confusing calls of selenium webdriver.

If you have problems with different APIs for calling remote, local or mobile browsers. If you are confused by so many different capabilities settings or have trouble with hard-to-maintain code. Tigre was designed especially for you.

## Get started

### Tigre installation

`#TODO`

#### Definition enabling vnc and video recorder on firefox
```Python
>>> from tigre.remote import firefox

>>> ff = firefox.version(70.0).vnc(True).resolution('800x600').video(True).build()
<selenium.webdriver.remote.webdriver.WebDriver (session="38f70e50-6009-4623-8969-34a9331ebf0a")>

>>> ff.capabilities
{'browserName': 'firefox', 'version': '70.0', 'enableVNC': True, 'screenResolution': '800x600', 'enableVideo': True}
```

<details markdown="1">
<summary>Or import expecific version...</summary>

You can call directly what version you want <code>firefox70</code>

```python hl_lines="1 5"
>>> from tigre.remote import firefox70

>>> ff = firefox.vnc(True).resolution('800x600').video(True)
ff.capabilities
{'browserName': 'firefox', 'version': '70', 'enableVNC': True, 'screenResolution': '800x600', 'enableVideo': True}
```

</details>
