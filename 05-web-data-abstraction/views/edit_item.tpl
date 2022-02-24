<html>
<body>
Edit this Item
<hr/>
<form action ="/edit/{{id}}" method ="post">
    <p>Edit Item:<input name="description" value="{{description}}"/></p>
    <p>Edit price:<input name="price" value="{{price}}"/></p>
    <p>Edit quantity:<input name="quantity" value="{{quantity}}"/></p>
    <p><button type ="submit">Edit</button></p>
</form>
<hr/>
<a href='/index'>Cancel</a>
</body>
</html>