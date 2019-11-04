from setuptools import setup, find_packages;

setup(
    name = (
        "match"
    ),
    version = (
        "1.0.0"
    ),
    description = (
        "match function inspired by V language"
    ),
    long_description = (
        "match function replaces original if-elseif operator."
    ),
    requires = (
        "Python 3.7 or newer"
    ),
    author = (
        "Tomoaki Yamashita"
    ),
    author_email = (
        "elessar869@gmail.com"
    ),
    url = (
        "https://github.com/TmxkGtw/match_func_python/tree/master/match"
    ),
    license = (
        "Apache License Version 2"
    ),
    packages = (
        find_packages()
    )
);