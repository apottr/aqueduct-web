<html>
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.13/semantic.min.css" />
  <script src="https://cdnjs.cloudflare.com/ajax/libs/viz.js/1.8.0/viz-lite.js">
  </script>
</head>
<body>
  <div class="ui grid">
    <div class="two wide column"></div>
    <div class="twelve wide column">
      {% block content %}
      {% endblock %}
    </div>
    <div class="two wide column"></div>
  </div>
</html>
