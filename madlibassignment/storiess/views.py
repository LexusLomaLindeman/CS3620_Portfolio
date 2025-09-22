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

def storySelected(request,id):

    selectedStory = StoryInfo.objects.get(id=id)

    if request.method == "POST":
        nouns = []
        verbs = []
        adjectives= []
        pronouns = []
        names =[]

        for key, value in request.POST.items():
            if key.startswith("noun"):
                nouns.append(value)

            if key.startswith("verb"):
                verbs.append(value)

            if key.startswith("adjective"):
                adjectives.append(value)

            if key.startswith("pronouns"):
               pronouns.append(value)

            if key.startswith("name"):
               names.append(value)
        
        newStory = selectedStory.story

        for i, verb in enumerate(verbs):
            placeholder = f"[verb{i}]"
            newStory = newStory.replace(placeholder, verb)
        
        for i, adjective in enumerate(adjectives):
            placeholder = f"[adjective{i}]"
            newStory = newStory.replace(placeholder, adjective)
        
        for i, noun in enumerate(nouns):
            placeholder = f"[noun{i}]"
            newStory = newStory.replace(placeholder, noun)

        for i, pronoun in enumerate(pronouns):
            placeholder = f"[pronoun{i}]"
            newStory = newStory.replace(placeholder, pronoun)

        for i, name in enumerate(names):
            placeholder = f"[name{i}]"
            newStory = newStory.replace(placeholder, name)
  

        context = {
            'storyName':selectedStory.storyName,
            'story': newStory,
        }
        return render(request, 'story.html',context)

    else:
        return redirect('index') 
