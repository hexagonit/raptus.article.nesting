Introduction
============

Manage where you will list your bottom articles. Disable your article for random fader or
other listings.

The following features for raptus.article are provided by this package:

Content
-------
    * Provides nesting support for articles

Dependencies
------------
    * archetypes.schemaextender
    * raptus.article.core

Installation
============

To install raptus.article.nesting into your Plone instance, locate the file
buildout.cfg in the root of your Plone instance directory on the file system,
and open it in a text editor.

Add the actual raptus.article.nesting add-on to the "eggs" section of
buildout.cfg. Look for the section that looks like this::

    eggs =
        Plone

This section might have additional lines if you have other add-ons already
installed. Just add the raptus.article.nesting on a separate line, like this::

    eggs =
        Plone
        raptus.article.nesting

Note that you have to run buildout like this::

    $ bin/buildout

Then go to the "Add-ons" control panel in Plone as an administrator, and
install or reinstall the "raptus.article.default" product.

Note that if you do not use the raptus.article.default package you have to
include the zcml of raptus.article.nesting either by adding it
to the zcml list in your buildout or by including it in another package's
configure.zcml.

Usage
=====

Add article
-----------
You may now add articles in your article. Click the "Add new" menu and select "Article" in the pull down menu.
You get the standard plone form to add your article. 

Components
----------
The following packages provide components to display contained articles:

    * `raptus.article.listings <http://pypi.python.org/pypi/raptus.article.listings>`_
    * `raptus.article.contentfader <http://pypi.python.org/pypi/raptus.article.contentfader>`_
    * `raptus.article.contentflow <http://pypi.python.org/pypi/raptus.article.contentflow>`_
    * `raptus.article.randomcontent <http://pypi.python.org/pypi/raptus.article.randomcontent>`_

Copyright and credits
=====================

raptus.article is copyrighted by `Raptus AG <http://raptus.com>`_ and licensed under the GPL. 
See LICENSE.txt for details.
