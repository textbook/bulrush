from collections import Mapping
import re

_HTML = '''
<ul class="menu-list">
  <li>
    <a rel="license" href="{url}">
      <span class="icon is-small">
        <i class="fa fa-{icon} fa-fw"></i>
      </span>
      <span>{content}</span>
    </a>
  </li>
</ul>
'''

_DEFAULT_ICON = 'file-text-o'

_CC_LICENSE = re.compile(
    r'CC([-\s])(?P<type>[A-Z-]+)\1(?P<version>[\d.]+)',
    flags=re.VERBOSE | re.IGNORECASE
)


def generate_license(license_):
    if isinstance(license_, Mapping):
        try:
            return _format_license(**license_)
        except TypeError:
            return ''
    return _generate_named_license(str(license_))


def _generate_named_license(license_name):
    if _CC_LICENSE.match(license_name):
        return _format_license(**_generate_cc_license(license_name))
    return _format_license(**_generate_generic_license(license_name))


def _format_license(*, name, icon=_DEFAULT_ICON, url):
    return _HTML.format(url=url, icon=icon, content=name)


def _generate_generic_license(license_name):
    return dict(name=license_name, icon=_DEFAULT_ICON, url='#')


def _generate_cc_license(license_name):
    match = _CC_LICENSE.match(license_name)
    type_ = match.group('type').lower()
    version = match.group('version')
    url = 'http://creativecommons.org/licenses/{}/{}/'.format(type_, version)
    name = 'CC {} {}'.format(type_.upper(), version)
    return dict(name=name, icon='creative-commons', url=url)
