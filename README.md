# Password generator

| Author | Email |
| --- | --- |
| Dmytro Soloviov | [dmytro.soloviov@gmail.com](mailto:dmytro.soloviov@gmail.com) |

**WARNING: This tool is not supposed to be used as actual password generator.  It's written for learning purpose only.**

## Command line

```shell
$ python pgen.py [-h] [-L LENGTH] [-d] [-l] [-u] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -L LENGTH, --length LENGTH
                        length of the password
  -d, --digits          include digits
  -l, --lowercase       include lowercase characters
  -u, --uppercase       include uppercase characters
  -s, --special         include special characters
```

Example:

```shell
$ python pgen.py -d -u
```

Password can contain only digits and upper-case letters.

## Import module

```python
>>> from pgen import password
>>> password(length, params)
```

where `length` is password length (**int**), `params` is optional parameters (characters password should consist of).

Returns password string.

#### Parameters

If provided value is considered to be `False` (e.g. `False`, `0`, `[]`, `{}`, etc.) or omitted - all types of characters will be present in password (numbers, upper- and lower-case letters, special symbols). Otherwise, list of parameters should be provided:

```python
['digits', 'lowercase', 'uppercase', 'punctuation']

['uppercase', 'lowercase', 'digits', 'punctuation']  # order doesn't matter
```
Other elements of the list will be ignored.

Example:

```python
['digits', 'uppercase']
```

Password can contain only digits (0 - 9) and upper-case characters (A - Z).

## Tests

```shell
$ python -m unittest discover -v
```

## TODO

- Use argparse or something like that for command line argument parsing
- Add missing tests
