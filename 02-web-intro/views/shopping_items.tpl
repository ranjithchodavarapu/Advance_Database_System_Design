<html>
<body>
<table>
% for item in shopping_item:
    <tr>
        <td>{{item['id']}}</td><td>{{item['desc']}}</td>>
        <td><a href = "/delete/{{item['id']}}">Remove</a></td>
        <td><a href = "/edit/{{item['id']}}">Edit</a></td>
    </tr>
%end
</table>
<hr/>
<a href="/add">Add an item</a>
</body>
</html>