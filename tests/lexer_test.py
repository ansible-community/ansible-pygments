# Author: Felix Fontein <felix@fontein.de>
# License: BSD-2-Clause
# Copyright: Felix Fontein <felix@fontein.de>, 2021
"""Tests for Pygments lexers.

They rely on token comparison for stability reasons. Relying on
additional style formatting is known to break with updates to
the pygments library itself.
"""

from pygments import __version__ as _pygments_version
from pygments.lexers import get_lexer_by_name as _get_lexer_by_name
from pygments.token import Token

PYGMENTS_VERSION_INFO = tuple(map(int, _pygments_version.split('.')))
IS_OLD_PYGMENTS_PRE_2_14 = PYGMENTS_VERSION_INFO <= (2, 14, 0)


def test_ansible_output_lexer():
    """Test that ``AnsibleOutputLexer`` produces expected tokens."""
    ansible_play_output_example = R"""
ok: [windows] => {
    "account": {
        "account_name": "vagrant-domain",
        "type": "User"
    },
    "authentication_package": "Kerberos",
    "user_flags": []
}

TASK [paused] ************************************************************************************************************************************
Sunday 11 November 2018  20:16:48 +0100 (0:00:00.041)       0:07:59.637 *******
--- before
+++ after
@@ -1,5 +1,5 @@
 {
-  "exists": false,
-  "paused": false,
-  "running": false
+  "exists": true,
+  "paused": true,
+  "running": true
 }
\ No newline at end of file

changed: [localhost]

TASK [volumes (more volumes)] ********************************************************************************************************************
Sunday 11 November 2018  20:19:25 +0100 (0:00:00.607)       0:10:36.974 *******
--- before
+++ after
@@ -1,11 +1,11 @@
 {
   "expected_binds": [
-    "/tmp:/tmp:rw",
-    "/:/whatever:rw,z"
+    "/tmp:/somewhereelse:ro,Z",
+    "/tmp:/tmp:rw"
   ],
   "expected_volumes": {
-    "/tmp": {},
-    "/whatever": {}
+    "/somewhereelse": {},
+    "/tmp": {}
   },
   "running": true
 }
\ No newline at end of file

changed: [localhost]
"""

    expected_resulting_text_tokens = [
        (0, Token.Text.Whitespace, '\n'),
        (1, Token.Keyword, 'ok'),
        (3, Token.Punctuation, ':'),
        (4, Token.Text, ' '),
        (5, Token.Punctuation, '['),
        (6, Token.Name.Variable, 'windows'),
        (13, Token.Punctuation, ']'),
        (14, Token.Text, ' '),
        (15, Token.Punctuation, '=>'),
        (17, Token.Text, ' '),
        (18, Token.Punctuation, '{'),
        (19, Token.Text, '\n    '),
        (24, Token.Name.Tag, '"account"'),
        (33, Token.Punctuation, ':'),
        (34, Token.Text, ' '),
        (35, Token.Punctuation, '{'),
        (36, Token.Text, '\n        '),
        (45, Token.Name.Tag, '"account_name"'),
        (59, Token.Punctuation, ':'),
        (60, Token.Text, ' '),
        (61, Token.Literal.String, '"vagrant-domain"'),
        (77, Token.Punctuation, ','),
        (78, Token.Text, '\n        '),
        (87, Token.Name.Tag, '"type"'),
        (93, Token.Punctuation, ':'),
        (94, Token.Text, ' '),
        (95, Token.Literal.String, '"User"'),
        (101, Token.Text, '\n    '),
        (106, Token.Punctuation, '}'),
        (107, Token.Punctuation, ','),
        (108, Token.Text, '\n    '),
        (113, Token.Name.Tag, '"authentication_package"'),
        (137, Token.Punctuation, ':'),
        (138, Token.Text, ' '),
        (139, Token.Literal.String, '"Kerberos"'),
        (149, Token.Punctuation, ','),
        (150, Token.Text, '\n    '),
        (155, Token.Name.Tag, '"user_flags"'),
        (167, Token.Punctuation, ':'),
        (168, Token.Text, ' '),
        (169, Token.Punctuation, '['),
        (170, Token.Punctuation, ']'),
        (171, Token.Text, '\n'),
        (172, Token.Punctuation, '}'),
        (173, Token.Text, '\n'),
        (174, Token.Text.Whitespace, '\n'),
        (175, Token.Keyword, 'TASK'),
        (179, Token.Text, ' '),
        (180, Token.Punctuation, '['),
        (181, Token.Literal, 'paused'),
        (187, Token.Punctuation, ']'),
        (188, Token.Text, ' '),
        (
            189,
            Token.Name.Variable,
            '*' * 132,
        ),
        (321, Token.Text, '\n'),
        *(
            (
                (
                    322,
                    Token.Text.Whitespace,
                    'Sunday 11 November 2018  20:16:48 +0100 (0:00:00.041)       '
                    '0:07:59.637 *******\n',
                ),
            ) if IS_OLD_PYGMENTS_PRE_2_14 else (
                (
                    322,
                    Token.Text,
                    'Sunday 11 November 2018  20:16:48 +0100 (0:00:00.041)       '
                    '0:07:59.637 *******',
                ),
                (401, Token.Text.Whitespace, '\n'),
            )
        ),
        (402, Token.Generic.Deleted, '--- before'),
        (412, Token.Text.Whitespace, '\n'),
        (413, Token.Generic.Inserted, '+++ after'),
        (422, Token.Text.Whitespace, '\n'),
        (423, Token.Generic.Subheading, '@@ -1,5 +1,5 @@'),
        (438, Token.Text.Whitespace, '\n'),
        (439, Token.Text.Whitespace, ' '),
        (440, Token.Text, '{'),
        (441, Token.Text.Whitespace, '\n'),
        (442, Token.Generic.Deleted, '-  "exists": false,'),
        (461, Token.Text.Whitespace, '\n'),
        (462, Token.Generic.Deleted, '-  "paused": false,'),
        (481, Token.Text.Whitespace, '\n'),
        (482, Token.Generic.Deleted, '-  "running": false'),
        (501, Token.Text.Whitespace, '\n'),
        (502, Token.Generic.Inserted, '+  "exists": true,'),
        (520, Token.Text.Whitespace, '\n'),
        (521, Token.Generic.Inserted, '+  "paused": true,'),
        (539, Token.Text.Whitespace, '\n'),
        (540, Token.Generic.Inserted, '+  "running": true'),
        (558, Token.Text.Whitespace, '\n'),
        (559, Token.Text.Whitespace, ' '),
        (560, Token.Text, '}'),
        (561, Token.Text.Whitespace, '\n'),
        *(
            (
                (
                    562,
                    Token.Text.Whitespace,
                    '\\ No newline at end of file\n',
                ),
            ) if IS_OLD_PYGMENTS_PRE_2_14 else (
                (562, Token.Text, '\\ No newline at end of file'),
                (589, Token.Text.Whitespace, '\n'),
            )
        ),
        (590, Token.Text.Whitespace, '\n'),
        (591, Token.Keyword, 'changed'),
        (598, Token.Punctuation, ':'),
        (599, Token.Text, ' '),
        (600, Token.Punctuation, '['),
        (601, Token.Name.Variable, 'localhost'),
        (610, Token.Punctuation, ']'),
        (611, Token.Text, '\n'),
        (612, Token.Text.Whitespace, '\n'),
        (613, Token.Keyword, 'TASK'),
        (617, Token.Text, ' '),
        (618, Token.Punctuation, '['),
        (619, Token.Literal, 'volumes (more volumes)'),
        (641, Token.Punctuation, ']'),
        (642, Token.Text, ' '),
        (
            643,
            Token.Name.Variable,
            '*' * 116,
        ),
        (759, Token.Text, '\n'),
        *(
            (
                (
                    760,
                    Token.Text.Whitespace,
                    'Sunday 11 November 2018  20:19:25 +0100 (0:00:00.607)       '
                    '0:10:36.974 *******\n',
                ),
            ) if IS_OLD_PYGMENTS_PRE_2_14 else (
                (
                    760,
                    Token.Text,
                    'Sunday 11 November 2018  20:19:25 +0100 (0:00:00.607)       '
                    '0:10:36.974 *******',
                ),
                (839, Token.Text.Whitespace, '\n'),
            )
        ),
        (840, Token.Generic.Deleted, '--- before'),
        (850, Token.Text.Whitespace, '\n'),
        (851, Token.Generic.Inserted, '+++ after'),
        (860, Token.Text.Whitespace, '\n'),
        (861, Token.Generic.Subheading, '@@ -1,11 +1,11 @@'),
        (878, Token.Text.Whitespace, '\n'),
        (879, Token.Text.Whitespace, ' '),
        (880, Token.Text, '{'),
        (881, Token.Text.Whitespace, '\n'),
        (882, Token.Text.Whitespace, ' '),
        (883, Token.Text, '  "expected_binds": ['),
        (904, Token.Text.Whitespace, '\n'),
        (905, Token.Generic.Deleted, '-    "/tmp:/tmp:rw",'),
        (925, Token.Text.Whitespace, '\n'),
        (926, Token.Generic.Deleted, '-    "/:/whatever:rw,z"'),
        (949, Token.Text.Whitespace, '\n'),
        (950, Token.Generic.Inserted, '+    "/tmp:/somewhereelse:ro,Z",'),
        (982, Token.Text.Whitespace, '\n'),
        (983, Token.Generic.Inserted, '+    "/tmp:/tmp:rw"'),
        (1002, Token.Text.Whitespace, '\n'),
        (1003, Token.Text.Whitespace, ' '),
        (1004, Token.Text, '  ],'),
        (1008, Token.Text.Whitespace, '\n'),
        (1009, Token.Text.Whitespace, ' '),
        (1010, Token.Text, '  "expected_volumes": {'),
        (1033, Token.Text.Whitespace, '\n'),
        (1034, Token.Generic.Deleted, '-    "/tmp": {},'),
        (1050, Token.Text.Whitespace, '\n'),
        (1051, Token.Generic.Deleted, '-    "/whatever": {}'),
        (1071, Token.Text.Whitespace, '\n'),
        (1072, Token.Generic.Inserted, '+    "/somewhereelse": {},'),
        (1098, Token.Text.Whitespace, '\n'),
        (1099, Token.Generic.Inserted, '+    "/tmp": {}'),
        (1114, Token.Text.Whitespace, '\n'),
        (1115, Token.Text.Whitespace, ' '),
        (1116, Token.Text, '  },'),
        (1120, Token.Text.Whitespace, '\n'),
        (1121, Token.Text.Whitespace, ' '),
        (1122, Token.Text, '  "running": true'),
        (1139, Token.Text.Whitespace, '\n'),
        (1140, Token.Text.Whitespace, ' '),
        (1141, Token.Text, '}'),
        (1142, Token.Text.Whitespace, '\n'),
        *(
            (
                (
                    1143,
                    Token.Text.Whitespace,
                    '\\ No newline at end of file\n',
                ),
            ) if IS_OLD_PYGMENTS_PRE_2_14 else (
                (1143, Token.Text, '\\ No newline at end of file'),
                (1170, Token.Text.Whitespace, '\n'),
            )
        ),
        (1171, Token.Text.Whitespace, '\n'),
        (1172, Token.Keyword, 'changed'),
        (1179, Token.Punctuation, ':'),
        (1180, Token.Text, ' '),
        (1181, Token.Punctuation, '['),
        (1182, Token.Name.Variable, 'localhost'),
        (1191, Token.Punctuation, ']'),
        (1192, Token.Text, '\n'),
    ]

    unprocessed_text_tokens = list(
        _get_lexer_by_name('ansible-output').
        get_tokens_unprocessed(ansible_play_output_example),
    )
    assert unprocessed_text_tokens == expected_resulting_text_tokens
