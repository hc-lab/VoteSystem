from django.contrib import admin

# Register your models here.
from VoteSystem.models import  Person, Candidate, RegisterCandidate, SufrageTable, RegisterVote
admin.site.register(Person)
admin.site.register(Candidate)
admin.site.register(RegisterCandidate)
admin.site.register(SufrageTable)
