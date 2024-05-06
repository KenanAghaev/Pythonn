#1-ci kok olan ededler
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]

# def kok(x):
#     if x<1:
#         return
#     elif x**0.5==round(x**0.5,2):
#         return x
    
# newlist=[kok(i) for i in mylist if kok(i)!=None]
# print(newlist)

# 2-ci tekrarlanmayan element

# def tam_list(lst):
#     u_lst = []
#     for item in lst:
#         if lst.count(item) == 1:
#             u_lst.append(item)
#     return u_lst

# my_list = [-1, 1, 2, 2, 6, 7, 7, 'say']
# netice_list = tam_list(my_list)
# print(netice_list)

#3-cu hasil
# ededler=input("ededleri vergulle ayirin:")
# mylist=ededler.split(',')
# def h(x):
#     hasil=1
#     for eded in x:
#         hasil*=int(eded)
#     return hasil

# print(h(mylist))

#4-cu bolenler

# eded=int(input("eded daxil edin:"))
# bolenleri = [x for x in range(1,eded+1) if eded % x ==0]
# print(bolenleri)

#5-ci aylar
# mylist=['yanvar','fevral','mart','aprel','may','iyun','iyul','avqust','sentyabr','oktyabr','noyabr','dekabr']
# def dictionary(aylar):
#     return[(ay,len(ay)) for ay in aylar]

# result=dictionary(mylist)
# print(result)

#6-ci adlar
# def ad(lst):
#     return[ad.split()[0].lower() for ad in lst]

# lst=["Kenan Aghaev","Emin Alekber","Pusta Zeynal","Lyaman Mammad"]
# adlar=ad(lst)
# print(adlar)

#7-ci index ortalama

# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]

# list3=[]


# for i in range(len(list1)):
#     a=(list1[i]+list2[i])/2
#     list3.append(a)

# print(list3)    