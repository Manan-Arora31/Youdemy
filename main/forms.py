from django import forms
from django.forms import modelformset_factory
from main.models import Courses, Chapters, Titles, Questions
class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('course_name', 'description', 'course_pictire', 'course_language')
        labels = {
            'course_name': 'Course Name',
            'description': 'Description',
            'course_pictire': 'Course Picture',
            'course_language': 'Course Language',
        }
        widgets = {
            'course_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course Name here'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course Description here'
            }),
            'course_pictire': forms.FileInput(attrs={
                'class': 'form-control-file',
                'required':False,
            }),
            'course_language': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course Language here'
            }),
        }
ChapterFormset = modelformset_factory(
    Chapters,
    fields=('chapter_name','description','chapter_pictire' ),
    extra=1,
    widgets={
        'chapter_name': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Chapter Name here'
            }),
        'description': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Chapter Description here'
            }),
    }
)
TitleModelFormset = modelformset_factory(
    Titles,
    fields=('title_name','description','title_pictire'),
    extra=1,
    widgets={'title_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Title Name here'
        }),
        'description': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Title Description here'
        }),
    }
)
QuestionModelFormset = modelformset_factory(
    Questions,
    fields=('question','answer'),
    extra=1,
    widgets={'question': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Question here'
        }),
        'answer': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Answer here'
        }),
    }
)