from collections import defaultdict

CAPABILITIES = ['version', 'enableVNC', 'enableVideo', 'screenResolution']


def attr_to_caps(attr: str) -> str:
    """Convert simpified attribute name to CamelCase capability."""
    return defaultdict(lambda: attr, {
        'version': 'version',
        'vnc': 'enableVNC',
        'video': 'enableVideo',
        'resolution': 'screenResolution',
    })[attr]
