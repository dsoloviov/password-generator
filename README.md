# Password generator

| Author | Email |
| --- | --- |
| Dmytro Soloviov | [dmytro.soloviov@gmail.com](mailto:dmytro.soloviov@gmail.com) |

## Usage

```python
>>> from pgen import password
>>> password(number, length, params)
```

where `number` is number of passwords to generate (**int**), `length` is password length (**int**), `params` is optional parameters (characters password should consist of).

If `number` is bigger than 1, list of passwords returns. Otherwise, single password string returns.

### Parameters

If provided value is considered to be `False` (e.g. `False`, `0`, `[]`, `{}`, etc.) or omitted - all types of characters can be present in password (numbers, upper- and lower-case letters, special symbols). Otherwise, dictionary of parameters should be provided:

```python
{
 'digits': boolean,
 'lower': boolean,
 'upper': boolean,
 'special': boolean
}
```

Example:

```python
{
 'digits': True,
 'lower': False,
 'upper': True,
 'special': False
}
```

Password can contain only digits (0 - 9) and upper-case characters (A - Z).

## Tests

Run tests

## TODO

1. Add tests
2. Add argument parsing
