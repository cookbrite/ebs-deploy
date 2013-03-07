from setuptools import setup

setup(

    # general meta
    name='ebs-deploy',
    version='0.0.1',
    author='Brian C. Dilley',
    author_email='brian.dilley@gmail.com',
    description='Python based command line tools for managing Amazon Elastic Beanstalk applications.',
    platforms='any',
    url='https://github.com/briandilley/ebs-deploy',

    # packages
    packages=['ebs_deploy'],

    # dependencies
    install_requires = [
        'boto == 2.8.0'
    ],
    # additional files to include
    include_package_data=True,

    # the scripts
    scripts=['scripts/ebs-deploy'],

    # wut?
    classifiers=['Intended Audience :: Developers']
)