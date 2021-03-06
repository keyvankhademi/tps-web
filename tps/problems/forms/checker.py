from django import forms

from problems.forms.files import SourceFileAddForm, SourceFileEditForm
from problems.forms.generic import ProblemObjectModelForm
from problems.models import SourceFile, Checker
from problems.models.problem_data import ProblemData


class CheckerAddForm(SourceFileAddForm):
    class Meta:
        model = Checker
        fields = ["name",]

    def save(self, commit=True):
        ret = super(CheckerAddForm, self).save(commit)
        problem_data = self.revision.problem_data
        if commit and problem_data.checker is None:
            problem_data.checker = self.instance
            problem_data.save()
        return ret
