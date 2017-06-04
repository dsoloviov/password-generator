# Password generator

| Author | Email |
| --- | --- |
| Dmytro Soloviov | [dmytro.soloviov@gmail.com](mailto:dmytro.soloviov@gmail.com) |

**WARNING: This tool is not supposed to be used as actual password generator.  It's written for learning purpose only.**

## Dependencies

- [Requests](http://docs.python-requests.org/en/master/)

```bash
pip install -r requirements.txt
```

## Command line

```shell
$ python pgen.py [-h] [-w | -c]

optional arguments:
  -h, --help        show this help message and exit
  -w, --words       password consists of words
  -c, --characters  password consists of characters
```

Example:

```shell
$ python pgen.py -w
```

Password will contain 4 words.

```shell
$ python pgen.py -c
```

Password will contain 16 characters

## Import module

```python
>>> from pgen import password
>>> password()
medley-pleasant-boastful-wooden
>>> password(False)
tAW$};V7$E8![#%P
```

TODO:

- add ability to configure password (through CLI and import)
- add tests
- refactor CharPassword