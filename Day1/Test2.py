# //    bangalore is capital of Karnataka
# //
# //    Op1 - Bangalore Is Capital Of Karnataka
# //
# //    Op2 - Berolagna Is Clatipa Of Kakatanra


def revCap(s):
    list_s= s.split(" ")
    s_new=""
    # print(list_s)
    for i in list_s:
        if i.__contains__("is") or  i.__contains__("of"):
            s_new=s_new+" "+str.title(i)
        else:
            x=str.title(i)
            l=len(i)
            s_new=s_new+" "+str.title(i[0])+x[l:0:-1]
            print(s_new)







s="bangalore is capital of Karnataka"
revCap(s)