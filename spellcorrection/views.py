from django.shortcuts import render
import language_tool_python

# Create your views here.
def home(request):
    return render(request, "spellcorrection/home.html",{'result':'','txt':''})

def  res(request):
    print(request.POST['txt'])
    tool = language_tool_python.LanguageTool('en-US')
    text = request.POST['txt']
    result = tool.correct(text)
    return render(request, "spellcorrection/home.html",{'result':result,'txt':text})
