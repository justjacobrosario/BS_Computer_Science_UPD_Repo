def official_name(school):
    if school == ():
        return ""
    else:
        if (school[0].lower()) in ("of", "in", "the", "for", "ng", "de"):
            return (str(school[0].lower()).strip() + " " + str(official_name(school[1:])).strip()).strip()
        else: 
            return (str(school[0].capitalize()).strip() + " " + str(official_name(school[1:])).strip()).strip()

print(official_name(("uNiVerSITy", "OF", "THe", "PHILIPPINES")))

# in returning a recursed string, return str(change case[n]) + str(function(param[n+1:]))