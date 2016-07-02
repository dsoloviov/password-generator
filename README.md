# Password generator

| Author | Email |
| --- | --- |
| Dmytro Soloviov | [dmytro.soloviov@gmail.com](mailto:dmytro.soloviov@gmail.com) |

**WARNING: This tool is not supposed to be used as actual password generator.  It's written for learning purpose only.**

## Run from command line

```shell
$ python pgen.py [-N <digit>] [-L <digit>] [--all] [-d] [-l] [-u] [-s]
```

where:

`-N <digit>` stands for number of passwords the tool produces. `-L <digit>` means the length of each password. If omitted, number of passwords is 1 with length equal 10.

`-d` means that password would contain digits, `-l` - lower-case letters, `-u` - upper-case letters, `-s` - special symbols. `--all` means that password would contain all types of characters mentioned above. Using `--all` overrides other parameters (e.g. using `--all` and `-d` will return password containing all types of characters). If omitted, password will contain all types of characters.

Example:

```shell
$ python pgen.py -d -u
```

Password can contain only digits and upper-case letters.

## Usage as a module

```python
>>> from pgen import password
>>> password(number, length, params)
```

where `number` is number of passwords to generate (**int**), `length` is password length (**int**), `params` is optional parameters (characters password should consist of).

Returns list of passwords.

#### Parameters

If provided value is considered to be `False` (e.g. `False`, `0`, `[]`, `{}`, etc.) or omitted - all types of characters can be present in password (numbers, upper- and lower-case letters, special symbols). Otherwise, list or tuple of parameters should be provided:

```python
['digits', 'lowercase', 'uppercase', 'punctuation']
```
Other elements of the list will be ignored.

Example:

```python
['digits', 'uppercase']
```

Password can contain only digits (0 - 9) and upper-case characters (A - Z).

## Tests

Run tests

## TODO

1. Add tests
