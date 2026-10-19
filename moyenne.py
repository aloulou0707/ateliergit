def moyennes(notes):
    return sum(notes)/len(notes)
def notemax(notes):
    return max(notes)
notes =[12,15,9,18]
print("Moyenne ",moyennes(notes))
print("note maximale ",notemax(notes))
def mediane(notes):
    tri=sorted(notes)
    n=len(tri)
    return tri[n//2]
print("mediane ",mediane(notes))

