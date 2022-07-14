from django import forms
from bolg.models imports Comment

class CommentForm(fomrs.ModelForm):
  class Meta:
    model = Comment
    fields =["comment"]
    