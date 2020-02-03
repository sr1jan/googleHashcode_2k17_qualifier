def vids_to_cache(ep_info, vids_size, cache_vids, c_size):
    caches = sorted(ep_info[1], key=lambda x: x[1])
    vids_req = sorted(ep_info[2], key=lambda x: x[1], reverse=True)

    for vid in vids_req:
        vid_size = vids_size[vid[0]]
        if vid_size > c_size:
            continue

        for c in caches:
            remain_csize = cache_vids[c[0]][1]
            if vid_size > remain_csize: continue

            cache_vids[c[0]][0].append(vid[0])
            cache_vids[c[0]][1] = remain_csize - vid_size
            # print(cache_vids)
            break

    # print(cache_vids)
    return cache_vids



if __name__ ==  '__main__':
    data = list(map(int, list(input().split())))
    vids, e_p, r, caches, c_size = data[0], data[1], data[2], data[3], data[4]

    # size of each video
    vids_size = list(map(int, list(input().split())))

    # cache -> [ [vids], remaining cache size ]
    global cache_vids
    cache_vids = {}
    for c in range(caches):
        cache_vids[c] = [[], c_size]


    # {ep: [ [data_latn, svr_conn], [(cache, latn),...], [(vid, num_of_req),....] ]}
    end_pts = {}
    for e_pt in range(e_p):
        ep_info = list(map(int, list(input().split())))
        end_pts[e_pt] = [[ep_info[0], ep_info[1]], [], []]
        for c in range(ep_info[1]):
            latn = list(map(int, list(input().split())))
            end_pts[e_pt][1].append((latn[0], latn[1]))

    req = {}
    for r in range(r):
        r_info = list(map(int, list(input().split())))
        end_pts[r_info[1]][2].append((r_info[0], r_info[2]))

    # for ep in end_pts:
    #     print(f"{ep} ~ {end_pts[ep]}")

    for ep in end_pts:
        # print(f"{ep}:")
        vids_to_cache(end_pts[ep], vids_size, cache_vids, c_size)
        # for cv in cache_vids:
        #     print(cv, *cache_vids[cv], sep=", ")
        # print()


    c = 0
    for cv in cache_vids:
        if len(cache_vids[cv][0]) is not 0: c+=1

    print(c)
    for cv in cache_vids:
        print(cv, *cache_vids[cv][0], sep=" ")



    # no_c = [0,[]]
    # for ep in end_pts:
    #     if end_pts[ep][0][1] is 0:
    #         no_c[0] += 1
    #         no_c[1].append(ep)

    #     if len(end_pts[ep][1]) is not 0:
    #         c_lats = [i[1] for i in end_pts[ep][1]]
    #         cmin = min(c_lats)
    #         cmax = max(c_lats)
    #         if cmax > end_pts[ep][0][0]:
    #             print(f"{ep} ~ dc_lat:{end_pts[ep][0]}, cmin_lat:{cmin}, cmax_lat:{cmax}")

    # print("Num_of_endPts:",len(end_pts))
    # print("Num_of_caches:",caches)
    # print("Not connected to any cache:",no_c)



