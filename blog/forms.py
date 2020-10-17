from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import BlogPost, Category


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


cat_choice = Category.objects.all().values_list('name', 'name')

cat_choice_list = []

for choice in cat_choice:
    cat_choice_list.append(choice)


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'header_image', 'snippet', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cat_choice_list, attrs={'class': 'form-control'}),
            # 'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'author', 'type': 'hidden'}),
            'body': SummernoteInplaceWidget(),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'header_image', 'snippet', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cat_choice_list, attrs={'class': 'form-control'}),
            'body': SummernoteInplaceWidget(),
        }

