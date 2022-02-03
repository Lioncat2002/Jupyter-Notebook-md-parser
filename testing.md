## RECURSIONS



```python
###PRINTING N FACTORIAL USING RECURSION:

def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)
n=int(input("ENTER THE NUMBER: "))
print(fact(n))
```

    ENTER THE NUMBER: 5
    120
    


```python
###PRINTING SUM OF "N" NATURAL NUMBERS

def sum_n(n):
    if n==0:
        return 0
    smalloutput= sum_n(n-1)
    return (n + smalloutput)
n=int(input("ENTER THE NTH NUMBER:"))
print(sum_n(n))


```

    ENTER THE NTH NUMBER:10
    55
    


```python
###POWER OF A NUMBER
def power(x,n):
    if n==0:
        
        return 1
    elif n==1:
        
        return x
    else:
        
        smalloutput=power(x,n-1)
        return (x*smalloutput)
x,n=input("Enter the number followed by the power:").split()
x=int(x)
n=int(n)
print(power(x,n))
```

    Enter the number followed by the power:3 3
    27
    


```python
###PRINTING NATURAL NUMBERS TILL "N" STARTING FROM 1:

def print_natural(n):
    if n==0:
        return
    print_natural(n-1)
    print(n)
    return
n=int(input("ENTER THE NUMBER:"))
print_natural(n)
    
```

    ENTER THE NUMBER:10
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    


```python
###FIBONACCI ELEMENT

def fibo(n):
    if n==1:
        return 1   #####can also use this: if n==1 or n==2:
                    ####                     return 1
    elif n==0:
        return 0
    fibo_n_1=fibo(n-1)
    fibo_n_2=fibo(n-2)
    return (fibo_n_1+fibo_n_2)

n=int(input("Enter the element you want to find:"))
fibo(n)
```

    Enter the element you want to find:23
    




    28657




```python
####RECURISON DEPTH , on this machine it is around 2900
import sys
sys.setrecursionlimit(5000)
print(fact(3000))

```

    41493596034378540855568670930866121709511191949318099176894676576975585651235319500860007652178003420075184635383617118495750871114045907794553402161068339611621037904199177522062663390179682805164719697495968842457728766097103003726111095340241127118833157738815328438929737613021106312930374401485378725446079610290429491049793888120762511625132917004641668962117590203575175488980653577868915285093782469994674699190832093511068363824287063522268544339213775150488588104036818809099292912497141900508938994404715351473154531587441509960174267875087460367974117072368747277143988920683691618503608198459718093784453523958505377611086511162363145920886108557450874513945305436213711898150847192094426374203275029996333784944014775671414680824207499914714878359669720638954670589960178569480263388767112871068004950827400717124819476386401369193544354120312786601434792549959143530120653103406625503231020738351502195103148673612338739395096551462159349015789949944072311004426924838140141455487872738045856023561583204317945953055830693351246890721246151468485308724031267967089113548982733475375756899365176396424781733462510879015743437398920492267098317033932107176343983352444576040476565400414414699479984354554597799386702839428513413188913165695310848513525094006147774047007331406541794428004436691903685469270857271701648011512057452448607968773784803660653009109815639091294110633715621540903800135058671624262333902434166628716521228590274568833504897926869369792878376894841436573866436955075473964882256222183380014600761196859217603234808467455216330411738004331144225926243690558782914907973885758784585739828695390302383837265882427654306437517757897215045071361801730051628424476294227485755627828763498767195281368913583918824499284741591683130334032199946752082914885764345863832313545205075955912062067273296951386122994658607527317884452449865348164169238844889061495850934373442889814884427321817131272533891534506581143823381205875379808605080889761753882896252933633750454549168600267229591225528854584482686655324313011353754812409561237686078007700707939541848907149467377854407528307872988103912945121929864793703451257436445581459757140822705986325165352906584571123585270211933452981105568398809884094980346185078025273038736784042169427237980464304250045030806637032760016341921442805708802430850567892108646977455139539119838636167190300278146380136932482332771595180596193069504237836082620570887209297929797429404576877338319877444685544294800321741056689423710545028870419611915072739000031642014474213323293871618029555614004602867400422885389854650328028428515122296028795741801621823236098320971441047012533067314896153236788734984553949604397050352347766211395914519270422122231426998692087463520980686224354813376194395131942868113486531562228173214976481705381846155326596187530296478601160872263640443922257601926494610916885151013143945574398303192557154162151442469122370519149097861849436150963109933639594561796593396851958605338631176324147066842257192394742531726479559749993283247279807896470753054014194090200609712674753186365525403212757757853930697530056595208207457499471898144453772248207888443335118545601568853708182892895218300139654376947286418776665762815389737340159410543681435437346134244692067070082782423645557450882556670157242752810317141640631410681384330924027281318960884813040665226169552825637183862464944295688859393846726723694199475571320546018263425731029115353532728808182773021596787088437293412117084511580629967697266601663635276959969021502122104954259567278593185516268447100374434620422003535391203738393095420695021486207390653190910821344334251497896284236198571674773848126097443055036250866354720730971298084697196537722779893160200560725058007512407494448163392214398118492748281978655178478547749198714138485042290383954090570842038137277135667703565041081780520695032136233521692740531015340921761834078817735674646749071616600653230438902639786065509005309872435445689315601329942407112295015453771521051942445512795364971214872222193729289159833001742397977592530501318837883494884232222507318816399438935627817102875432588794558857742780390717166381257903798149148445526885871629931014510733215554773264576035916184298708323237568837917135073006026738292294687081030751946020376438138677107333779312582257356435534577162804030480925785909747233413932904072239860005448269296110393640127539539899397420021925268928622564959279136369546983247314494094297494213208716963662812963846191378114609210701033012119934264941666449130310898493535366401831282683112506578386425906537197010907276429330534751297336716929415047870949241778121534979499449732358445130210029720359993576507730563696950539990891252004810120090569633144368179194247963563389102486250773367249399801723451627048850149438343735826440053481474957421328873648479589553843836378275601433377798816126854462406494134416119108952653326761627660221130879211665924379496534838030236064294981985541014311566601739518539426008673198564586684635442730180022292607589767192198367529528365158715521887698317999005853121518691037776676883654291247419826099434535671529412823837612115555686210454583810355154404953718470726363218532775486501811002621331228429860926112159573066023932077476742800909462674322138805290643067711276964013735906251051050623568241317651533030775358975134565147424167401517470720839101869989993279364910892687924739705814152855543965954222603919059265825637344676406359525838966981511983959886603683753042017990328185945569412550519066302854869533377682984600031808093822130038102214387057461181304251961916405970456035183121708151658647356556540532928411748628957082856792300053525846377061280591452035546389932127875906349627837975871352588618213252263577038396202737385324908353680497990085701522483303439525197344653342994652565236096742834550523739733902374261808871799283722285366293439240895762913154442106573609205481842139365893867715542842477275100166734357743093638948444564764377184073874379471007867151070449554657626281566137550730763768080600031844296233977808233311359787577136983012817571625671683287281511937336685789437109097748581222868126824122317272681184975207863453107495331708260153159440253645365524453587952034745213429248916644504804355352281977721981971869054884176896398782704782066126921472548618247859626434279190274503452994769367997217285165465591799471789067885687278574470084289723778234763080740919512966238346427839653865017324665850192144091694630371265581197700774682562035198318782913591013997817303635173764706714383992810291224460848320518983248348855131025539721583184931653670732273172995431750775475634748127320956655431851879586978172491721700865768098908327830838240437737974455342525688712898855513180967012497859454290609627370590659970784172738420721605576789060565167694565490120388165775861939230924362983389549857279874523398090499858467484850399509109398834210424693113617875978611803096108774362764990414655167545507613665725914993376114340243762910290384135888531312591132544849225896007184851169390193985434649415483782338302531368775990005443722332901462568184095998830522521585328599833990336595418932696680163265899358234663247080324020429791357425755498549372896192091650794671997121439832581553945835125648010889886887056882711222628734035772418424803231173027338442220604015609242079569493204943809402465562530303328824165302038006041288444384884189129393985971765670211501611340121169355535864984802941563238279447576315042685734269863116562800932164578165410411899078396210758605145091526528422433647230880469088426412525126584729134059195171754291152622002229756986927959124620964363057052133099216422258437651889193630329851223282950806126200573565554213183555838289318138795940962303792777230344423432341561603558590502324475274502630869831414125396371754413611897269158650716722308083435295578401087236027347001118786146233185439431057058483770474806035004556885020602730222256397630738939985024978155182679916994164145540329909813190506654358156657691529068908186204138444091456355291242064901717436430473455191375922914953282988151808740076733486997695322871450791584448703980405737673555777873593937891577147956023340708456392314170118392555234618119775915673385955919265270624063734277760215846511035368057963320714896942663358570375305829676608224208465464558556667889222627619990263961792637457851652540918756608543859661221944248720424960000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    


```python
###checking whether a list is sorted or not 
def isSorted(a):
    l=len(a)
    if l==0 or l==1:
        return True
    
    if a[0]>a[1]:
        return False
    b=a[1:]
    isSmallerListSorted=isSorted(b)
    # return isSmallerListSorted
    if isSmallerListSorted:
        return True
    else:
        return False
a=[1,2,3,4,5]
        
    
print(isSorted(a))
```

    True
    


```python
#Given an array of length N, you need to find and return the sum of all elements of the array.
def arraysum(a):
    if not a:
        return 0
    else:
        return a[0] + arraysum(a[1:])
    
a=[1,2,3,4,5,6,7,8,9,10]
arraysum(a)
        
    
```




    55




```python
### CHECK whetther the given element is present in an array or not, if present return True else return False
def checkele(arr,x):
    if not arr:
        return False
    if arr[0]==x:
        return True
    else:
        return checkele(arr[1:],x)
    
    
    
    
    
    
    




arr=[15,24, 58 ,61, 79, 3 ,97, 81, 81, 45, 62, 21, 72, 72, 68, 45, 11, 50, 87, 20, 28, 77, 51, 89 ,58 ,66 
,23]
x=23
print(checkele(arr,x))
```

    True
    


```python
####CHECKING WHETHER AN ARRAY IS SORTED OR NOT (LESS MEMORY USAGE)
def isSortedBetter(arr,si=0):
    l=len(arr)
    if si==l-1 or si==l:
        return True
    if arr[si]>arr[si+1]:
        return False
    isSmallerListSorted=isSortedBetter(arr,si+1)
    return isSmallerListSorted
arr=[1,2,3,69,96]
isSortedBetter(arr)
```




    True




```python
###WAP TO RETURN THE INDEX OF FIRST OCCURENCE OF AN ELEMENT IN AN ARRAY
def firstindex(arr,x,si=0):
    if not arr or si==len(arr):
        return False
    
    if arr[si]==x:
        return si
    return firstindex(arr,x,si+1)
    
    
    
    
    
arr=[69,2,34,5,6,2342,69,612312,3414,12,1,69]
x=0
print(firstindex(arr,x))
```

    False
    


```python
###WAP TO RETURN THE INDEX OF THE FIRST OCCURENCE OF AN ELEMENT IN AN ARRAY(WITH MAKING NEW LISTS)
def firstIndex(arr, x):
    # Please add your code here
    if not arr:
        return -1
    if arr[0]==x:
        return 0
    smallerlist=firstIndex(arr[1:],x)
    if smallerlist<0:
        return smallerlist
    return smallerlist + 1
arr=[1,2,3,4,5,667,23,69,123,45,67,34,2,4,69]
x=69
firstindex(arr,x)
```




    7




```python
###WAP TO RETURN THE INDEX OF THE LAST OCCURENCE OF AN ELEMENT IN AN ARRAY
def lastindex(arr,x):
    if not arr:
        return -1
    smallerlist=lastindex(arr[1:],x)
    if smallerlist>=0:
        return smallerlist + 1
    if arr[0]==x:
        return 0
    return -1

arr=[1,1,23,5,3,6,23,1,3134,5]
x=5
lastindex(arr,x)
        
    
        
        
        
    
    
    
```




    9




```python
def lastindex(a,x):
    l=len(a)
    if l==0:
        return -1
    smallerList=a[1:]
    smallerListOutput= lastindex(smallerList,x)
    if smallerListOutput!=-1:
        return smallerListOutput + 1
    else:
        if a[0]==x:
            return 0
        else:
            return -1
a=[1,1,23,5,3,6,23,1,3134,5]
x=99
lastindex(a,x)
```




    -1




```python
####checking whether a word is a palindrome or not 

def chkpalindrome(string):
    if not string or len(string)==1:
        return True
    else:
        return string[0]==string[-1] and chkpalindrome(string[1:-1])
    
string="racecar"
chkpalindrome(string)
```




    True




```python
###replace a character in a string with a given character 
def replaceChar(string,a,b):
    if len(string)==0:
        return string
    smallOutput = replaceChar(string[1:],a,b)
    if string[0]==a:
        return b + smallOutput
    else:
        return string[0] + smallOutput
    
replaceChar("dacdxcd","c","x")
```




    'daxdxxd'




```python
###elements of an array


def elements (arr,count=0):
    if count==len(arr):
        return
    else:
        print(arr[count])
        elements(arr,count + 1)
        
arr=[1,2,3,4,5,6,7,8]
elements(arr)
```

    1
    2
    3
    4
    5
    6
    7
    8
    


```python
###elements of an array in reverse order


def revelements(arr,count=-1):
    if count<(-1*len(arr)):
        return
    else:
        print(arr[count])
        revelements(arr,count-1)
revelements([1,2,3,4,5,6,7,8])
```

    8
    7
    6
    5
    4
    3
    2
    1
    


```python
###reversing an array
def revlist(arr,start=0,end=len(arr)-1):
    if len(arr)==0 or len(arr)==1:
        return arr
    if start>=end:
        return arr
    
    arr[0],arr[-1]==arr[-1],arr[0]
    revlist(arr,start+1,end-1)
    
arr=[1,2,3,4,5]
print(revlist(arr))
print(arr)
    
```

    None
    [1, 2, 3, 4, 5]
    


```python
####removing X from a string 
def removex(string):
    if not string :
        return string
    if string[0]=='x':
        smalloutput=removex(string[1:])
        return "" + smalloutput
    else:
        smalloutput=removex(string[1:])
        return string[0] + smalloutput
string="xabcdxabcdxx"
print(removex(string))
    
```

    abcdabcd
    


```python
####REPLACE PI IN A STRING WITH 3.14
def replacePI(string):
    if len(string)==0 or len(string)==1:
        return string
    if string[0]=="p":
        if string [1]=="i":
            return "3.14"+ replacePI(string[2:])
        else:
            return string[0]+ replacePI(string[1:])
    else:
        return string[0]+ replacePI(string[1:])
string="pip"
print(replacePI(string))
```

    3.14p
    


```python
###remvoing consecutive duplicates  from a string recursively

def removeDup(string):
    if len(string)==0 or len(string)==1:
        return string
    smallstring=removeDup(string[1:])
    if string[0]==smallstring[0]:
        return string[0] + smallstring[1:]
    else:
        return string[0]+ smallstring
    
string="tadayutaysgcgtttggytytyyyikk"

print(removeDup(string))
```

    tadayutaysgcgtgytytyik
    


```python
###BINARY SEARCH WITH RECURSION 
def binarySearch(array,ele,si,ei):
    if si>ei:
        return -1
    mid = (si+ei)//2
    if array[mid]==ele:
        return mid 
    elif array[mid]>ele:
        return binarySearch(array,ele,si,mid-1)
    else:
        return binarySearch(array,ele,mid+1,ei)
    
array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ele=20
si=0
ei=len(array)-1
print(binarySearch(array,ele,si,ei))
```

    19
    


```python
'''MERGE SORT AS A SINGLE CALLABLE FUNCTION:
MERGE SORT IS VERY GOOD FOR BIG DATASETS AND PRETTY UNIVERSAL AS I DONT HAVE TO TAKE CARE OF SPECIAL CASES, BASIC IN ITS WORKING
AND VERY FAST WHEN COMPARED TO ITERATIVE SEARCHES SUCH AS BUBBLE SORT, SELECTION SORT ETC.THIS ONE IS NOT GONNA RETURN ANYTHING
AS LISTS ARE MUTABLE AND CAN BE CHANGED WHILE BEING INSIDE THE FUNCTION'''
def mergesort(arr):
    
    ###THIS IS THE MERGE PART FOR THE MAIN LIST AND WHERE MOST OF THE WORK HAPPENS :
    def merge(arr1,arr2,arr):
        i=0
        j=0
        k=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<=arr2[j]:
                arr[k]=arr1[i]
                i=i+1
                k=k+1
            else:
                arr[k]=arr2[j]
                j=j+1
                k=k+1
        while i<len(arr1):
            arr[k]=arr1[i]
            i=i+1
            k=k+1
        while j<len(arr2):
            arr[k]=arr2[j]
            j=j+1
            k=k+1
                
    ##recursive sorting part,THIS WILL CALL THE MERGE PART FOR EVERY ELEMENT AND THE RESULT WOULD BE A SORTED ARRAY
    def sort(arr):
        if len(arr)==0 or len(arr)==1:
            return arr
        mid=len(arr)//2
        arr1=arr[0:mid]
        arr2=arr[mid:]
        
        sort(arr1)
        sort(arr2)
        merge(arr1,arr2,arr)
        
    sort(arr)
        
arr=[int(ele) for ele in input("ENTER YOUR LIST OF ELEMENTS: ").split()]
mergesort(arr)
arr
        
```

    ENTER YOUR LIST OF ELEMENTS: 54 34 67 89 12 13 1 0 69
    




    [0, 1, 12, 13, 34, 54, 67, 69, 89]




```python
###QUICK SORT AS A SINGLE CALLABLE FUNCTION:(BETTER THAN MERGE SORT FOR SMALLER DATASETS)
def quicksort(arr):
    def partition(arr,si,ei):
        pivot=arr[si]###assuming the first element as pivot, move it to the right place in the array
        count=0###for counting the elements smaller than the supposed pivot element
        for i in range (si,ei+1):
            if arr[i]<arr[si]:
                count=count+1
        arr[si+count],arr[si]=arr[si],arr[si+count]
        pivot_index=si+count
        ####now we are going to swap elements around the pivot based on whether they are > or < pivot 
        i=si
        j=ei
        while i<j:
            if arr[i]<pivot:
                i=i+1
            elif arr[j]>pivot:
                j=j-1
            else:
                arr[i],arr[j]=arr[j],arr[i]
                i=i+1
                j=j-1
        return pivot_index
        
                
        
        
    
    def sort(arr,si,ei):###recursive sorting part
        if si>ei:
            return
        pivot=partition(arr,si,ei)
        sort(arr,si,pivot-1)
        sort(arr,pivot+1,ei)
    sort(arr,0,len(arr)-1)
arr=[int(ele) for ele in input("Enter your elements:").split()]
quicksort(arr)
print(arr)
        
        
```

    Enter your elements:12 34 65 99 7 6 5 4 100
    [4, 5, 6, 7, 12, 34, 65, 99, 100]
    


```python
####TOWER OF HANOI!!!!

def tower_hanoi(n,a,b,c):##n IS AN INTEGER WHILE A,B,C ARE TOWERS(source,auxillary,destination)
    if n==1:
        print("move 1st disk from",a,"to",c)
        return
    tower_hanoi(n-1,a,c,b)### A to B using C
    print("move",n,"th disk from",a,"to",c)
    tower_hanoi(n-1,b,a,c)
tower_hanoi(3,"Source","Helper","Destination")
```

    move 1st disk from Source to Destination
    move 2 th disk from Source to Helper
    move 1st disk from Destination to Helper
    move 3 th disk from Source to Destination
    move 1st disk from Helper to Source
    move 2 th disk from Helper to Destination
    move 1st disk from Source to Destination
    


```python
###WAP A RECURSIVE FUNCTION TO COMPUTE SUM OF EVEN AND ODD NUMBERS TILL N
sumeven=0
sumodd=0
def evenodd(n):
    global sumeven
    global sumodd
    if n==0:
        return 0
    else:
        if n%2==0:
            return n +  evenodd(n-1)
        else:
            return n +  evenodd(n-1)
    
evenodd(5)
```




    15




```python
sumeven=0
sum0dd=-0
def evenodd(n):
    global sumeven
    global sumoddb
    if n==0:
        return 0
    else:
        if n%2==0:
            return n + evendod(n)
```


```python
###WAP FOR CALCULATING GEOMETRIC SUM upto 5 decimal places

def geometric_sum(k):
    if k<0:
        return 0
    else:
        sum = geometric_sum(k-1)
        return (1/2**k) + sum 
print(str.format('{0:.5f}',geometric_sum(4)))
    
```

    1.93750
    


```python
def chkpalin(string):
    if len(string)==0:
        return False
    elif len(string)==1:
        return True
    else:
        if string[0]==string[-1]:
            return chkpalin(string[1:-1])
            
        else:
            return False
    
string=input("Enter your string"
if chkpalin(string.lower()):
    print("true")
else:
    print("false")

```

    Enter your stringRace car
    false
    


```python
###multipliation
def multiplication(m,n):
    if n==0:
        return 0
    elif n<0:
        return -m - multiplication(-m,n+1)
    else:
        return m + multiplication(m,n-1)
m=int(input())
n=int(input())
print(multiplication(m,n))
```

    -5
    -3
    15
    


```python
def countzero(n):
    global count
    if n==0:
        return 
    
    else:
        if n%10==0:
            count = count + 1
            countzero(n//10)
        else:
            countzero(n//10)
n=int(input())
count=0
(countzero(n))
print(count)

```


```python
def pairstart(string):
    if len(string)==0 or len(string)==1:
        return string
    else:
        if string[0]==string[1]:
            return string[0]+ "*"+pairstart(string[1:])
        else:
            return string[0]+ pairstart(string[1:])
print(pairstart("hello"))
```

    hel*lo
    


```python
###WAP TO RETURN ALL THE INDEXES OF AN ELEMENTS IN AN ARRAY

def indexele(arr,ele,result,si=0):
    if len(arr)==si:
        return result
    else:
        if arr[si]==ele:
            result = result + [si]
            return indexele(arr,ele,result,si+1)
        
        else:
            return indexele(arr,ele,result,si+1)
arr=[int(ele) for ele in input("enter the elements: ").split()]
ele=int(input("enter the element to find:"))
result=[]
print("These are the indexes",indexele(arr,ele,result))
            
            
            

            
            
            
```

    enter the elements: 23 23 4 5 6 7 23 1 2 3
    enter the element to find:23
    These are the indexes [0, 1, 6]
    


```python

```
