{% extends "admin/base.html" %}
{% block title %}{% if project %}Edit{% else %}New{% endif %} Project — Admin{% endblock %}
{% block admin_content %}
<div class="eyebrow">{% if project %}Edit{% else %}New{% endif %}</div>
<h1 style="font-size:1.9rem;">{% if project %}Edit project{% else %}New project{% endif %}</h1>

<form method="POST" style="max-width:560px; margin-top:24px;">
  <div class="field" style="margin-bottom:16px;">
    <label>Project name</label>
    <input type="text" name="name" required style="width:100%;" value="{{ project.name if project else '' }}">
  </div>
  <div class="field" style="margin-bottom:16px;">
    <label>Location</label>
    <input type="text" name="location" required style="width:100%;" value="{{ project.location if project else '' }}">
  </div>
  <div class="field" style="margin-bottom:16px;">
    <label>Description</label>
    <textarea name="description" rows="4" style="width:100%;">{{ project.description if project else '' }}</textarea>
  </div>
  <div class="field" style="margin-bottom:20px;">
    <label>Cover image URL (optional)</label>
    <input type="text" name="cover_image" style="width:100%;" value="{{ project.cover_image if project else '' }}">
  </div>
  <button type="submit" class="btn btn-brass">{% if project %}Save changes{% else %}Create project{% endif %}</button>
  <a href="{{ url_for('admin_projects') }}" class="btn btn-outline">Cancel</a>
</form>
{% endblock %}
