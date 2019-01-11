def stars(m_dict,tv_dict):
    result = {}
    for (key,val) in m_dict.items():
        for i in range(0,len(val)):
            if not val[i] in result:
                result[val[i]] = [key]
            else:
                result[val[i]].append(key)
                result[val[i]].sort()
    for (key,val) in tv_dict.items():                        
        for i in range(0,len(val)):
            if not val[i] in result:
                result[val[i]] = [key]
            else:
                result[val[i]].append(key)
                result[val[i]].sort()
    return result                    


movies = {"How to Be Single": ["Alison Brie", "Dakota Johnson",
                               "Rebel Wilson"],
          "The Lego Movie": ["Will Arnett", "Elizabeth Banks",
                             "Alison Brie", "Will Ferrell"]}
tvshows = {"Community": ["Alison Brie", "Joel McHale",
                         "Danny Pudi", "Yvette Brown",
                         "Donald Glover"],
           "30 Rock": ["Tina Fey", "Tracy Morgan", "Jack McBrayer",
                       "Alec Baldwin", "Elizabeth Banks"],
           "Arrested Development": ["Jason Bateman", "Will Arnett",
                                    "Portia de Rossi"]}
print(stars(movies, tvshows))
