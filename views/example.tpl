<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>sample</title>
<link href="/css/main.css" media="screen" rel="stylesheet" type="text/css">
</head>
<body>
<div>
<p>こんにちは</p>
{{("<script>alert('sample')</script>")}}
<p>
%if 3 % 2 == 1:
ここは表示される
%else:
ここは表示されない
%end
</p>
</div>
</body>
</html>
