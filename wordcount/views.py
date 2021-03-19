from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#Counting algorithm (Fix later)

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()


    worddictionary = {} #empty dictionary that will contain words from wordlist

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)

    return  render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddictionary': sortedwords })
