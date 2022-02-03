<html>
<body>
<table>
% for item in shopping_item:
    <tr>
        <td>{{item['id']}}</td><td>{{item['desc']}}</td>><td><a href = "/delete/{{item['id']}}">Delete_items</a></td>
    </tr>
%end
</table>
</body>
</html>