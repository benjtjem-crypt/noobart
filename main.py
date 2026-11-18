min_sekk = ["white house","eifel tower",] 

def tell(tingene):
    antall_ting = len(tingene)
    print(f"Du har {antall_ting} ting i sekken")
    
def legg_i(sekken, ny_ting):
    sekken.append(ny_ting)
    print(f"Du la {ny_ting} i sekken!")

def print_sekk(sekken):
    for ting in sekken:
        print(ting)
    
tell(min_sekk)
legg_i(min_sekk, "gorilla")

tell(min_sekk)
print_sekk(min_sekk)

