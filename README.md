# pelican-ishomepage

Add Jinja global function `ishomepage(url, output_file)`.

Invoking this function in a template can tell whether the currently
generated page is front page or not. This dirty little hack is required
to correctly add e.g. `active` class to the home page menu element.

## Example configuration

```python
# Assume we have a home page menu item defined like this:

MENUITEMS = (
    ("Home", SITEURL + "/"),
)
```

## Example template usage

```python
{% if MENUITEMS %}
<ul class="menu">
{% for item, url in MENUITEMS %}
    <li>
        <a href="{{ SITEURL }}{{ url }}"
        {% if ishomepage(url, output_file) %} class="active"{% endif %}>
        {{ item | escape }}
        </a>
    </li>
{% endfor %}
</ul>
{% endif %}
```

## TODO

+ Make tests
+ Publish to PyPI
