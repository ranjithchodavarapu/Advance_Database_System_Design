<html>
<body>
Edit this Item
<hr/>
<form action ="/edit/{{id}}" method ="post">
    <p>Edit Item:<input name="description" value="{{description}}"/></p>
    <p><button type ="submit">Edit</button></p>
</form>
<hr/>
<a href='/index'>Cancel</a>
</body>
</html>