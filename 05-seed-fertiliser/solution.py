from pyprojroot import here

with open(here("05-seed-fertiliser/input.txt"), "r") as f:
    txt = f.read()
    f.close()
txt = txt.rsplit("\n\n")
seeds = txt.pop(0)
seeds = seeds.split(": ")[-1].split(" ")
seeds = [int(s) for s in seeds]
# seeds = {"seeds:_": seeds}

# make a dict containing all the maps
mapmap = {}
for i in txt:
    maplines = i.splitlines()
    source, destination = maplines.pop(0).replace(":", "").replace(" map", "").split("-to-")
    mapkey = f"{source}:{destination}"
    print(maplines)
    mapnums = []
    for j in maplines:
        nums = j.split(" ")
        nums = [int(n) for n in nums]
        mapnums.append(nums)
    mapmap[mapkey] = mapnums


def find_seed_location(seed:int, source_pat:str="seed", maps:dict=mapmap):
    source_val = seed
    while source_pat != "location":
        print(f"Seed is {seed} Key is {source_pat}")
        dest_key = [k for k in maps.keys() if k.startswith(source_pat)][0]
        dest_map = maps[dest_key]
        source_pat = dest_key.split(":")[-1]
        print(f"Next source pat will be {source_pat}")
        for m in dest_map:
            if (source_val >= m[1]) and (source_val < (m[1] + m[-1])):
                diff = source_val - m[1]
                print(f"source diff is {diff}")
                # print(source_ind)
                # find the destination
                source_val = m[0] + diff
                print(f"destination starts at {m[0]} is {source_val}")
            else:
                source_val = source_val

    print(f"Dest is {source_val}")
    return source_val


locations = []
for s in seeds[0:1]:
    locations.append(find_seed_location(s))
    
   
min(locations)
# 2393304 too low
# 260682763 too high
len(seeds)
len(locations)