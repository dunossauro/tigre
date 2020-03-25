# Capabilities

In this section of documentation we explain how use capabilities.

In normal cases using selenium we need create a [python dictonary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) to describe webdriver capabilities. Something like that

```Python
from selenium.webdriver import Remote

capabilities = {
    'browserName': 'Firefox',
    'browserVersion': '69',
    'acceptInsecureCerts': True
}

browser = Remote(
    command_executor='your-remote-webdriver-url',
    desired_capabilities=capabilities,
)
```

The tigre's main idea is make remote webdriver usability more easy.

TODO: explicar coisas

## Tigre imports

Tigre is implemented based on [PEP-562](https://www.python.org/dev/peps/pep-0562/). So when you call the import we parse the name and invoke the correct class.

### Code exaple:

```Python

from tigre.remote import <browser><version>

```

Using this mecanism Tigre can auxiliate you to write less code. For example `<browser><version>` can be replaced for real examples above.

## Tigre Browser name

```Python
# Examples importing only browser
from tigre.remote import firefox
from tigre.remote import chrome
from tigre.remote import opera

>>> firefox.capabilities
# {'browserName': 'firefox'}
```

## Tigre Browser version

In imports you can define browser name and browser version

```Python
from tigre.remote import firefox69

>>> firefox69.capabities
# {'browserName': 'firefox', 'version': '69'}
```

## Tigre dynamic setting capabilities

For another capabilities like platform name you can implements using dynamic methods.

```Python
from tigre.remote import firefox69

>>> firefox69.platform('linux')
>>> firefox69.capabilities
# {'browserName': 'firefox', 'version': '69', 'platformName': linux}
```

### Tigre converted capabilities

| Tigre | Original | type |
| - | - | - |
| version | version | int or str|
| vnc | enableVNC | bool |
| video | enableVideo | bool |
| resolution | screenResolution | str |
| platform | platformName | str |
| insecure | acceptInsecureCerts | bool |

```Python
from tigre.remote import firefox
>>> firefox.version(69).vnc(True).video(True).resolution('800x600').platform('linux').insecure(True)
# firefox(caps={'browserName': 'firefox', 'version': '69', 'enableVNC': True, 'enableVideo': True, 'screen Resolution': '800x600', 'platformName': 'linux', 'acceptInsecureCerts': True}})
```

(????) So in this sections of documentation we explain a create a relation beetwen.

### Tigre not built-in converted

...

## Base capabilities [W3C](https://w3c.github.io/webdriver/#capabilities)

| Capability | tool key | Tigre equivalent | type | function |
| - | - | - | - |- |
| Browser name    | "browserName"    | [import defitinion]() | string | Identifies the user agent. |
| Browser version | "browserVersion" | `.version(int)`  [import defitinion]() | `string` or `int` | Identifies the version of the user agent. |
| Accept insecure TLS certificates | "acceptInsecureCerts"| `.insecure(bool)`  |boolean|	Indicates whether untrusted and self-signed TLS certificates are implicitly trusted on navigation for the duration of the session. |
| Page load strategy | "pageLoadStrategy" | `.strategy(str)` | str | Defines the current session’s page load strategy. |
| Proxy configuration | "proxy" |  `.proxy(ProxyObject)` | ProxyObject | Defines the current session’s proxy configuration. |


## Selenium grid capabilities

| Capability | tool key | Tigre equivalent | type | function |
| - | - | - | - |- |

## Appium capabilities

| Capability | tool key | Tigre equivalent | type | function |
| - | - | - | - |- |

## [Selenoid capabilities](https://github.com/aerokube/selenoid/blob/master/docs/special-capabilities.adoc#special-capabilities)

| Capability | tool key | Tigre equivalent | type | function |
| - | - | - | - |- |

## Zalenium capabilities

| Capability | tool key | Tigre equivalent | type | function |
| - | - | - | - |- |

## No mapped capabilities
