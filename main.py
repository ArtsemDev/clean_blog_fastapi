from core.models import Post


async def insert_posts():
    posts = [
        {'title': 'Великий пост 1', 'body': 'Описание <b>первого</b> великого поста', 'slug': 'velikiy-post-1'},
        {'title': 'Великий пост 2', 'body': 'Описание <b>второго</b> великого поста', 'slug': 'velikiy-post-2'},
        {'title': 'Великий пост 3', 'body': 'Описание <b>третьего</b> великого поста', 'slug': 'velikiy-post-3'},
        {'title': 'Великий пост 4', 'body': 'Описание <b>четвертого</b> великого поста', 'slug': 'velikiy-post-4'},
        {'title': 'Великий пост 5', 'body': 'Описание <b>пятого</b> великого поста', 'slug': 'velikiy-post-5'},
    ]
    for post in posts:
        post = Post(**post)
        await post.save()

import asyncio
asyncio.run(insert_posts())
