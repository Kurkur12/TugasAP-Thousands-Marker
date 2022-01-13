from django.shortcuts import render
from time import ctime
from .myutils import number_of_consonants, number_of_vowels, showDate, calculateTax, thousandsMarkerCur

def code(request):
    k = showDate()
    context = {
        'judul' : 'Tugas AP 2021 keren',
        'nama'  : 'Kurniawan Bagaskara',
        'NIM'   : 'L200214253',
        'waktu' : k,
        'pesan' : 'bismillah',
    }




    if request.POST:
        rt = request.POST.get('tax')
        try:
            if int(rt) > 0:
                resultTaxt = calculateTax(int(rt))
                total = 0
                for x in resultTaxt:
                    total += int(x[2].replace("Rp ", "").replace(".", ""))
                total = thousandsMarkerCur(total)
                rtCur = thousandsMarkerCur(int(rt))
                context.update({"rt" : rt, "rtCur" : rtCur , "resultTax" : resultTaxt, "totalTax" : total, })
            else:
                context.update({"exc":"Please insert positive integer! "})
                
        except:
            context.update({"exc":"Please insert positive integer! "})
        # vo = countVowels(rt)
        # co = countConsonants(rt)
    
    return render(request , 'pajak/index.html', context)
def about(request):
    return render(request, 'pajak/about.html')