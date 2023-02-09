#2306. Naming a Company
def distinctNames(self, ideas: list[str]) -> int:
    count = 0
    done = []
    elle = [0]
    ideas.sort()
    for x in range(0,len(ideas)-1):
        if ideas[x][0] == ideas[x+1][0]:
            continue
        else:
            elle.append(x+1)
    print(elle)
"""    for x in range(len(ideas)-1):
        A = ideas[x]
        for y in range(x+1,len(ideas)):
            B = ideas[y]
            if [B,A] not in done :
                done.append([B[0]+A[1:],A[0]+B[1:]])
                if B[0]+A[1:] not in ideas and A[0]+B[1:] not in ideas:
                    count+= 2
    
    return count"""
"""    for x in range(0,len(done)):
        print(done[x])
        if done[x][0][0] != done[x][1][0]:
            a = done[x][1][0] + done[x][0][1:]
            b = done[x][0][0] + done[x][1][1:]
            print(a,b)
            if a not in ideas and b not in ideas:
                count += 2"""

"""    for i in range(int(len(ideas)/2)):
        ideaA = ideas[i]
        for ideaB in ideas[:i]+ideas[i+1:]:
            if [ideaA,ideaB] not in done:

                done.append([ideaA,ideaB]) 
                done.append([ideaB,ideaA])              
                print(done,ideaA,ideaB)
                tempA,tempB = ideaA,ideaB
                ideaA = tempB[0]+tempA[1:]
                ideaB = tempA[0]+tempB[1:]
                if ideaA not in ideas and ideaB not in ideas:
                    #print(ideaA," ",ideaB,"\t",ideas)
                    count += 2
                ideaA = tempA
                ideaB = tempB
            else:
                continue
    return count            """


print(distinctNames(0,ideas =
["fvqb","oqndiu","ttghzij","irm","nrc","plomcni","zjo","vysdzh","igy","bfbyfa","em","e","pfttjusc","odt","zkysf","danjbtmjyl","ehg","dn","xngj","sfcydheiqt","xyvslexmr","ywwjx","ckqfsii","wyxqjt","mvejfhiz","op","z","yqoosorx","umiluthxd","fixwlji","b","vrmxbjfp","tvur","tewdv","rxliykudu","hkcqlwcq","eiovjeopqe","wkbsfi","kw","wjljn","puwpmoidt","mcbavifub","dyvslexmr","wriwkqigda","qkroyqarx","galvb","xooltbvp","oewdv","ax","lfculsdkda","fdxaie","obsrty","jxvdrg","inxxbns","xxguo","wx","qicjqvq","nzodxzjj","pqxszwuvlq","ae","ialky","jxr","wzl","wrurv","mype","orvn","hanjbtmjyl","ddjdoftoxn","snaulwlrc","aafiemzaj","ymfgxmwftm","jamxqcyn","ogy","ekpl","bychyapv","t","tvybuin","mgy","skuaf","nq","ja","m","y","cxguo","lukx","fciqkqmij","wqoxhbn","xxfb","dqtuajlx","fcbyafyhi","lbcpe","eqipqzyac","mvshgnwi","fvtjyxuvz","prurv","pyjb","xpfd","kyz","aa","yrukkw","mcigoojfd","ccia","slwbxzajt","j","npab","sy","ugpwgoo","wgl","idxaie","csx","jyrlf","bxfb","mbtsljr","ppwczwpu","gaqgdd","epva","hibynv","vlzzh","bvppn","udzjwic","zjybfv","wwxf","zyzwpzcv","nzfdmj","r","jcxaiydhwp","mcvohzwi","s","jncrvhl","du","vqkfarj","rrurv","vow","ireit","fqsuvfxfay","puuzpvoj","vkpn","wjiynyf","bzqyfu","kbjfou","p","fp","hb","bclozexya","tbbqcauyd","pp","uy","mqdohmppo","zyonao","ukroyqarx","plt","jviyprjfe","tz","js","qmqbqmz","h","onl","ouo","yfdrthn","kyyhslfg","tigs","okslsuii","gmydwcuz","ourt","jzg","tjoimpag","x","fsjhziy","wukpgjclj","dmewbxwjlr","rrgjwsrxo","ouel","oenv","yufesmid","xpwzyprxzn","rirvusfaub","nakwxmj","qyis","vt","zvtnc","yzxglaftxd","hdlqlcbo","bng","trfess","awavw","qofnofb","unl","ofpi","ytygtikhi","mtwr","fcuvmp","xvyxo","mlgian","kjzjvqfaiq","wevumst","drzd","pltxktqvwo","pygnebefr","vyephecebc","bc","opcq","qeupxg","cfcshjwmj","xbxs","nioaprb","duavxqm","wiehmba","tmgmt","nwysfweld","upx","douuqzyue","olvekc","ygt","ava","qemcmwypcp","ezbdfequky","sslb","durt","sbvma","kupyp","sggmtds","sbigv","thq","kfdsp","qkl","pumymdyji","oglk","pybqyy","zb","okjrquxq","st","vzivbpyv","yljvfzkxhg","hujrsbsj","zett","xpsixu","vawazfio","yfbpasz","aee","phvnzizbmv","shsvqrf","foxbhwo","coyp","eq","qlxihgaf","aunmipq","ujdufzwt","uyfwzhv","siwszzl","nxsgfvtio","nxu","jvubudi","nly","xwxf","vmytdlqavs","kbbqcauyd","sme","fyvslexmr","sefbq","yruzwzspg","fkltcrvrm","w","ezoftqvy","hkb","jgy","hbbqcauyd","npdfusd","txuuhbm","xtya","g","beupxg","jyiruuch","nxymnknoft","gohh","cc","qilzrc","vgtwff","fbtxpen","gypldt","reupxg","qjljn","zfxjr","nc","iruvnagxl","bzs","hqxszwuvlq","orhprwxg","hc","rjnzakx","fapbt","bqpkbetdds","wty","wso","risasrmn","gd","lrm","tgsdzrs","cmbbuhutny","jwleqws","kavxalu","mgokvqwkm","wzfdrmgj","eglk","nloaopfuk","yhsbofcj","egthd","yr","vattjzfvzk","vroyt","ttjusn","f","foyx","yurufcrzkt","aohiuhzidk","pv","ny","q","froalon","lihuhpofr","oudq","qmovtrqpl","vloaopfuk","spy","cescee","synzqz","vso","bxhdw","lifrssig","gnidvnyk","uj","shlwhgmq","ootcoroo","gi","ksbjfwcaa","xmvutn","pckqlkhr","cz","qvlwgtaxd","igarb","xibtlut","aciov","zo","mgjfjgpckg","uk","mkysf","mlscaai","v","ejli","bvubudi","uiauj","apdu","zzyhg","pxbuoa","dzpn","aucwnffap","zsaaa","qqpcizi","aolpxrtxsa","xgthd","tgzys","uruyybxycc","cgt","nbtimwpr","ivkagsuhat","xiehmba","jcig","dydkwbzdxp","miwgdotedc","qj","rp","xwkuaiyg","iplrvgsl","nica","tsxcujiswe","omkwadli","sgjfjgpckg","pcxaiydhwp","cypeugaelx","ahxdksgb","wk","mn","qtya","nhkbo","zxpdrhj","bkzlovs","lxzgeb","o","ifmivwgpg","wrevyqdvq","akpdmw","c","odfmsmxt","esvjqnvce","kj","jwwjwjv","fvqvykd","ntmphpw","rcigoojfd","kn","hutn","fw","rov","adnvx","sdhs","pdykro","csndx","uhshsdgx","sslwjktw","mfeom","xdt","kpgnfrtb","ua","pjtjzhhm","plnmynnwj","ggsxhvs","frflap","wnaeia","aopxqsf","ukpl","uycc","ogimybnqli","fggj","boqrjlol","gwfpurs","jcwaz","qszalypvd","sqkyknakxj","lv","im","fhmrtyqb","dikuqlutna","aawukhwvdf","lvm","hqaxh","cmwuqzw","xtjoep","xiex","gn","deuqwb","vhenxxfkm","cvbvbjtfyc","ruepw","aclb","efp","oysdzh","zcejfnp","qxpbnqz","crwy","uky","qlfohmbpx","cj","me","gjiqte","nmxkjyjj","ck","d","qurufcrzkt","ou","sgl","lmkwadli","dtygtikhi","pkroyqarx","zxd","sc","aegjivv","oteb","ss","zrm","sbzzrzg","ilwtpfbr","aroyt","kltozago","qjcvosyxf","hhxdksgb","oljsfsgpf","fogjwait","myrlf","unr","zdkkckknq","nfpi","sdnwie","hycymt","vdpqoi","stnmuotsv","jpwczwpu","fx","oggyuyhfz","faorr","ef","sq","l","i","ieuadqc","sabjmdup","rppncdqoqb","qvfzm","dyyhslfg","atjoep","wkcgc","fgpbjq","mrl","sjiynyf","aluo","mooshwn","hvbvbjtfyc","mh","sgbbwr","cczofbbkm","yeafjsyyz","jn","vsopod","rgzq","cfzijk","qky","ahrqfcybib","loqrjlol","lfwkqj","etqmtg","vakwxmj","iggmtds","raispgodf","ampsjl","buzcycl","xvppn","qh","fkwfzya","yamxqcyn","uofczmpjd","hclfaxtrl","jkxs","yocgia","tql","lgv","oamnrc","ujavqmg","yqq","xdbzsea","ayms","fupyp","yuj","ieswz","om","ljaofjdn","hrgqefb","qag","jhfxunisp","byddbstas","utdkxpglrt","ov","jfzmqvy","mpx","gxi","uiwgdotedc","oxspcg","bwa","lu","outbbdg","hybqyy","hqr","kaxcl","u","qgfqqchcv","uyyhslfg","bfzijk","ssy","iprktpszev","tci","lvwrtrlfcj","hrtqhczl","aab","xa","mazhx","rawazfio","prvsjt","wdvjqeqdu","ijavqmg","vmcbiiit","onmhvkws","cuw","btqbdof","jz","qpy","qoxdp","zkpl","shb","hntieibjd","keb","otsyoqpcuo","utmljd","vwrx","vmewbxwjlr","cf","xnrwxk","bvejfhiz","gjmo","sofczmpjd","tevkykk","bpdfusd","luopl","hd","tqhvp","fpyw","tzdkmejcps","xwa","frezghj","fymscu","tugddjcs","ggevgie","fmubimr","zptj","tlfohmbpx","aogngdppq","urxlyrtut","elgian","ex","wthjlnlbwd","tqxszwuvlq","todaqfv","k","yewdv","fgayiukjvs","drkeo","ywi","jynzqz","sxeuz","wawazfio","pmreu","pdvsz","itwoo","sljvfzkxhg","ra","lxmrvbpgn","qiwszzl","optqzwdb","oc","awbmydp","pewdv","pnvmi","gh","sgubgo","pfp","tawo","cdizggq","mgwtpngic","idczqemz","nhmrtyqb","hbwbei","tjaa","tkr","ildywyd","xychyapv","obwbei","zv","ogf","nrrp","sxzstans","nmzkgw","xaqyzvjjuq","sbr","jdnwie","gafjqclqu","pmlurwufma","xk","hkspomrhke","popqxw","yudq","hj","ivyq","hso","dty","qyna","ingyemtn","gmasdnksuj","qa","evklv","n","wrkne","sntid","wbziyok","ylrlre","cewspqfe","pkpl","zgoh","posho","iuve","a","bbzc","rtjoep","fr","thhh","htzzk","kutgzyvufb","orfaiovol","umgk","tuwsdk","am","ucig","scs","wicd","muusykbnow","sw","hhrqfcybib","anzgyqrjr","afxueqt","wxnkprjnq","ikcg","ftztcrtkf","xicwu","mdvqs","wuudst","dmx","wng","va","olzp","vuzdqfooj","okdygrsg","hu","wbpdrvgv","jgzys","xdywfpzrr","mnosxa","zsgibplul","guxgxx","hwpnbwx","dmij","seqawkip","mesnjvuhye","qbbygu","qugzakr","kgphkd","ogpqje","zxzgeb","kol","ezqnj","bcxaiydhwp","cymtmcquu","ftliq","dbbepji","vjwwa","kp","cfv","sszwb","nqv","xag","ipbnb","jd","zpij","buvndst","pyhdemphn","hkr","mjykssurlq","qwv","rpwhxhg","ygx","srtqhczl","gfllvgwkmp","seekexbhxd","xxy","dwyuc","ddhs","lyumvdg","td","fxiwibgpy","wjmd","quoh","iakmh","nvkagsuhat","jafjltf","airvusfaub","xwer","tbaax","qwwjx","jffjzdl","dupynps","dljsfsgpf","zriwkqigda","qyvslexmr","qrgjwsrxo","tlhz","pjzbzaje","zseazyhb","qjppyjx","iwavw","zbqqlbatfe","lsdvljgwhi","xbodzhp","av","iavxalu","snftktc","kjiynyf","if","ldinajckh","dwixy","qsevzixa","bbvma","vdxaie","qqxxno","hpij","shkww","eljvfzkxhg","ndpojstyk","lnwdlhe","rz","lyrgtmser","udjdoftoxn","yablcwle","qjxj","ywfcaj","hdaidhghb","ccbpywmsp","wnovgytcm","gubaxiity","mafj","wje","gtykd","uqwkere","ahroi","hwapxaa","mgthd","zeuadqc","xhzygtsalj","dazu","hkpn","kzwutcto","ro","linynwupm","vmzttlazxs","dkbykvcyxo","tpepwtisr","qxfawz","lzjjqpfcr","ap","foyxdcmgqf","kynttrc","cazhx","mojl","bpyxp","wnhdi","qo","ciwq","jpwhxhg"]))