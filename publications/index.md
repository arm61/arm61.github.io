---
layout: default
---

<h1>Publications</h1>

{% for pub in site.data.publications reversed %}
  <body>
  <b>
    {{ pub.title }}
  </b><br>
  <small>
    <i>{{ pub.journal }}</i>, 
    {% if pub.volume.size > 0 %}
        <b>{{ pub.volume }}</b>
    {% endif %}
    {% if pub.issue.size > 0 %}
        ({{ pub.issue }}), 
    {% endif %}
    {% if pub.pages.size > 0 %}
    {{ pub.pages}},
    {% endif %}
    {{ pub.year }}
    {% if pub.paper.size > 0 %}
         &mdash; <a href="{{ pub.paper }}">Paper</a>
    {% endif %}
    {% if pub.thesis.size > 0 %}
         &mdash; <a href="{{ pub.thesis }}">Thesis</a>
    {% endif %}
    {% if pub.code.size > 0 %}
         | <a href="{{ pub.code }}">Code</a>
    {% endif %}
    {% if pub.docs.size > 0 %}
         | <a href="{{ pub.docs }}">Docs</a>
    {% endif %}
    {% if pub.esi.size > 0 %}
         | <a href="{{ pub.esi }}">ESI</a>
    {% endif %}
    {% if pub.data.size > 0 %}
         | <a href="{{ pub.data }}">Data</a>
    {% endif %}
    {% if pub.oer.size > 0 %}
         | <a href="{{ pub.oer }}">OER</a>
    {% endif %}
    {% if pub.arxiv.size > 0 %}
         | <a href="{{ pub.arxiv }}">arXiv</a>
    {% endif %}
    {% if pub.chemrxiv.size > 0 %}
         | <a href="{{ pub.chemrxiv }}">ChemRxiv</a>
    {% endif %}
    <br>
    {{ pub.authors | join: ", " }}
  <br>
  <i>{{ pub.caption }}</i>
  </small>
  </body>
  <hr>
{% endfor %}
