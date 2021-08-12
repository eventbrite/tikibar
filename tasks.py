from __future__ import absolute_import

from invoke_release.tasks import *  # noqa


configure_release_parameters(  # noqa
    module_name='tikibar',
    display_name='Eventbrite Common Utilities Library',
    use_pull_request=True,
    use_tag=False,
)
