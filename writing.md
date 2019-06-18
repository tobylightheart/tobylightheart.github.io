---
layout: page
title: Research
permalink: /research/
---

<h1>Online Writing</h1>

<ul class="post-list">
  {% for post in site.writing %}
    <li>
      <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

      <h2>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </h2>
    </li>
  {% endfor %}
</ul>


<h1>Publications</h1>

<ul class="post-list">
  {% for post in site.publications %}
    <li>
      <span>
        {{post.authors}} ({{post.year}}), {{post.title}}, <i>{{post.publication}}</i>, {{post.notes}}
        {% if post.media == "URL" %}
        {{post.media}}:
        <a href="{{post.web}}">{{post.web}}</a>
        {% else %}
        {{post.media}}
        {% endif %}     
      </span>

    </li>
  {% endfor %}
</ul>
