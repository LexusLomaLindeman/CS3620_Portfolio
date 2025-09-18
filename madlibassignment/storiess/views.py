from django.shortcuts import render,redirect
from .models import StoryInfo

# Create your views here.
def index(request):
   storyInfo = StoryInfo.objects.all()
   context = context = {'storyInfo':storyInfo}
   return render(request, "index.html",context)

def test(request):
   return render(request, "Stories/test.html")

def form(request , id):

   storySelected = StoryInfo.objects.get(id=id)
   context = {
         "storySelected": storySelected,
         "nounRange": range(storySelected.noun),
         "verbRang":range(storySelected.verbcount),
         "adjectiveRange": range(storySelected.adjective),
         "pronounsRange": range(storySelected.pronouns),
         "nameRange":range(storySelected.names)
    }

   return render(request, 'form.html',context)

def storySelected(request,selectedStory):
    if request.method == "POST":
        nouns = []
        verb = []
        adjective= []
        pronouns = []
        name =[]

        for key, value in request.POST.items():
            if key.startswith("noun"):
                nouns.append(value)

            if key.startswith("verb"):
                verb.append(value)

            if key.startswith("adjective"):
                adjective.append(value)

            if key.startswith("pronouns"):
               pronouns.append(value)

            if key.startswith("name"):
               name.append(value)

        context = {
            'nouns': nouns,
            'verb': verb,
            'adjective': adjective,
            'pronouns': pronouns,
            'name': name
        }
        storySelected = f"{selectedStory}.html"
        return render(request, storySelected, context)

    else:
        return redirect('index') 
