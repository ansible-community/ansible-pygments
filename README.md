# Ansible Sphinx Highlighter extension
[![Python linting badge](https://github.com/ansible-community/sphinx_ansible_highlighter/workflows/Python%20linting/badge.svg?event=push&branch=main)](https://github.com/ansible-community/sphinx_ansible_highlighter/actions?query=workflow%3A%22Python+linting%22+branch%3Amain)
[![Python testing badge](https://github.com/ansible-community/sphinx_ansible_highlighter/workflows/Python%20testing/badge.svg?event=push&branch=main)](https://github.com/ansible-community/sphinx_ansible_highlighter/actions?query=workflow%3A%22Python+testing%22+branch%3Amain)
[![Codecov badge](https://img.shields.io/codecov/c/github/ansible-community/sphinx_ansible_highlighter)](https://codecov.io/gh/ansible-community/sphinx_ansible_highlighter)

This is the [Sphinx extension](https://www.sphinx-doc.org/en/master/) `sphinx-ansible-highlighter` which provides a lexer for Ansible output.

Unless otherwise noted in the code, it is licensed under the terms of the GNU General Public License v3 or, at your option, later.

## Using the Sphinx extension

Include it in your Sphinx configuration ``conf.py``::

```
# Add it to 'extensions':
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'notfound.extension', 'sphinx_ansible_highlighter']
```
