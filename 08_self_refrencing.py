from pydantic import BaseModel
from typing import Optional,List


class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List["Comment"]] = None


Comment.model_rebuild()  # To handle self-referencing models and increase performance otherwise you will get a major degradation
comment_1 = Comment(id=1,content="This is the first comment")
comment_2 = Comment(id=2,content="This is the second comment",replies=[comment_1])
comment_3 = Comment(id=3,content="This is the third comment",replies=[comment_1,comment_2])

print(comment_3.model_dump())