<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Sample</title>
<link href="/css/main.css" media="screen" rel="stylesheet" type="text/css">
</head>
<body>
<div class="container">
<h1>Sample</h1>
<div class="submit">
<form method="post" action"/" enctype="multipart/form-data">
	<div class="form-text">
	<textarea rows="10" cols="30" name="ex_text" id="ex-text"></textarea>
	</div>
	<div class="form-file">
	<input type="file" name="file">
	</div>
	<div class="form-submit">
	<input type="submit" name="submit" value="sumbit">
	</div>
</form>
</div>
%from main import nl2br
%for post in posts:
<div class="post">
	{{!nl2br(post[1])}}
</div>
<div class="post-image">
<img src="/uploads/{{post[2]}}" alt="{{post[2]}}" class="ex-image">
</div>
%end
</div>
<script src="/js/main.js"></script>
</body>
</html>
