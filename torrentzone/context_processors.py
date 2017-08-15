from utils.titleSearcher import titleSearcher

def add_title(request):
    x2 = titleSearcher()
    lo = x2.search()
    return {"title":lo}
  
