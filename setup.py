from setuptools import setup


setup(
    name='mezzanine-live-tile',
    version='1.1',
    license='MIT License',

    install_requires=[
        'Mezzanine >= 3.1.10',],

    description='A Plug and play app for mezzanine CMS to provide live tile and notifications for new website content for your Windows 8,Windows 8.1, Windows 10, or Windows Phone visitors.',
    long_description=open('README.rst').read(),

    author='Musharraf Omer',
    author_email='ibnomer2011@hotmail.com',

    url='https://github.com/mush42/mezzanine-live-tile',
    download_url='https://github.com/mush42/mezzanine-live-tile/downloads/',

    include_package_data=True,

    packages=['mezzanine_live_tile'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django'])
