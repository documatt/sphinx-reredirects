FAQ
####

Aren't 301 redirects better?
****************************

Client-side redirects with meta refresh are okay for search engines, even the most ancient browsers, and users too.

|project| extension was created for tech writers who don't want or can't manage redirects with server-side 301 redirects. Generally, SEO consultants recommend server-side redirects created with ``.htaccess`` and similar files. However, many documentation is hosted as on static website hosting which doesn't support server-side redirects.

I know better how to write HTML redirect file
*********************************************

By default, created HTML redirect files contains ``<html><head><meta http-equiv="refresh" content="0; url=${to_uri}"></head></html>``.

If you want JavaScript redirection instead, wait longer, or whatever, set ``redirect_html_template`` option. This option should points to file inside source dir (directory containing ``conf.py``). For example::

    redirect_html_template_file = "redirect.html.template"

Actual target URI requested in configuration is available under ``${to_uri}`` placeholder.

Why name "reredirects"?
***********************

Because the name "redirects" is already taken by `another <https://github.com/sphinx-contrib/redirects>`_ extension. Unfortunately, it doesn't fulfil our requirements (the most notable it doesn't support wildcards and placeholders). These were reasons why we decided to bring a new extension.
