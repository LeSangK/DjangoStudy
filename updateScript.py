from snippets.models import Snippet

snippet = Snippet.objects.get(id=2)
snippet.title = "おはようございます、世界"
snippet.code = 'print("Good Morning, World!")'
snippet.description = "朝の挨拶"
snippet.save()
print("スニペットを更新しました", snippet)
