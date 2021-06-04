# Author: Felix Fontein <felix@fontein.de>
# License: BSD-2-Clause
# Copyright: Felix Fontein <felix@fontein.de>, 2021
"""Tests for Pygments lexers."""

from pygments import highlight
from pygments.formatters import HtmlFormatter

from ansible_pygments.lexers import AnsibleOutputLexer


def run_test(data, lexer):
    """Format the data snippet as HTML using a given lexer."""
    formatter = HtmlFormatter()
    result = highlight(data, lexer, formatter)
    return formatter.get_style_defs('.highlight'), result


def test_ansible_output_lexer():
    """Test that AnsibleOutputLexer produces expected HTML output."""
    data = R"""
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
    _, result = run_test(data, AnsibleOutputLexer())
    print(result)

    assert result == R"""<div class="highlight"><pre><span></span><span class="k">ok</span><span class="p">:</span> <span class="p">[</span><span class="nv">windows</span><span class="p">]</span> <span class="p">=&gt;</span> <span class="p">{</span>
    <span class="nt">&quot;account&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="nt">&quot;account_name&quot;</span><span class="p">:</span> <span class="s">&quot;vagrant-domain&quot;</span><span class="p">,</span>
        <span class="nt">&quot;type&quot;</span><span class="p">:</span> <span class="s">&quot;User&quot;</span>
    <span class="p">},</span>
    <span class="nt">&quot;authentication_package&quot;</span><span class="p">:</span> <span class="s">&quot;Kerberos&quot;</span><span class="p">,</span>
    <span class="nt">&quot;user_flags&quot;</span><span class="p">:</span> <span class="p">[]</span>
<span class="p">}</span>

<span class="k">TASK</span> <span class="p">[</span><span class="l">paused</span><span class="p">]</span> <span class="nv">************************************************************************************************************************************</span>
Sunday 11 November 2018  20:16:48 +0100 (0:00:00.041)       0:07:59.637 *******
<span class="gd">--- before</span>
<span class="gi">+++ after</span>
<span class="gu">@@ -1,5 +1,5 @@</span>
 {
<span class="gd">-  &quot;exists&quot;: false,</span>
<span class="gd">-  &quot;paused&quot;: false,</span>
<span class="gd">-  &quot;running&quot;: false</span>
<span class="gi">+  &quot;exists&quot;: true,</span>
<span class="gi">+  &quot;paused&quot;: true,</span>
<span class="gi">+  &quot;running&quot;: true</span>
 }
\ No newline at end of file

<span class="k">changed</span><span class="p">:</span> <span class="p">[</span><span class="nv">localhost</span><span class="p">]</span>

<span class="k">TASK</span> <span class="p">[</span><span class="l">volumes (more volumes)</span><span class="p">]</span> <span class="nv">********************************************************************************************************************</span>
Sunday 11 November 2018  20:19:25 +0100 (0:00:00.607)       0:10:36.974 *******
<span class="gd">--- before</span>
<span class="gi">+++ after</span>
<span class="gu">@@ -1,11 +1,11 @@</span>
 {
   &quot;expected_binds&quot;: [
<span class="gd">-    &quot;/tmp:/tmp:rw&quot;,</span>
<span class="gd">-    &quot;/:/whatever:rw,z&quot;</span>
<span class="gi">+    &quot;/tmp:/somewhereelse:ro,Z&quot;,</span>
<span class="gi">+    &quot;/tmp:/tmp:rw&quot;</span>
   ],
   &quot;expected_volumes&quot;: {
<span class="gd">-    &quot;/tmp&quot;: {},</span>
<span class="gd">-    &quot;/whatever&quot;: {}</span>
<span class="gi">+    &quot;/somewhereelse&quot;: {},</span>
<span class="gi">+    &quot;/tmp&quot;: {}</span>
   },
   &quot;running&quot;: true
 }
\ No newline at end of file

<span class="k">changed</span><span class="p">:</span> <span class="p">[</span><span class="nv">localhost</span><span class="p">]</span>
</pre></div>
"""
