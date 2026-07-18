<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{% block title %}Admin — Meridian Land{% endblock %}</title>
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
<div class="admin-shell">
  <aside class="admin-sidebar">
    <div class="brand"><span class="mark"></span>Meridian</div>
    <nav>
      <a href="{{ url_for('admin_dashboard') }}" class="{% if request.endpoint=='admin_dashboard' %}active{% endif %}">Dashboard</a>
      <a href="{{ url_for('admin_projects') }}" class="{% if request.endpoint and request.endpoint.startswith('admin_project') %}active{% endif %}">Projects</a>
      <a href="{{ url_for('admin_plots') }}" class="{% if request.endpoint and request.endpoint.startswith('admin_plot') %}active{% endif %}">Plots</a>
      <a href="{{ url_for('admin_inquiries') }}" class="{% if request.endpoint=='admin_inquiries' %}active{% endif %}">Enquiries</a>
      <a href="{{ url_for('admin_site_visits') }}" class="{% if request.endpoint=='admin_site_visits' %}active{% endif %}">Site visits</a>
      <a href="{{ url_for('home') }}" target="_blank" style="margin-top:20px;opacity:0.7;">View live site ↗</a>
      <a href="{{ url_for('admin_logout') }}" style="opacity:0.7;">Log out</a>
    </nav>
  </aside>
  <main class="admin-main">
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        {% for category, message in messages %}
          <div class="flash {% if category=='error' %}flash-error{% endif %}">{{ message }}</div>
        {% endfor %}
      {% endif %}
    {% endwith %}
    {% block admin_content %}{% endblock %}
  </main>
</div>
</body>
</html>
