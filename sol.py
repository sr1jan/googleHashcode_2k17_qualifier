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


    # {ep: [[d_latn, c_conn], [(c,diff),..], [(vids,req),...]]}
    end_pts = {}
    for e_pt in range(e_p):
        ep_info = list(map(int, list(input().split())))
        end_pts[e_pt] = [[ep_info[0], ep_info[1]], [], []]
        for c in range(ep_info[1]):
            c_info = list(map(int, list(input().split())))
            end_pts[e_pt][1].append((c_info[0], ep_info[0] - c_info[1]))

    for r in range(r):
        r_info = list(map(int, list(input().split())))
        end_pts[r_info[1]][2].append((r_info[0], r_info[2]))

    # print(f"end_pts: {end_pts}\n")

    v_dict = {}
    for i in range(vids):
        v_dict[i] = []

    c_dict = {}
    for i in range(caches):
        c_dict[i] = []


    # {ep: [d_latn, [cnce_conn]],....}
    # [ [{vid}: [req,...],...], [{cache}: [diff,...],...] ]
    ep_dl_c = {}
    vids_caches = []
    for ep in end_pts:
        ep_dl_c[ep] = [end_pts[ep][0][0],[c[0] for c in end_pts[ep][1]]]

        vids = [v[0] for v in end_pts[ep][2]]
        cache = [c[0] for c in end_pts[ep][1]]

        for v,_ in v_dict.items():
            if v not in vids:
                v_dict[v].append(0)
        for v in end_pts[ep][2]:
            v_dict[v[0]].append(v[1])

        for c,_ in c_dict.items():
            if c not in cache:
                c_dict[c].append(0)
        for c in end_pts[ep][1]:
            c_dict[c[0]].append(c[1])

    vids_caches.append(v_dict)
    vids_caches.append(c_dict)


    cv_prod_comb = {}
    for c in range(caches):
        cv_prod_comb[c] = []

    for c in vids_caches[1]:
        max_prod_list = []
        for v in vids_caches[0]:
            # print(f"{v},{c} ~ {vids_caches[0][v]} | {vids_caches[1][c]}")
            cart_prod = [a*b for a,b in zip(vids_caches[0][v],vids_caches[1][c])]
            max_prod = max(cart_prod)
            max_prod_list.append([v, max_prod])
        max_prod_list = sorted(max_prod_list, key=lambda x: x[1], reverse=True)
        cv_prod_comb[c].append(max_prod_list)

    for comb in cv_prod_comb:
        l = [cc for cc in cv_prod_comb[c][0] if cc[1] is not 0]
        print(comb, *l, sep=' ')
    print()

    for comb in cv_prod_comb:
        # print(comb, cv_prod_comb[comb])
        for v in cv_prod_comb[comb][0]:
            if v[1] is 0: continue
            cur_c_size = cache_vids[comb][1]
            # print(c[0], cur_c_size)
            if vids_size[v[0]] <= cur_c_size:
                cache_vids[comb][0].append(v[0])
                cache_vids[comb][1] = cur_c_size - vids_size[v[0]]


    # print()
    # for c in cache_vids:
    #     # l = [cc for cc in cache_vids[c] if cc is not 0]
    #     print(c, *cache_vids[c], sep=' ')
    # print()


#     c = 0
#     for cv in cache_vids:
#         if len(cache_vids[cv][0]) is not 0: c+=1

#     print(c)
#     for cv in cache_vids:
#         if(len(cache_vids[cv][0])) is not 0:
#             print(cv, *cache_vids[cv][0], sep=" ")


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
    # print("Num_of_videos:",len(vids_size))
    # print("Not connected to any cache:",no_c)



