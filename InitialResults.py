import matplotlib.pyplot as plt
import matplotlib as mpl

blockData = "[13379 52],[21392 61],[10462 98],[18227 103],[12240 103],[22290 131],[11283 331],[22237 143],[11225 203],[7228 210],[16214 264],[11236 196],[23223 313],[22443 356],[10283 336],[10473 340],[10427 317],[23390 497],[46284 408],[10245 459],[21276 382],[11224 496],[13229 371],[10316 442],[11218 479],[20252 491],[22442 394],[11261 452],[34260 595],[21477 549],[4285 675],[20399 588],[18418 677],[21649 1217],[18306 644],[10443 693],[8419 725],[11305 1071],[8556 663],[36315 807],[5300 625],[21376 686],[11486 1004],[7622 1032],[8517 820],[9314 845],[9501 1229],[8505 902],[19619 894],[34276 825],[22274 847],[25302 1104],[19698 1426],[6392 864],[22325 1019],[21656 3126],[13372 1737],[12495 1838],[8213 1008],[14232 1179],[18217 1098],[10307 1280],[22230 1185],[8332 1032],[10660 1218],[8405 1260],[21243 1233],[21285 1215],[22439 1220],[9143 1253],[22239 1280],[8377 1810],[8291 1443],[8312 1894],[16544 1271],[33537 1429],[8776 1980],[21597 2893],[14521 1561],[19530 1609],[9273 1935],[18297 1602],[6342 2535],[10247 1563],[11057 1654],[13738 4416],[12438 3732],[22491 1878], [22233 2020], [7322 2572], [21231 1702], [41227 1993], [17895 2390], [11715 3508], [21232 1895], [12941 3696], [8608 3268], [30244 2038], [10467 2341], [21336 2052]"
tradData = "[21 7],[9 9],[11 8],[8 7],[8 7],[10 8],[10 7],[11 7],[10 8],[10 8],[10 7],[9 7],[12 7],[9 7],[9 5],[8 7],[9 8],[9 9],[10 7],[9 7],[8 7],[10 8],[9 7],[10 6],[9 6],[12 10],[9 8],[7 8],[9 9],[9 7],[9 9],[8 6],[12 7],[11 5],[9 22],[7 9],[8 7],[9 8],[10 7],[8 7],[8 6],[8 8],[9 8],[10 7],[9 9],[8 7],[9 7],[9 8],[12 6],[9 8],[9 9],[14 5],[8 12],[9 7],[9 8],[10 8],[8 9],[10 7],[9 6],[12 6],[6 6],[9 8],[9 7],[7 6],[10 7],[9 8],[8 8],[9 8],[8 8],[8 8],[7 9],[11 7],[9 9],[9 9],[13 6],[9 13],[9 8],[8 7],[12 7],[9 8],[8 9],[9 9],[9 8],[9 8],[9 8],[9 8],[11 7],[9 8],[8 7],[9 9],[8 8],[9 8],[9 8],[8 9],[10 7],[7 7],[10 7],[11 7],[11 9],[8 8]"
blockConcurrent = "[14261 59],[9251 62],[6611 62],[10240 63],[10362 59],[24249 56],[7291 62],[11246 54],[9271 59],[24391 274],[5285 72],[4298 155],[12293 153],[23911 1088],[20566 1372],[18552 323],[14035 1240],[14432 768],[15318 324],[60315 189],[10258 239],[10846 850],[10783 613],[13129 713],[14128 407],[15695 1107],[16403 283],[6566 267],[7611 177],[8409 131],[14613 537],[4141 701],[5159 1212],[5414 538],[6438 817],[7492 335],[10843 1498],[11187 980],[11663 900],[12281 216],[6257 393],[21580 274],[22573 580],[23263 250],[24671 1179],[13552 228],[15278 212],[16305 452],[17299 629],[18549 624],[12256 327],[9716 284],[11646 584],[4176 263],[12508 242],[14700 547],[7990 134],[12058 274],[10469 989],[11402 186],[8458 194],[3791 1164],[4986 1557],[5256 289],[6262 454],[7688 532],[10487 1316],[10893 1854],[1803 536],[12797 863],[9264 228],[13671 232],[14376 211],[16542 194],[17498 440],[18420 797],[8364 142],[9425 265],[10365 441],[12070 664],[1276 450],[22283 237],[23509 245],[8280 206],[9363 236],[10571 570],[11561 354],[12422 1017],[14646 426],[13334 47],[9840 1392],[15262 381],[17083 305],[17259 701],[6454 860],[7685 748],[8260 163],[9389 537],[10440 357],[11521 640],[4265 274],[10455 1041],[11366 1917],[12500 333],[13380 2214],[16637 838],[15416 1580],[18630 464],[19442 1107],[17315 250]"
tradConcurrent = "[19 24],[10 7],[13 7],[11 6],[9 6],[8 11],[15 5],[13 6],[8 11],[9 10],[14 21],[18 23],[27 11],[27 11],[22 9],[13 27],[23 12],[20 9],[22 18],[78 24],[13 10],[10 10],[10 13],[12 11],[13 8],[11 27],[11 11],[24 9],[15 10],[29 8],[17 13],[18 12],[66 33],[12 8],[14 10],[20 8],[31 25],[13 8],[14 9],[43 8],[23 9],[9 7],[11 7],[16 10],[11 6],[10 7],[13 8],[16 12],[9 7],[28 8],[8 7],[15 13],[11 9],[16 10],[11 13],[24 19],[12 10],[21 6],[22 11],[28 7],[13 12],[22 9],[16 15],[15 10],[17 10],[22 8],[23 10],[20 12],[11 7],[31 10],[11 7],[10 6],[15 15],[13 9],[10 13],[11 7],[11 7],[10 7],[11 9],[32 6],[11 14],[15 7],[13 17],[19 12],[23 41],[20 9],[27 19],[9 7],[12 17],[31 9],[11 7],[42 28],[11 8],[12 11],[11 9],[10 7],[12 8],[9 14],[13 10],[43 8],[15 7],[23 15],[33 60],[17 10],[14 22],[23 14],[39 20],[16 11],[6 6],[13 12]"

## function to preprocess data
def Process(dataString, l):
    dataString = dataString.split(",")
    print(len(dataString))
    data2 = []
    for data in dataString:
        data = data.split()
        data2.append(data)

    data3 = []

    for data in data2:
        item = []
        for x in data:
            x = x.replace("[","")
            x = x.replace("]","")
            item.append(x)
        data3.append(item)
        

    postTimes = []
    queryTimes = []

    for d in data3:
        postTimes.append(d[0])
        queryTimes.append(d[1])

    def divide_chunks(l, n):
        # looping till length l
        for i in range(0, len(l), n):
            yield l[i:i + n]

    postTimes = [int(x) for x in postTimes]
    queryTimes = [int(x) for x in queryTimes]


    postTimesChunked = list(divide_chunks(postTimes, l))
    queryTimesChunked = list(divide_chunks(queryTimes, l))

    return postTimesChunked, queryTimesChunked


# preprocess data
blockPosts, blockQueries = Process(blockData,20)
tradPosts, tradQueries = Process(tradData,20)


blockConcurrentPosts, blockConcurrentQueries = Process(blockConcurrent, 10)
tradConcurrentPosts, tradConcurrentQueries = Process(tradConcurrent, 10)


# Plot
fig = plt.figure(figsize =(8, 8))

ax = fig.add_subplot(223)
flierprops = dict(marker='o', markerfacecolor='k', markersize=2,linestyle='none', markeredgecolor='k')
bp = ax.boxplot(blockConcurrentPosts, flierprops = flierprops)
ax.set_title('Block Post Times (Concurrent)')
ax.set_xlabel('Run #')
ax.set_ylabel('Time (ms)')
# make log scale
ax.set_yscale('log')
ax.set_yticks([1,10, 100, 1000,10000, 100000])
ax.set_xticklabels([0,1,2,3,4,5,6,7,8,9,10])
ax.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

ax = fig.add_subplot(224)
flierprops = dict(marker='o', markerfacecolor='k', markersize=2,linestyle='none', markeredgecolor='k')
bp = ax.boxplot(blockConcurrentQueries, flierprops = flierprops)
ax.set_title('Block Query Times (Concurrent)')
ax.set_xlabel('Run #')
ax.set_ylabel('Time (ms)')
# make log scale
ax.set_yscale('log')
ax.set_yticks([1,10, 100, 1000,10000, 100000])
ax.set_xticklabels([0,1,2,3,4,5,6,7,8,9,10])
ax.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

ax = fig.add_subplot(221)
flierprops = dict(marker='o', markerfacecolor='k', markersize=2,linestyle='none', markeredgecolor='k')
bp = ax.boxplot(tradConcurrentPosts, flierprops = flierprops)
ax.set_title('Traditional Post Times (Concurrent)')
ax.set_xlabel('Run #')
ax.set_ylabel('Time (ms)')
# make log scale
ax.set_yscale('log')
ax.set_yticks([1,10, 100, 1000,10000, 100000])
ax.set_xticklabels([0,1,2,3,4,5,6,7,8,9,10])
ax.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

ax = fig.add_subplot(222)
flierprops = dict(marker='o', markerfacecolor='k', markersize=2,linestyle='none', markeredgecolor='k')
bp = ax.boxplot(tradConcurrentQueries, flierprops = flierprops)
ax.set_title('Traditional Query Times (Concurrent)')
ax.set_xlabel('Run #')
ax.set_ylabel('Time (ms)')
# make log scale
ax.set_yscale('log')
ax.set_yticks([1,10, 100, 1000,10000, 100000])
ax.set_xticklabels([0,1,2,3,4,5,6,7,8,9,10])
ax.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())
# plot 1
# ax = fig.add_subplot(221)
# flierprops = dict(marker='o', markerfacecolor='k', markersize=2,linestyle='none', markeredgecolor='k')
# bp = ax.boxplot(tradPosts, flierprops = flierprops)
# ax.set_title('Traditional Post Times')
# ax.set_xlabel('Number of Posts')
# ax.set_ylabel('Time (ms)')
# # make log scale
# ax.set_yscale('log')
# ax.set_yticks([1,10, 100, 1000,10000, 100000])
# ax.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

# # plot 2
# ax = fig.add_subplot(222)
# flierprops = dict(marker='o', markerfacecolor='k', markersize=2,linestyle='none', markeredgecolor='k')
# bp = ax.boxplot(tradQueries, flierprops = flierprops)
# ax.set_title('Traditional Query Times')
# ax.set_xlabel('Number of Posts')
# ax.set_ylabel('Time (ms)')
# # make log scale
# ax.set_yscale('log')
# ax.set_yticks([1,10, 100, 1000,10000, 100000])
# ax.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

# # plot 3
# ax = fig.add_subplot(223)
# flierprops = dict(marker='o', markerfacecolor='k', markersize=2,linestyle='none', markeredgecolor='k')
# bp = ax.boxplot(blockPosts,flierprops = flierprops)
# ax.set_title('Blockchain Post Times')
# ax.set_xlabel('Number of Posts')
# ax.set_ylabel('Time (ms)')
# # make log scale
# ax.set_yscale('log')
# ax.set_yticks([1,10, 100, 1000,10000, 100000])
# ax.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

# # plot 4
# ax = fig.add_subplot(224)
# flierprops = dict(marker='o', markerfacecolor='k', markersize=2,linestyle='none', markeredgecolor='k')
# bp = ax.boxplot(blockQueries,flierprops = flierprops)
# ax.set_title('Blockchain Query Times')
# ax.set_xlabel('Number of Posts')
# ax.set_ylabel('Time (ms)')
# # make log scale
# ax.set_yscale('log')
# ax.set_yticks([1,10, 100, 1000,10000,100000])
# ax.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())


# plot all
fig.tight_layout(pad=1.0)
plt.xticks([1,2,3,4,5,6,7,8,9,10,11], [0,1,2,3,4,5,6,7,8,9,10])
plt.show()