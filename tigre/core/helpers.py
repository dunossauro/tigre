from collections import defaultdict

_converted_capabilities = {
    'version': 'version',
    'vnc': 'enableVNC',
    'video': 'enableVideo',
    'resolution': 'screenResolution',
    'platform': 'platformName',
    'insecure': 'acceptInsecureCerts',
}

CAPABILITIES = _converted_capabilities.values()


def attr_to_caps(attr: str, capabilities=_converted_capabilities) -> str:
    """Convert simpified attribute name to CamelCase capability."""
    return defaultdict(
        lambda: attr,
        capabilities,
    )[attr]
