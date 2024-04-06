from django.contrib.auth.models import User
from snippets.models import Snippet

admin_user = User.objects.get(username="admin")
snippet = Snippet(
    title="test_1",
    code='print("Hello, World!")',
    description="こんにちは！世界",
    created_by=admin_user,
)

snippet.save()

all = Snippet.objects.all()

print("スニペットを作成しました", all)
