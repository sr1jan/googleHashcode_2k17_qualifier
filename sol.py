if __name__ ==  '__main__':
    data = list(map(int, list(input().split())))
    vids, e_p, r, caches, c_size = data[0], data[1], data[2], data[3], data[4]

    vids_size = list(map(int, list(input().split())))

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


    # printing end_point, number of server connected
    # dict[key_value][list_index][sub_list_index]
    for ep in end_pts:
        print(f"{ep}, {end_pts[ep][0][1]}")

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



