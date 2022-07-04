from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# if you can't understand it, its not for you ha ha!
grid=[[' ']*9]*9
def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
def sol(grid):      
    for i in range(0,9):
        for j in range(0,9):
            # empty cell
            if(grid[i][j]==''):
                a = '123456789'
                for k in range(0,9):
                    if(isSafe(grid,i,j,a[k])):
                        grid[i][j]=a[k];                   
                        if(sol(grid)):
                            return True
                                
                        else:
                            grid[i][j]=''
                                
                            
                        
                return False
                    
                
            

    return True

 

def index(request):
    return render(request,'index.html')

def solve(request):
    dj1=request.POST.get('1','default')
    dj2=request.POST.get('2','default')
    dj3=request.POST.get('3','default')
    dj4=request.POST.get('4','default')
    dj5=request.POST.get('5','default')
    dj6=request.POST.get('6','default')
    dj7=request.POST.get('7','default')
    dj8=request.POST.get('8','default')
    dj9=request.POST.get('9','default')

    dj10=request.POST.get('10','default')
    dj11=request.POST.get('11','default')
    dj12=request.POST.get('12','default')
    dj13=request.POST.get('13','default')
    dj14=request.POST.get('14','default')
    dj15=request.POST.get('15','default')
    dj16=request.POST.get('16','default')
    dj17=request.POST.get('17','default')
    dj18=request.POST.get('18','default')

    dj19=request.POST.get('19','default')
    dj20=request.POST.get('20','default')
    dj21=request.POST.get('21','default')
    dj22=request.POST.get('22','default')
    dj23=request.POST.get('23','default')
    dj24=request.POST.get('24','default')
    dj25=request.POST.get('25','default')
    dj26=request.POST.get('26','default')
    dj27=request.POST.get('27','default')

    dj28=request.POST.get('28','default')
    dj29=request.POST.get('29','default')
    dj30=request.POST.get('30','default')
    dj31=request.POST.get('31','default')
    dj32=request.POST.get('32','default')
    dj33=request.POST.get('33','default')
    dj34=request.POST.get('34','default')
    dj35=request.POST.get('35','default')
    dj36=request.POST.get('36','default')

    dj37=request.POST.get('37','default')
    dj38=request.POST.get('38','default')
    dj39=request.POST.get('39','default')
    dj40=request.POST.get('40','default')
    dj41=request.POST.get('41','default')
    dj42=request.POST.get('42','default')
    dj43=request.POST.get('43','default')
    dj44=request.POST.get('44','default')
    dj45=request.POST.get('45','default')

    dj46=request.POST.get('46','default')
    dj47=request.POST.get('47','default')
    dj48=request.POST.get('48','default')
    dj49=request.POST.get('49','default')
    dj50=request.POST.get('50','default')
    dj51=request.POST.get('51','default')
    dj52=request.POST.get('52','default')
    dj53=request.POST.get('53','default')
    dj54=request.POST.get('54','default')

    dj55=request.POST.get('55','default')
    dj56=request.POST.get('56','default')
    dj57=request.POST.get('57','default')
    dj58=request.POST.get('58','default')
    dj59=request.POST.get('59','default')
    dj60=request.POST.get('60','default')
    dj61=request.POST.get('61','default')
    dj62=request.POST.get('62','default')
    dj63=request.POST.get('63','default')

    dj64=request.POST.get('64','default')
    dj65=request.POST.get('65','default')
    dj66=request.POST.get('66','default')
    dj67=request.POST.get('67','default')
    dj68=request.POST.get('68','default')
    dj69=request.POST.get('69','default')
    dj70=request.POST.get('70','default')
    dj71=request.POST.get('71','default')
    dj72=request.POST.get('72','default')

    dj73=request.POST.get('73','default')
    dj74=request.POST.get('74','default')
    dj75=request.POST.get('75','default')
    dj76=request.POST.get('76','default')
    dj77=request.POST.get('77','default')
    dj78=request.POST.get('78','default')
    dj79=request.POST.get('79','default')
    dj80=request.POST.get('80','default')
    dj81=request.POST.get('81','default')
    
    grid=[[dj1 ,dj2 ,dj3 ,dj4 ,dj5 ,dj6 ,dj7 ,dj8 ,dj9],[dj10,dj11,dj12,dj13,dj14,dj15,dj16,dj17,dj18],[dj19,dj20,dj21,dj22,dj23,dj24,dj25,dj26,dj27],[dj28,dj29,dj30,dj31,dj32,dj33,dj34,dj35,dj36],[dj37,dj38,dj39,dj40,dj41,dj42,dj43,dj44,dj45],[dj46,dj47,dj48,dj49,dj50,dj51,dj52,dj53,dj54],[dj55,dj56,dj57,dj58,dj59,dj60,dj61,dj62,dj63],[dj64,dj65,dj66,dj67,dj68,dj69,dj70,dj71,dj72],[dj73,dj74,dj75,dj76,dj77,dj78,dj79,dj80,dj81]] 
    sol(grid)
    a=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','xxx','sexy','hot','babe','me','iwill','become','first','trillionaire','if','youthink','its','ajoke','then','fuck','you','mothe','rf','uck','er']
    dict={}     
    for i in range(81):    
        dict[a[i]]=grid[int(i/9)][(i-int(i/9)*9)%9]
    print(dict)
    return render(request,'result.html',dict)


def solveanother(request):
    return render(request,'index.html')
