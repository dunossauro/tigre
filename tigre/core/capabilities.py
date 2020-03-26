selenium = {
    'version': 'version',  # str or int
    'platform': 'platformName', # str
    'insecure': 'acceptInsecureCerts', # bool
    'strategy': 'pageLoadStrategy' # str ['normal', 'eager', 'none']
}


selenoid = {
    'vnc': 'enableVNC',  # bool
    'video': 'enableVideo',  # bool
    'resolution': 'screenResolution',  # str
}


capabilities = {**selenium, **selenoid}
