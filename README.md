# [Pygments] lexer and style Ansible snippets

[![Python linting badge](https://github.com/ansible-community/ansible-pygments/workflows/Python%20linting/badge.svg?event=push&branch=main)](https://github.com/ansible-community/ansible-pygments/actions?query=workflow%3A%22Python+linting%22+branch%3Amain)
[![Python testing badge](https://github.com/ansible-community/ansible-pygments/workflows/Python%20testing/badge.svg?event=push&branch=main)](https://github.com/ansible-community/ansible-pygments/actions?query=workflow%3A%22Python+testing%22+branch%3Amain)
[![Codecov badge](https://img.shields.io/codecov/c/github/ansible-community/ansible-pygments)](https://codecov.io/gh/ansible-community/ansible-pygments)

This project provides a [Pygments] lexer that is able to handle
[Ansible] output. It may be used anywhere Pygments is integrated.
The lexer is registered globally under the name `ansible-output`.

It also provides a [Pygments] style for tools needing to highlight
code snippets.

The code is licensed under the terms of the BSD 2-Clause license.

## Using the lexer in [Sphinx]

Make sure this library in installed in the same env as your [Sphinx]
automation via `pip install ansible-pygments sphinx`. Then, you should
be able to use a lexer by its name `ansible-output` in the code blocks
of your RST documents. For example:

```rst
.. code-block:: ansible-output

    [WARNING]: Unable to find '/nosuchfile' in expected paths (use -vvvvv to see paths)

    ok: [localhost] => {
        "msg": ""
    }
```

## Using the style in [Sphinx]

It is possible to just set `ansible` in `conf.py` and it will "just
work", provided that this project is installed alongside [Sphinx] as
shown above.

```python
pygments_style = 'ansible'
```

[Ansible]: https://www.ansible.com/?utm_medium=github-or-pypi&utm_source=ansible-pygments--readme
[Pygments]: https://pygments.org
[Sphinx]: https://www.sphinx-doc.org
