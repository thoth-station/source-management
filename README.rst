Thoth's Source Management
=========================

This library provides abstraction that allow's
`thoth <https://thoth-station.ninja/>`__ to interact with various source
management systems. We use OGR underneath to interact with git forges.

Install
-------

Use pipenv - This project is released on
`PyPI <https://pypi.org/project/thoth-sourcemanagement>`__, so the
latest release can be installed via pip or
`Pipenv <https://pipenv.readthedocs.io>`__ as shown below:

``pipenv install thoth-sourcemanagement``

How to use -
------------

.. code:: python

    from thoth.sourcemanagement.sourcemanagement import SourceManagement
    from thoth.sourcemanagement.enums import ServiceType

    # Service type you want to use
    service_type = ServiceType.GITHUB
    sm = SourceManagement(service_type, 'https://www.github.com', `private_token', 'username/repo_name')

Or if you want to use the application to interact as a Github Application -

.. code:: python

    # Service type you want to use
    service_type = ServiceType.GITHUB
    sm = SourceManagement(service_type=service_type, service_url='https://www.github.com', token=None, slug="username/repo_name", installation=True)

The environment variables that need to be set are -
    * `GITHUB_PRIVATE_KEY_PATH` - The path where the private key is located.
    * `GITHUB_APP_ID` - The Application ID of the Github app.


You could then call all the functions offered by the Source Management class.
