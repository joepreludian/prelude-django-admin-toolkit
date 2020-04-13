from setuptools import setup, find_packages


setup(
    name="prelude-django-admin-uikit",
    version="0.2.0",
    packages=['prelude_django_admin_uikit'],

    install_requires=[
        'django>=3',
        'django-compressor',
        'django-sass-processor'
    ],

    include_package_data=True,

    author="Jonhnatha Trigueiro",
    author_email="joepreludian@gmail.com",
    description="Template for Django admin based on uikit",

    keywords="django admin uikit",
    url="https://github.com/joepreludian/prelude-django-admin-toolkit",
    project_urls={
        "Bug Tracker": "https://github.com/joepreludian/prelude-django-admin-toolkit/issues/new",
        "Documentation": "https://github.com/joepreludian/prelude-django-admin-toolkit",
        "Source Code": "https://github.com/joepreludian/prelude-django-admin-toolkit",
    },

    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ]
)
