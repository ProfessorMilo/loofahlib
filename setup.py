from setuptools import setup, find_packages

setup(
    name="LoofahLib",
    version="0.1.1",
    packages=find_packages(),  # finds the inner LoofahLib folder automatically
    install_requires=[
        "pygame",
        "playsound",
        "requests",
        "pillow",
    ],
    description="A massive library of everything I might need for a game",
)
