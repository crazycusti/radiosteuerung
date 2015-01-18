<!doctype HTML>
<html>
<head>
	<title>Radiosteuerung</title>
	<style>
		body, button {
			font-size: 18px;
			font-family: Helvetica, Arial, sans-serif;
		}
		button {
			min-height: 3em;
		}
	</style>
	<script>
		var x = new XMLHttpRequest();
		function handler() {
			if (x.readyState == 4 && x.status == 200) {
				setTimeout(function() { location.reload(); }, 500);
			}
		}
		function toggle() {
			x.open('GET', '/do/{{"stop" if playstate else "play"}}');
			x.onreadystatechange = handler;
			x.send(null);
			return true;
		}
	</script>
</head>
<body>
	<h1>Radiosteuerung</h1>
	<p>Das Radio <b>{{'läuft' if playstate else 'läuft nicht'}}</b> im Moment.</p>
	<button id="toggleradio" style="width: 100%" onclick="toggle()">{{'STOP' if playstate else 'PLAY'}}</button>
</body>
</html>
