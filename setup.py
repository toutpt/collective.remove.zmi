from setuptools import setup, find_packages

version = '1.0'

setup(
    name='collective.remove.zmi',
    version=version,
    description="Remove ZMI",
    long_description=open("README.rst").read() + "\n" +
     open("CHANGES.txt").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Framework :: Zope2",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='plone',
    author='JeanMichel aka toutpt',
    author_email='toutpt@gmail.com',
    url='https://github.com/toutpt/collective.remove.zmi',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.remove'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Zope2',
        # -*- Extra requirements: -*-
    ],
    extras_require=dict(
        test=['plone.app.testing', 'plone.app.robotframework'],
    ),
    entry_points="""
    # -*- Entry points: -*-
    """,
    #setup_requires=["PasteScript"],
    #paster_plugins=["ZopeSkel"],
)
