cmsplugin-blog Attachments
==========================

An extension for `cmsplugin-blog <https://github.com/fivethreeo/cmsplugin-blog/>`_
which adds attachments to the blog. This is based on 
`django-filer <https://github.com/stefanfoulis/django-filer>`_ and
`django-document-library <https://github.com/bitmazk/django-document-library>`_.

Installation
------------

You need to install the following prerequisites in order to use this app:

* Django
* django-cms
* cmsplugin-blog
* django-filer
* django-document-library

If you want to install the latest stable release from PyPi::

    $ pip install cmsplugin-blog-attachments

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-blog-attachments.git#egg=cmsplugin_blog_attachments

Add ``cmsplugin_blog_attachments`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'cmsplugin_blog_attachments',
    )


Usage
-----

Just write a blog Entry and you will see a new inline for attachments in the
Entry admin.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
