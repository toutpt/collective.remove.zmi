Introduction
============

This addon remove the Zope Management Interface from Zope.

Why doing that ?
----------------

Do you install phpmyadmin on all LAMP server ?
And what if the ZMI has security issues ?

I really believe ZMI should be an addon for Zope2 using new zope technologies.
ZMI use DTML ... and is build by method on the persistent object, so it can't
be replaced, so let's remove it, and rebuild it.

So this addon is a first step before providing a nice ZMI.


WARNINGS
========

This addon is experimental, it may breaks lots of addons / stuff. It is a weird
patch on the core of Zope2. It patch all object which inherits from Zope base
one.

It will not touch to your data, only to the code.

How to install
==============

Just make the egg parts of your instance's eggs, no ZCML is needed.

This addon has no Plone dependencies but it support it, so you can use with it.

Credits
=======

Companies
---------

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_

People
------

* JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. _makinacom:  http://www.makina-corpus.com
