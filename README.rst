Tikibar
=======

A debugging and information toolbar for django, designed for lightweight impact
so it can be enabled selectively and run in production.


Features
--------

Among other things, it includes:

* CPU usage time statistics
* Used template tracking
* SQL call logging and timing
* Cross-domain functionality


Getting Started
---------------

To use Tikibar, you need to add it to your Django ``INSTALLED_APPS`` and then
include the middleware (``tikibar.middleware.TikibarMiddleware``) in your
Django middleware configuration.


Release Process
---------------
* Bump version in ``tikibar/version.py`` | ``__version_info__ = (x, x, x)``.
* ``git add tikibar/version.py``
* ``git commit -am 'Bump tikibar to x.x.x'``
* ``git push origin master``
* ``git tag -a x.x.x -m "Bump tikibar to x.x.x"``
* ``git push origin x.x.x``
