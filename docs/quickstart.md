# Quickstart

Eager to get started? This page gives a good introduction to Tigre. It assumes you already have Tigre installed. If you do not, head over to the [Installation]() section.

## Minimal usage

The first think you need know is how import and use Tigre. So, the fist example looks like

```Python
from tigre.remote import firefox  # 1

my_browser = firefox.build()  # 2
```

So what did that code do?

1. importing `firefox` from `tigre.remote`. `tigre.remote` supose we are using a remote webdriver and we have a selenium grid up. If you dont have a selenium grid configurated, please read [starting a selenium grid](.) section. Importing firefox you already have the capabilities of firefox for the selenium grid `{'browserName': 'firefox'}`

2. Building a firefox remote webdrver. The method `.build()` assumes many settings by default, the build method call a senium `RemoteWebdriver`.

## Acess your grid

In many cases, you are running the development code or using selenium standalone and you need configure the selenium grid URL. In this example, you can use `tigre.config` to help you to set the correct configuration.

```Python
from tigre import config  # 1
from tigre.remote import firefox

config.remote_url = "http://localhost:4444/wd/hub"  # 2

browser = firefox.build()  # 3
```

1. Import `tigre.config`.
2. Set your selenium grid URL
3. When tiger builds its webdriver, it will start based on the `config` settings

### Environment variables

You will probably run your code in different environments. For example, your local development URL may be a URL indicating `localhost`, but in production, your URL may change.

The most efficient way to do this is to use environment variables. To define the URL of your grid we use the variable `TIGRE_REMOTE_URL`

Você pode simplesmente dizer qual a sua URL no momento em que for executar o seu código:

```bash
TIGRE_REMOTE_URL=http://localhost:4444/wd/hub python your_code.py
```

Or you can export the moment you export your other environment variables

```bash
export TIGRE_REMOTE_URL=http://localhost:4444/wd/hub

python your_code.py
```

## Dynamic version imports

In many cases, we need to run our code on different versions of browsers or mobile devices. We would normally do this using capabilities. However, the tiger provides a simpler alternative. What we call dynamic import.

For example, we may want to import only Firefox or import a specific version of firefox to run a test:

```Python
from tigre.remote import firefox    # 1
from tigre.remote import firefox70  # 2
```

1. We import only Firefox
2. We specifically imported version 70 of firefox

That way the capabilities would already be sitting

```python hl_lines="2 5"
>>> firefox.capabilities
{'browserName': 'firefox'}

>>> firefox70.capabilities
{'browserName': 'firefox', 'version': '70'}
```

## Setting capabilities
