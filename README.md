# LeetCode
LeetCode刷题记录

2022/7/7
今天下午遇到的题都比较简单，就有一个稍微难一点点。有两个是链表的题目。一是合并链表，将两个链表放在一起比较，小的就放入新链上，再来两个while循环，但是只有一个能执行，执行的那一个链表直接全部接到新链上就行了。而是判断链表是否有环。其实只需要一个快慢指针就行了。一起考研的时候一直有点没看懂，当时没看懂是我想复杂了，因为链表环总是在最后，是不可能在环后面有环的。第三个是滑动窗口+哈希表问题，要抓住题目关键就是滑动窗口是一样大这个条件，第四个是广度搜索优先。这几个题都不难，但是可能对leetcode和python有点不熟悉，导致最后提交代码时总是多多少少会有一点点错误，这些都是需要加强的地方。

2022/7/8
今天下午遇到的都是图的问题，全部都是关于图的遍历，虽然题目看起来很高大上其实都是纸老虎。图的问题好像并没有太注重时间复杂度，大部分题一提交就过了，只不过没有怎么用过深度遍历都是广度遍历，下次遇到图的问题用深度遍历写，加强一下深度遍历的理解。

2022/7/9
明天妹妹就回家了，成绩实在是太差了，七科得了4个D我真的服。今天做了两个多源广度优先搜索的问题，这个算广度搜索的一个变种，两个题都是属于同一个类型，一开始拿着都不太会做但是看了一个题的题解以后就发了他们的相同之处了，第二个题也是有惊无险的做了出来，虽然说还有两个全0的测试用例没有通过但是我直接if grid==[[0]] or grid==[[0,0,0,0]] return 0就过了，虽然有点耍赖嫌疑。

2022/7/11
昨天有点忙没有刷到题，今天做了3个有关于回溯的题目，一个是组合，一个是全排列，还有一个是字符串字母所有不同的组合。这三个题目都是递归的寻找，先要寻找递归的终止条件，即按照题目要求，一个一个的寻找符合条件的答案，在符合条件的答案中，长度和题目要求的长度相同之后加入到返回的集合当中，二是确定单层的搜索循环，单层的搜索循环如果成功实现，题目也就迎刃而解了。最后，关于找出所有不同的组合，可以用二进制枚举。今天刷题收获满满。

2022/7/12
今天的每日一题是三个动态规划题目，分别是爬梯子、打家劫舍和最小三角形路径和，后面两个比较难的我都会做但是第一个竟然有点点不太会，动态规划的主要问题在于抽象出方程，但是很多时候我都没法抽象出来，这次能做出来的原因主要是因为以前做过可能，希望能在动态规划上能更深入一些因为听说大厂面试动态规划的题目比较多。

2022/7/13
今天遇到两个关于二进制位运算的题目，两个完全不会做，一个是因为以前没有接触过，第二个就是不知道Python怎么进行位运算，都看了一下题解，好在是理解了如何进行二进制数1的循环检查和一些其他二进制问题的知识，二进制问题的特征比较明显，就是一般都是与2有关，不过好像这个是一句废话，继续加油吧。

2022/7/14
今天也是位运算题目，关于位运算的题目可以说是一通百通，可惜我没用桶。一个是只出现一次的数，给了一个数组，找出里面只出现过一次的数，不申请额外的存储空间，可以用异或运算，因为异或运算下来的结果只会是出现了一次的数，异或运算满足交换律，相同的数异或又是0，0与任何数异或都是任何数，所以直接异或就完事。第二个是将二进制数逆序，可以遍历二进制数，先用Res（函数的返回值）为0.用1和n与运算，得到的数字向左位移31-index个位置，这样就把1送到了Res的第一个位置，然后n右移1位，继续这样，直到完成循环。这些算法都不知道这些人怎么想出来的，已经感觉到智商被碾压了。

2022/7/15
今天遇到的题全都是二分查找的变种，虽然我也是用的二分查找但是我总感觉我的路子有点野，而且代码很垃圾，虽然全都通过了但是总感觉很奇怪。妹妹成绩实在是太差了，本来暑假我姑妈他们都是不准备让我妹妹回珠海来玩，但是我妈妈他们还是让我妹妹回来玩了，然后让我给她辅导功课，我千叮嘱不要抄答案，也不要乱做，可是还是乱做抄答案来敷衍，可是她怎么可能敷衍的过我呢，一眼就看出来了，真的是头疼她的成绩。

2022/7/16
今天遇到的还是二分查找的变种，有一说一二分查找上手还是比较容易，但是要想熟练使用还是有很大一段路需要走，因为题目一般都会是在两个区间之内去使用二分查找，需要多找出区间之内的规律再使用二分查找。二分查找最显眼的标志就是时间复杂度位O（logn）和查找xxxx。以后遇到题目当中有这两个要求解题思路尽量就向二分查找上靠。

2022/7/17
今天遇到的题目是双指针。三数之和与删除链表重复节点，删除链表重复节点不知道为什么没有做出来，按道理来说这个应该是很简单，第一次都做出来了但是第二次没有做出来，可能思维有点僵化。三数之和就是两数之和的变种。首先需要将数组排序，排序之后L，R指针分别令为index+1和len-1，因为已经拍了序号，如果三个数加起来大于0，说明R需要-1，如果小于0说明L小了需要+1.等于0时需要去重，去重也是这个题很关键的一步，通过两个while循环完成去重部分，最后返回数组，双指针的题目有双指针一起在左边，也有双指针在两边的题目，每次双指针题目都要让我想好久，希望可以多练练双指针。

2022/7/18
今天遇到的也是双指针题目，有三个题，其中两个题都是题目给两个列表，这种一般都要用双指针，一个列表一个指针来遍历，但是我看官方的题解写的十分简洁，我写的跟做体力活一样。其中有一个题有一些难度，一开始根本没有看出来要用双指针，而且解题的关键就是容量=指针指的较小值*两指针之间的距离，这样的话移动双指针只能移动较小的值的指针，这样一次遍历就可以将最大容量遍历完成。双指针YYDS！

2022/7/19
今天遇到的题目全都是滑动窗口，一开始第一个题是有点思路，但是后来正确思路没有写出来我还以为是我思路不对，然后歪了之后写了很久也没有写出来（其实主要是因为题目看错了，题目要求>=而我看成了==导致我一直提交出错）。第二个题目是第一个题目的变种，前面的写的很顺利，但是出现了连续的子数组和，这个我没有想到竟然是right-left+1（这里就不进行详细的说明了），第三个题目很顺手，哈希表+滑动窗口就出来了，这几个题都特别经典，需要反复揣摩。

2022/7/23
今天终于有空继续刷leetcode了，高中玩的特别好的同学来珠海格力上班，这几天一直陪同学一起玩，不太方便刷leetcode。今天还是两道深度优先和广度优先的问题，感觉现在广度优先算法我已经比较熟练了，但是深度优先算法总是不太好实现，可能是实现的次数比较少，一边都是递归的实现就行了。希望多来两道广度优先算法练练手。

2022/7/25
今天遇到开始补前面的烂账，今天遇到好几个广度深度优先搜索的题目都没有做出来，题解也有些没有看懂，打算明天再来，今天遇到子集问题其实就是一个二进制枚举，但是当时没看出来于是没有做出来，第二个是深度优先搜索的题目，将所有的路径都找出来，每递归一次就需要纪录一次，主要不知道为什么我做题速度太慢了，希望以后能快一点，知识学无止境。

2022/7/28
今天遇到的子集II问题是子集I问题的变式，相当于也是二进制的枚举，但是要剔除重复的而已，在Python当中排序一下，检查是否在Res（返回的列表）当中即可。这两周一直没有什么时间来刷题，明天回归正常的生活，把之前所有的烂账补上！

2022/7/29
今天本来打算好好写写leetcode但是不知道为什么只写了两道就有点不想写了。今天遇到回溯问题，写是全排列II和组合总数，全排列II我有点想法但是无奈全排列Ⅰ有点没搞懂最后还是看了I的题解然后把II给做了出来，组合总数看到时就有想法，但是准备做第三个题，也就是组合总数的变式，遇到需要剪枝的情况，导致我就不想做了，明天再来看看，马上要交学习报告了，赶紧肝一下学习报告。

2022/7/30
今天写的三个题目，都是要用递归写，三个题目只有一个做了出来，就是给电话号码然后返回全部组合的字母。还有一个括号配对的题目，我其实很有感觉，感觉有一点像二进制枚举的变种，但是编码能力有限没有写出来，看了题解之后感觉还是很简单的，跟我的想法很接近。第三个题目是昨天没有写出来的题目的变种，里面遇到一些剪枝操作，而且我自己写的代码放上去跑竟然会无限递归，最后看了题解之后还是写了出来，主要是剪枝操作我有一点点懵不过好在是看懂了，感觉递归的剪枝操作一遍都是在同一层进行，以前都是比较懒，全部递归出来看看是否in Res当中，但是用这种方法时间经常会超限，所有说剪枝的操作我还是要学一学，刷了快一个月题了，感觉还是有一丢丢进展哈哈哈哈！

2022/8/1
今天遇到一个打家劫舍变种和一个深度优先搜索的题目，深度优先搜索+回溯做了我一个小时，而且最后有一个用例实在是太难跑了，而且我还是递归，本地编译器都跑了半天，只能IF==用例特定输出了，本来早就是写出来了硬是搞了半天。打家劫舍变种还是有一点麻烦，因为首尾也算相连，所有只能在(0，n-2)和(1,n-1)当中来计算机最大，而且还是用的斐波那契循环的方法写的，并不是用DP数列这样计算，题解的代码写的非常优美，以后还要继续加油我。

2022/8/2
今天下午写了三道动态规划的题目，感觉动态规划题目最最最关键的就是找到状态转移方程，第一个是整数拆解，不是很会但是看了题解之后懂了，然后开始最零钱转化的问题，其实提前转换和整数拆解是一个题目，就是整数拆解从1~J拆解，零钱拆解通过给的数组拆解，虽然懂了但是编码能力太差还是没写出来，最长递增子序列还好之前做过，有惊无险的写了出来。

2022/8/3
今天下午遇到三个题，有两个贪心算法一个动态规划，动态规划的题目我倒是写出来了，但是贪心算法的题目我看不出来我总是用动态规划写导致老是超时，我要去百度查查什么题用DP什么时候用贪心，还有就是妹妹学习实在是太差了，不知道究竟是不是没有天赋，但是我感觉不至于，应该是没有用心，实在是脑阔痛。

2022/8/4
哇塞，动态规划实在是太难了，如果只是数字的动态规划我还能做一做，如果抽象成字符的那种就要花费我很长时间，今天两个题都没做出来，每个都做了一个多小时，真是功亏一篑，编码太差而且总是差一点点感觉，还是要继续加油，本来还想继续写，看了题解还是有一点点问题没有搞懂，但是今天要出门了，这几天都没有看机器学习，马上又要交学习报告了，真是烦死了。

2022/8/5
今天遇到一个二维DP的动态规划题目，根本没有头绪。看了一下题解，如果只给了一个数组的动态规划题目，一般就是一维DP，如果是两个数组或字符串，那么一般就是二维的DP。看了题解之后知道怎么做了。然后还有一个有一个大坑。因为我一般都是用Python刷题，然后这次数组的初始化时[[0]*(M+1)]*(N+1),但是这个初始化会导致二维数组当中的每一个一维数组都指向一个相同的地址，相当于浅复制，如果你改了其中一个一维List中的一个数，那么其他一维List当中的相同位置的数字也会改变，二维数组的初始化应该写出[[0]*(M+1) for _ in range(N+1)]。

2022/8/8
今天做的题目叫做“编辑距离”，就是给定两个字符串，只有增替插三种操作，计算出最少的操作次数，之前因为已经有一点经验了而且大二做过，所以还是有一点点想法。DP数组呢还是用一个二维的数组。数组大小为(M+1)*(N+1)因为要包含两个空字符串的形式。空字符串到word1，也就是第一行的DP就是0，1，2,...,N，第一列也是同理。其次最关机的就是比较字符串word1[0...i-1]和word2[0...j]，word1[0...i]和word2[0...j-1]，word1[0...i-1]和word2[0...j-1]然后更新DP数组，返回DP[N][M]。

2022/8/9
leetcode上面的算法怎么这么难吖！一个是要求写一个打乱数组的数据结构题，数据结构题根本没怎么刷过然后还有一个就是按位与，给定一个range然后按位与，输出数字。将最大和最小一起右移直到两个数字相同，返回位移后的数再左移跟他们右移相同次数的数。不用考虑其他数因为是在range当中，总会有0在中间（这一层当时没有想到），还有最长回文子串的动态规划算法实在是太难了，明天写吧。

2022/8/10
费了九牛二虎之力终于把昨天这个题给做上了，解析写的太复杂了，让人看不懂，总结就是回文串长度1，2要单独考虑，因为用动态规划的时候aba让左右都减去a，只剩下一个，如果是abba，左右都减去a，剩下两个，所有说1和2的情况单独考虑，其他的用转移方程。还有一个题巨TM恶心人，写了快一个小时还是没写出来，难是不难就是恶心。

2022/8/12
这几天厂里太忙了，回到家都已经很晚了，根本没时间做题了。今天做了一个题叫做用户分组，其实并不是很难，但是经过前面的毒打过后我总是想用O(N)的时间复杂度把它做出来，但是还是没做出来，可能是编码能力不行，但是用了O(N^2)的时间复杂度提交也是过了，心里滋味复杂。

2022/8/13
一个回溯题，一眼看出来了，但是写还是用了20分钟多。

2022/8/15
今天是一个合并K个有序链表，分治法，踩了一个大坑，10^4+1！=10**2+1，改BUG改了30多分钟，终于把这个找出来了。

2022/8/16
今天做了一个esay的数据结构题，比较简单一次提交就过。但是遇到一个hard的算法题没有做出来，虽然我的做法通过了大部分的测试，但是有几个长的需要的时间太长导致提交时时间超限了，看了题解要用线段树，看了很久也没有看懂，明天继续加油弄懂。

2022/8/17
加上昨天的以一共做了两个周赛，周赛现在能稳定做出两个题，三个题一般都能做出来，但是第四题有点难度，不太好做，明天研究这两个周赛的第四题。

2022/8/18
今天写的周赛题实在是有点难，可能还是有些没有掌握好，今天周赛只做了一个最简单的就没有做了，实在是不想做了，明天继续加油吧。

2022/8/19
害，最近今天一直没做中档题，一做就寄，继续加油吧。

2022/8/22
今天写了leetcode一个周赛，只做出来了两题，一题是A+A'==B+B'这种类型的题目，还好之前好像做个一个类似的，一开始没想起来，后来想起来了做了出来，就是移项，然后用哈希表记录就行，还有一个广度优先搜索，这个比较简单也做出来了。还有一个好像是求最小公倍数，但是我不知道怎么求，这个没做出来，第四题根本没时间看了，什么时候我也能半小时AK拿一个周赛第一捏~

2022/8/23
哎我操，今天就写了一个题还没有写出来，理解错题目意思了，这几天可能没时间写题了，要准备去学校，收拾东西了。

2022/8/24
今天写了两个简单得练手题，一个是之前思路错了没有写出来的题，主要是题目有些“依次”，“一开始”这种没有看到，一开始就想着用回溯，回溯倒是也写出来了而且时间也比正常写消耗的端，可惜这些条件限制了不让用回溯，第二个就是单纯得简单练手题。

2022/8/25
今天遇到的题目一眼就看出来是双指针了，看来这两个月刷题还是有效果哈哈哈哈！

2022/8/26
明天就要返校了，学习报告还没有写，今天先写一个简单的每日一题练练手好了。

2022/8/29
刚到学校几天还有一点不太习惯，今天写了三个题，两个简单题，一个hard，关于记忆化搜索，记忆化搜索在Py3里要对函数用装饰器@lru_cache，然后函数要返回一些值，这样当其他的搜索走到下一步的时候直接加就行不用继续运算了，节省了很多时间，不过很不熟练。

2022/8/30
今天做了一个之前的小竞赛，做了三个题，但是只有其中一个我是敢肯定我交上去就能通过的，其他两个我做的方法和题解都不一样但是竟然都通过了，第一个简单题当时还让我想了很久，我本来以为是贪心算法，就是先给数组排序然后慢慢加，题解是前缀和，但是我那样做也是做出来了，还有一个也是做出来了本来以为不对但是交上去竟然就对了。

2022/8/31
2392属于拓扑排序hard题，本来像这个给优先级，但是发现给优先级没办法更新前面的优先级大小而且没办法检查是否有环，这个题明天再来。做了一个中档题，模拟栈的运行顺序一次AK。

2022/9/1
今天一个简单题，本来不想用二重循环但是没有做出来，结果用了两重循环就直接出来了，看题解好像是用单调栈求左边最小的第一个元素。

2022/9/3
排序+动态规划，这个动态规划题目跟之前做过的一个很像，所以一次AK。继续加油！

2022/9/4
米哈游的题雀氏难，只做了两个，简单题都花了我半天，第二个题是记忆化搜索，对记忆化搜索的理解加深了一部分，但是这个题还是没出来，虽然我感觉我想法应该是跟题解一样的，但是就是没做出来不知道为什么，不过也算有收获。

2022/9/5
今天遇到的二叉树题目不太会，本来打算一个一个遍历来着，其实想法就错了，题解正确做法是二叉树序列化，遍历哈希表来做。继续加油！今天晚上还没有课，把之前没有做对的题目顺便搞一下。

2022/9/6
HARD果然名不虚传，这个题刚开始看的时候还是很有感觉的，但是做出来完全是错误的，首先是python编码不行，其次方法也不对，题解是根据子字符串个的贡献来计算总和，而我直接想要回溯暴力，结果完全就错误了，继续加油！

2022/9/7
今天写了一个简单题，但是幺蛾子还挺多，其他倒是没什么特别的关键是除了0的情侣，最后加了一个Token，当有除0情侣就让Token=1加上去一起除这样就解决了除0问题。

2022/9/8
今天这个题有点偏OJ风格，其实不是很难但是主要是考你能不能找到规律，很遗憾没有找出来，给n个数字，根据这个数组前后绝对值，构造一个k个不同值的数组，其实就是1，n，...然后2,n-1这样排列先把K-1个搞出来，后面的全部弄差值为1即可。

2022/9/9
简单题，easy！

2022/9/11
今天这个hard很难，完全没有思路，第857题，主要是通过工人性价比，用大根堆维护一个最低的工作质量从而获得最低的支付工资，遇到两个数组的题没有思路的话可以试试除法，已经遇到好多个运用除法从而或得O（N）的时间复杂度题目，话说回来，这个题简直秒不可言！

2022/9/13
中档题，一开始还以为是全排列变种，后来发现只能交换一次，试了好几次终于用递归做出来了。

2022/9/14
简单题。最近有点水逆，档案给本科学校寄到研究生学校弄丢了我真的TM服了。

2022/9/15
绝世推理题。首先发现灯的周期是6，其次5、6灯的状态和2、3灯状态相同，最后可能找出灯的推理图，代码不难主要是难推。

2022/9/17
这个有点像两数之和的一个简单题，但是当时没有看出来，用的python当中defaultdict把每个字母的每个位置记录下来，用最后一个位置减去第一个位置，也做出来了，现在想起来好像两数之和的做法简单一些。

2022/9/18
几个简单题，不过今天竟然第一次做了一个hard题出来，还要继续加油吖！

2022/9/19
一个简单题和一个hard，hard没有做出来，明天再看看。

2022/9/20
今天的每日一题是个回溯题，虽然刚开始有点感觉回溯但是并没有往这个方向靠，结果没有做出来。看了题解之后才知道这个题多难。以前的回溯都是index==len(nums)之后直接添加数组到返回集合中，这次是返回bool类型，没有经验，一开始还不知道怎么做。其次是剪枝操作的一些细节理解，加油加油！

2022/9/21
今天每日一题有点难，一开始我以为想全排列一样，总是能够换出s1的所有情况，但是没换出来，看了题解之后用的BFS剪枝成功通过，然后通过的用例也非常险，如果Res已经有了答案，但是在递归途中Changes>=Res了就可以直接补递归了，继续加油！

2022/9/25
中档题，一次Ak.

2022/9/26
这个题有点难，我看题解是用的位运算，没有看懂，然后看评论，原来是一共有n+2个数，缺的两个数是x,y。先求差值a=x+y，再求b=x*2+y*2，解方程，然后返回数组，不过当时没有看出来，继续加油！

2022/9/28
今天这个题有点感觉但是没有做出来，虽然我感觉应该是3，5，7里面来回换着乘最后得到答案但是没有写出来，看了题解，用的动态规划，通过上一个DP数组暂存数字累乘得到最终答案。

2022/9/30
一次AK。

2022/10/4
中档题，一开始想法有点歪好在后来发现了规律。主要是要抓住如果遇到")"括号，"("括号的队列里没有左括号是要算到返回当中，抓住这个规律就能做出来。

2022/10/8
索引排序加田忌赛马。学会了怎么对数组进行索引排序，然后用田忌赛马的方法找出匹配的数组元素。

2022/10/9
今天是一个只有（）括号的字符串求值问题，今天这个没有想出来，看了题解，感觉方法确实很巧妙，O(n)就能出来。当时我也思考了很久但是没什么头绪。我也想用栈但是不知道怎么用。每次遇到（括号就往栈加0，0是栈内的和，然后遇到）括号就比较，如果是0就在栈未的值加1，否则乘2加到栈尾，用max(2*stack.pop(),1)一句话就能实现两个效果确实很巧妙。最近状态不太好，几个中等题都没写出来，还是要继续加油才行。

2022/10/10
今天每日一题是一个Hard的DP，设两个数组，一个是交换数组一个不交换数组，根据前面是否是nums1[i-1]和nums2[i-1]判断是否需要加1.还是很难的题，继续加油吧。

2022/10/13
今天一直上课都没来得及写，就是找Index和arr[Index]的关系，如果当前的Index!=arr[Index],就在arr[Index:arr[Index]]中找最大的arr[Index],然后继续循环找，直到走到最后都没找到比当前最大还要大的arr[Index]就划分一个块，如果Index==arr[Index]，也单独划分一次，这样O（N）就出来了。

2022/10/14
今天每日一题是个字符串的子序列变种问题，其实还是有点难度。DP[Index]=DP[Index]+NewCount-Reapet。NewCount实际上就等于DP[Index-1]，Reapet是上一次遇到这个字母的NewCount，一直规划就行了。

2022/10/17
滑动窗口+哈希表，虽然知道怎么做但是写不出，题解的代码确实精简，还是要加强练习。

2022/10/18
今天这个hard题有点想法，写的代码总是最后几个测试用例超时。看题解用的是数位DP，其实看完代码之后感觉数位DP更像是记忆化搜索+深度优先策略。就是根据从左到右依次规划，根据当前位置的数来判断下一位数字的可选择范围，最后一次性返回，解法确实秒，可能还没有练到家现在。

2022/10/19
简单题，一次AK。

2022/10/20
中等题，就是一个找规律的题目。一开始看了一下数据量以为直接模拟队列可以暴力遍历出来但是直接报超时，把队列打印出来了，当时思路就已经往找规律方向靠了，但是没有找出来规律。实际上的规律就是当前Index所在的长度是上一次Index长度的2倍，前半段与上一次Index的队列相同，后半段则是取反，用递归的方式往下找，虽然当时看了题解之后知道规律了但是还是写不出，还是要多练感觉。

2022/10/21
中档题，感觉还是题目有点没有搞懂，他说是往回看最长有多少连续天数的股票价格小于当前价格，我理解的是可以一直往前面找，就算中途断过一次也继续统计Max天数，但是题目好像是不统计，断了就终止。题解是同单调栈，维护一个天数的变量，把栈当中所有小于当前价格的天数弹出，计算当前天数与栈当中倒数第二天天数的差值。

2022/10/22
今天这个每日一题太难了，完全没有头绪，而且根本没有时间做了，大致看了一下题解，DP+二分查找，就是动态规划需要看前面的DP有没有合适的，前面的DP下标就用二分查找来找，不过还是有点没有看懂，等着明天再来研究吧实在是没有时间了今天，不过有一个收获就是python当中有二分查找的容器还是不错，可以用来解题，方便。

2022/10/23
简单题，一次AK。

2022/10/24
今天的中档题竟然没有做出来，我原先以为是可以通过数组大小的索引的排序就能找出来，可惜总是有用例不对，感觉上应该是很快就能做出来但是还是差一点。题解时间复杂度O(N)，就是一直维护一个当前下标之前数组的最大值，不断与后面的数进行比较，如果后面的数比前面的数小，就把这个新数字的下标包含进去，更新CurMax,最后返回下标就行。

2022/10/25
今天每日一题还是没有做出来，虽然看到题目之后知道是图类的题目，而且还是问的最少要走多少步，看起来应该就是广度优先的题目，但是还是没有具体的实现出来，而且还有一个关键的信息没有看到，就是图中只会有两个孤岛，这个很关键。题解的思路是先把一个孤岛找出来，全部标记为-1，利用广度优先的搜索办法，检查第一次接触到1的step，返回step就行。编码还是差了点，还是要多看多谢才行。

2022/10/26
今天的每日一题是个hard题，完全没有思路，我一开始还以为是动态规划呢。前缀和+双端队列解题，首先用preSubNums统计数组的前缀和。依次遍历数组preSubNums,固定当前遍历的i，从队列Queue的第一个元素开始找(Queue当中存储的是下标)，如果找到CurSun-preSubNums[Queue[0]]就存储起来i-Queue.pop(0)，再动态的维护Queue的单调性，因为Queue当中的下标，在preSubNums当中会有大于等于CurNum的情况，将他们弹出，因为CurNum下标比较靠后，如果能够更新的话，越靠后的Res会更小，最后返回Res就行。

2022/10/27
简单题，一次AK。

2022/10/28
又是一个单调栈题目，每次单调栈题目都看不出来。通过单调栈将当前位置i的左边辐射区域与右边辐射区域统计出来，收到影响的数组数量有L*R个，只需要乘arr[i]，加到返回值上，就能够在O(N)的时间复杂度下把答案求出来。

2022/10/29
今天出去监考一天，快十点才回到寝室，好在是一个简单题，一次AK。

2022/10/30
今天中档题是之前做过的一个题，二进制枚举即可。

2022/10/31
一个找规律的题目，功亏一篑。拿到题目我就感觉应该往找规律方面靠，但是我一直以为是初始化前两个开始找，但是总是没找出来，原来是初始化前三个开始找，从前三个开始，配合当前指针指的值延展数组，O(N)复杂度内就能出来。

2022/11/1
一个简单题，把每个List当中的字符串拼接起来比较一下就行。

2022/11/2
当时看数据量最多只有30个towers，当时感觉能枚举出来，但是我以为最大值只会出现在点的坐标上，看完题解也是枚举，但是提前统计了出现的边界框，然后做3次for循环枚举出来，三次for枚举出来也是感觉很奇怪，很少有遇到3次for循环的情况。

2022/11/3
一个简单题，差点没做出来，主要是没想到暴力能遍历出来，好在是遍历出来了。

2022/11/4
一个中档题，看完题目后我的第一反应是target正负的情况可以只考虑大于0的情况，事实上也确实如此，但是思路有点问题，因为我一开始我尝试用深度优先，深度优先确实可以出来答案，但是答案并不是最优的，后来我想尝试广度优先，但是广度优先的停止条件不知道怎么找，最后卡住看了题解。题解说这是一个数学题，分了四种情况讨论。第一种情况就是一路往左走，刚好走到target。第二种情况是不能刚好走完，但是超过target的nowPos-target是一个偶数，那么就把第一步往右走，其他往左走，这样就能刚好到target，而且步数没有改变。第三种情况是，超过target的nowPos-target是一个奇数，那么倒数第二步往回走，这样叶能刚好走到，但是步数会+1。第四种情况是，超过target的nowPos-target是一个奇数，再走一步也是奇数，这样的话倒数第二步左走，最后一步右走。就这四种情况，我看题解代码写的非常精简，但是能包含这四种情况，确实牛逼。

2022/11/5
今天这个hard题还没有昨天mid难，但是还是没有做出来，这个题虽然很好想但是不好下手，可能还是我代码写的太少了，思路是正确的，用栈暂存就好了。

2022/11/6
简单题，一次AK。

2022/11/7
一个中档题，一开始思路是没什么问题，但是花了我不少时间。先把左右括号去掉，得到数字字符串，先将数字字符串划分Left和Right，先看看Left和Right是不是合法的整数，如果是合法的整数就加入LeftList和RightList，然后看看Left和Right有多少种能够合法划分的小数，如果能合法划分就加入LeftList和RightList当中，最后用一个双重for循环将他们输入到返回的数组当中。有一个问题是如何判断数字是否合法，要合法就必须满足两个条件，1是第一个数字不等于0，要么就等于0(整数只需要判断是不是满足这一个条件就行)，2是小数部分最后一位不等于0(小数需要满足两个条件)。这个题最后花了很久时间是因为判断if语句的时候，本来应该是=='0'，结果写成了==0，导致两个0的类型不一样，最后花了很长的时间去找错，下次要小心才行。

2022/11/8
简单题，先遍历List[str]当中的每一个word，再遍历每一个word当中是否有不在Dicts当中的字符，如果有则进行标记，在退出第二重循环时Sum不进行+1，这样一次遍历就能够通过，时间复杂度O(N)。

2022/11/9
今天一个跟图有关的问题吗，在一个图上有0有1，找全为1的十字架最大的阶数。一开始我还以为是深度优先遍历，但是最后有10个用例会超时。看完题解之后发现使用动态规划，直接解题方向就错了。不过虽然方向错了，但是思路还有有一点点相似的地方。我的思路是每一个点开始遍历，从上下左右四个方向开始查找最小的路数，最后从全部的点当中比较最大的。题解是用动态规划从左到右，从上到下，从右到左，从下到上，两次两个for循环遍历，如果当前的点不为0，那么就在之前方向的基础上加1，最后更新到DP数组，看看是否比DP数组小，小的话就更新（因为DP数组当中的数字有其他方向来的，我们要统计最小的阶数，在最小的合法阶数当中找最大阶数），最后返回就行。

2022/11/10
今天这个hard属于是长见识了。眨眼一看好像发现不是很难，就是一个广度优先搜索算法。但是题目里面加了一些条件，你必须在路径当中捡到钥匙，这样再遇到锁的时候你才能继续走。这样的话就非常麻烦了。题解用BFS+状态压缩。首先就是先遍历一次图，记录开始位置在栈当中，统计一共有多少把钥匙（钥匙的顺序大小按a-z这样排序压缩到一个int类型的数字当中，更新和判断是不是对应锁用位运算来判断），然后遍历队列。从当前点的四个方向开始搜索，如果坐标超出了界限，就continue，因为后面还有可以遍历的方向。遇到墙也continue，遇到锁判断没有对应的钥匙也要continue。然后创建新变量NewCur，如果遇到钥匙了，更新NewCur,更新的公式就是NewCur|=（NewCur<<(ord(当前字符)-ord("a"))）。如果更新后的NewCur==（1<<钥匙数量）-1的话，那么就意味着所有钥匙都收集齐了，返回当前的Step+1，如果没有收集齐，看看当前的坐标(NewX,NewY,NewCur)在Dists的记录当中Step是多少，跟Step+1进行比较，如果Step+1比Dists当中的大，那就不用记录了，因为最终答案肯定不是它,否则就记录下来，并把坐标加入到队列当中，直到队列为空。如果队列为空都没有返回，那就没有通路，返回-1.

2022/11/11
简单题，但是题目没看清楚，只是统计元音字母的个数而已，我还以为要用哈希表来辅助统计判断，好在是过了。

2022/11/12
今天是一个中等题，但是今天这个题我感觉比较新颖，题目看起来是一个图类的题目，但是读完题目之后又能感觉出来不是。就是有1*2的长条多米诺骨牌和由三个小方块组成的L型多米诺骨牌，要将他们排列在2*N的格子上，看看多少种排列方案。一开始我以为是找规律的类型题目，我把1-8的答案都输出来看了看但是还是没有找出来答案。看完题解发现是通过动态规划来做。F[1]=1,F[2]=2,F[3]=5,这三个是方案确定的，F[4]呢是通过F[3]的答案拼接新的组合方案+F[2]的答案拼接新的组合方案+F[1]的答案拼接新的组合方案。F[5]的答案又和F[4]、F[3]、F[2]和F[1]有关。但是这样肯定不行，因为F[n]的答案就要回头统计F[1]-F[N-1]的答案组合。由于递推公式F[N-1]=F[N-2]+F[N-1]+2*(F[N-1]+...+1)，将N-1替换成N，将F[N]和F[N-1]做差就能得到简洁的新公式F[N]=F[N-1]*2+F[N-3]。

2022/11/14
一个hard题，做法确实挺巧妙，通过公式变形，可以变换成SUM(A)/K==SUM(nums)/n。通过二进制枚举左边，将左边的所有子集枚举到left的集合当中，右边也是一样得操作，判断右边的子集有没有和左边子集是相反数的，如果有就返回false。

2022/11/15
简单题，一次AK。

2022/11/16
一个中档题，虽然有点感觉但是还是没有做出来，我发现了局部倒置一定是全局倒置这一点，想着如果能找到非局部倒置，那么就能够通过这个判断出来，但是并不知道怎么避免O(N)的时间复杂度，最后题解也正式利用这个规律，从后往前遍历，从len(nums)-2的位置开始到1，如果num[i-3]>minSuf,minSuf是从nums[-1]到nums[i-2]位置维护的最小值，如果有num[i-3]>minSuf的情况，就可以返回false了。

2022/11/17
今天这个题我一开始的想法就是遍历words当中的每一个word，看看word是否是s当中的子序列，虽然想法没什么问题但是最后9个用例会超时，看完题解之后，题解也是提到了这个问题，虽然题解看懂了但是代码我有点问题，题解通过哈希表将s当中的每一个字符的index都存储起来，然后找word[j]当前指的这一个字符的哈希表当中的下标来找，但是代码我总觉得没看太懂。

2022/11/20
一个中档题，模拟香槟塔，计算某个位置上杯子装了多少香槟，一开始没有想好怎么模拟出来，看了题解之后懂了。

2022/11/21
今天这个题是概率+记忆化搜索，这种题真的有人能写的出来吗？题解太长就不写了，808题。

2022/11/22
hard题，题解不知道怎么写才好，直接上题目878。

2022/11/23
一个简单题，一次AK。

2022/11/24
最近写leetcode总是感觉不太认真，今天又是一个中档题，一眼看下去感觉是单调栈但是单调栈总是感觉掌握不是很熟悉，抽个空看看单调栈专题加强一下练习才行。

2022/11/25
采用双指针，首先判断s[i]==t[j]，如果两个字符不相等，则返回false,如果两个字符相等，就往后遍历两个指针，指向s字符的指针统计的当前字符与指向t字符的指针指向当前字符的数量，指向s的指针字符数量要大于指向t字符的指针，如果小于就返回false。如果两个两个指针指向的字符数量不相同，那么指向s的字符指针的数量要大于3，否则也返回false。

2022/11/26
一个简单题，一开始还在想怎么在O(N)时间内做出来，结果看了一下数据量，就在100以内，感觉应该可以暴力遍历出来，果然一次提交就过了。

2022/11/28
一个中档题，一开始看数据量感觉好像可以遍历出来，但是当时不知道怎么实现。题解先是统计了前缀和帮助遍历，其次用动态规划，先规划好J=1的数组(就是可以不用分割直接统计平均值)，将值存储到DP[IndexI][1]当中。其次J从[2,k+1]当中遍历，I从[J，len(NUMS)-1]当中遍历，因为I的值必须要比J大，不然分不了足够的子数组，最后X从[J-1,I],计算DP[IndexI][IndexJ] = max(DP[IndexI][IndexJ],DP[X][IndexJ - 1] + (PreSum[IndexI] - PreSum[X]) / (IndexI - X))。

2022/11/29
简单题，但是第一次没有通过，因为有几个用例情况没有考虑好，更改后我从每次的第一个开始，第一个字符不变遍历一次和第一次字符取反遍历一次，这样取小就行。

2022/11/30
一个hard题，构建一个频率栈，频率相同就弹出最后一个。一开始我的思路就是用一个哈希表辅助，但是只用一个哈希表辅助的话，虽然统计最大的频率方便很多，但是你要POP操作弹出最大频率相同靠后的就有点麻烦了，然后就没思路了。题解用了两个哈希表辅助，一个是用来存储最大频率，一个是构建每一个频率里的val，当你需要POP操作，直接对着最大频率的哈希List弹出就行，但是细节是每次弹出需要检查是否当前MaxFreq的哈希List是否为0，为0的话就要让MaxFreq-1。

2022/12/1
简单题。

2022/12/6
偷了几天懒，今天一个简单题，想复杂了，好在是没有浪费多少时间。

2022/12/7
一个中等题，完全没思路。题解是哈希表+贪心算法，首先要先比较两个数组的和大小，让数组和小的为nums1，数组和大的为num2。如果我们想要最快的追平DIFF，肯定要让数组小的尽量变6，数组大的尽量变1，我们从5-1遍历（因为差值的范围只会是从1到5），然后遍历的时候，如果diff>i*Cnt[i],我们直接diff-=i*cnt[i]，然后步数Res+=i,如果diff>=i*Cnt[i],直接返回Res + (Diff + item - 1) // item。

2022/12/8
一个简单题，就是统计国际象棋每一个方格的颜色，如果这个方格的位置坐标对2取余的值是相同的，那么就是黑色，否则白色，非常简单一次就过了。

2022/12/9
一个中等题，判断一个数字能不能被不同的3的幂给表示，没有做出来，其实想法也很简单就是对这个数字进行进制转换，但是不能有2在进制位上，因为这样就不满足不同的幂和了，能转换出来就returnTrue。

2022/12/10
一个困难题，完全没有思路，题意是给二维数组，二维数组当中的每一个一维数组都是一个长方体的长宽高，这个长方体在堆叠的时候可以旋转，因此长宽高是可以互相变换的，题目要求返回堆叠最高的高度，因此我们首先对每一个长宽高进行排序，让每一个正方形高的长度最大，这样才能找到最长的堆叠高度，对每一个i下标的长方形找[0,i-1]，计算他们存粹的到他们的最高高度，在符合情况的条件下往下动态规划就行了。

2022/12/11
今天一个简单题，一次AK。

2022/12/15
昨天才放假回到家，还没来得及做LeetCode，今天一个简单题，一次AK。

2022/12/19
前几天阳了一直没力气写，今天终于恢复了不少，但是今天是一个图的简单题，竟然没有写出来，可能是我图搜索算法掌握的还不牢固吧，还要继续努力。

2022/12/20
现在经常看中等题没有思路，今天是一个二分查找的题目，说实话题解代码还是设计的还是一如既往的巧妙，就先就是要先看出来用二分查找才行，把左右边界设定在[1,max(nums)],将一个口袋的数分成Mid，需要的次数时是(nums-1)//Mid，这个时候更新返回值，并且继续查找看看有没有更小的返回值。

2022/12/21
今天一个中等题，感觉最近的中等题我都做不起。分情况讨论，先排序，如果a+b<=c，那么直接返回a+c，如果a+b>c，返回(a+b+c)//2。虽然但是，我公式还是没看懂怎么推的。

2022/12/22
一个hard，没有做出来，状态压缩+动态规划。首先先申请一个二维数组，将给定数组的nums的所有两个数的GCD全存储起来。循环偏移[0,2^m-1]，具体做法就是1<<m就行。主要是要遍历2^m-1个状态，遍历之前要先判断当前的数二进制中的是不是偶数个，不是偶数个就不便利。是偶数个之后暴力循环每一个二进制中的1，计算他们的GCD分数加到F[K]当中，这样就算的就是为k状态下的最大得分。

2022/12/23
今天终于来了一个简单题，但是太简单的没什么意思啊。

2022/12/24
一个中等题，第一次我直接根据当前字母大小来排序，但是有点问题，后来改成了按照字典序添加一次就过了。

2022/12/26
今天一个中等题，一开始我还以为是就是把乘法改成加法直接相加就行比如第一次+1，第二次重复出现+2，第三次+3这样，但是题解是直接用求和公式做出来的，我这个方法我没有写出代码来求证，不过仔细想一想好像也是可以通过的，试了一下好像勉强通过了。

2022/12/27
一个简单题。

2022/12/29
今天的每日一题是个简单题，统计三个数组当中出现在两个数组以上的数字，直接先把每一个数组都Set一下然后放入哈希表中，将三个哈希表相加起来遍历一次，看看Val>=2的就将Key加入到返回列表当中。然后还补了一下昨天的每日一题，昨天的每日有点没有看懂，今天总算是看懂了，就是判断一个字符串，从前看和从后看是否有相同的，要是有就删除前面和后面相同的字符(数量倒是不用管，直接有相同的全部删掉就行)，最后返回Right-Left+1就行(Right-Left+1)其实就是去掉之后字符的长度。

2022/12/30
今天是一个数据结构的中等题，发现自己在做题当中的一些问题，比如当我需要使用数组记录的时候，我常考虑申请一个很大的数组，这样的话不仅空间会超限而且很可能没办法维护遍历，我可以申请一个数组使用优先队列的想法，就把已经记录的按照二分查找遍历维护就行了，没必要全部申请下来。还有就是今天的题没有做出来，看了题解之后确实是懂了，主要就是距离可以通过(Left+Right)//2，然后位置就是Prev+Dist就行了。

2023/1/2
前两天放假，看题目都是简单题实在是不想做。今天是一个中档题，其实我感觉我跟题解的思想是一样的，但是我一开始还是犯了之前的错误就是想要一个一个的全部存储在数组当中，因为我感觉这样简单一些，但是这样做今天的题目第一个用例就超时了，后来我用一维数组[Price，Amount]存储在数组当中变成二维数组，但是感觉久了没有认真做题导致我脑子有点慢，写的有点奇怪而且我还发现了我代码的一个问题就是我不知道怎么保持根据一维数组当中的某一个位置来保持二维数组的有序，然后题解用的是heapq保持优先队列，我是使用的二分查找插入的方式保持有序，好在是写出来而且发现了问题。

2023/1/3
今天是之前做过的一个简单题，但是当时练的太少了，现在回头看看确实是长进了一些，改进了一下之前写的，一次AK。

2023/1/4
今天是一个中档题，题目需要用到二分查找，但是我没有看出来是二分查找的题目。我总是感觉二分查找的题目隐藏的很深，两眼一蹬就只有看题解了。首先，解题的第一步就是要了解到，锁定了nums[index]之后，整个数组的Sum就固定了。但是一开始我的想法是用maxSum给nums[index]，然想办法分配maxSum,这样的话一开始就错了。第二点解题的关键就是找[1,maxSum]当中小于maxSum的数字，然后这时候就遇到一个问题，需要计算当前数组的和，编写一个函数因为是左右都是等差数列，但是会有max>=Cnt和max<Cnt的情况，这时候要想好计算的公式。最后还有一个我没有搞懂的问题就是mid=(left+right+1)//2为什么他要+1再÷2。我看题解是因为不这样做会有死循环，比如Left=3，Right=4,这时候计算Mid=3,永远也跳不出循环。

2023/1/7
又是隔了几天才做，主要是前天的没有看懂然后昨天有事情耽搁了。今天这个题我一开始还简单的以为是一个贪心算法的题目，先比较数组最左端和最右端到底谁大，判断能不能减，如果不能减就减小那个，如果小的也不能减就返回-1，最后再看看x是不是等于0，是就返回ans，不是就返回-1。但是这样做会有解答错误，说明是算法不对。看完题解以后发现是用的滑动窗口。首先统计数组的总和，如果数组总和大于我们要寻找的值，直接返回-1，因为就算全部减去也不能找到目标。然后让left=-1,right=0。遍历left从(-1,n-1)，顺带说一句left不可能到达n-1，到达n-1就和sun(nums)>x是一种情况。然后当left!=-1的时候，我们每次循环都让前缀和加上nums[left],每一次循环我们都要缩短后缀和，当lSum+rSum>x的时候就一直让rSum-=nums[right],然后每次循环判断lSum+rSum==x，符合条件就就不断更新返回值，返回值的更新公式ans=min(ans,left+1+n-right)。这个更新公式就考虑极端情况，就比如第一次遍历的时候就满足，比如left=-1，right=n,这时候应该是操作了n次，然后一次考虑left=0,right=n-1，这样就能把更新公式给找出来了。

2023/1/8
简单题！

2023/1/9
今天一个中档题，看懂了题目之后我直接用暴力的方法每一次循环都将新的arr给写出来判断是否正确，我以为这种方法叫做暴力原来是叫做模拟，一开始我本来是打算不这样做的但是看了一下数据好像很小试了试没想到就过了。

2023/1/11
简单题！

2023/1/12
今天做了两个题，1个是腾讯面试题，昨天晚上看到的。还有一个是今天的每日一题。先说今天的每日一题吧，今天的每日一题我感觉我是可以做出来的就是一个很简单的Strs当中括号括起来的key换成val，但是没有做出来太气了，其实真的非常简单的但是没有做出来实在是太气了。第二个就是腾讯的面试题，昨天晚上看到的，就是吃橘子有三种操作，1是吃一个橘子，2是如果橘子个数能够整除2，就吃掉二分之一的橘子，3是如果橘子个数能够整数3，就吃掉三分之二的橘子，但是有时候会解答错误而且给的数据实在是太大了，容易超时。题解是递归的往下查找if n<=1:return n否则return 1+min(n%2+fun(n//2),n%3+fun(n//3))，并且使用记忆化搜索,把时间复杂度限制在O(log^2(N))，这样做其实还有分析的步骤，一开始本来还有(N-K)的步骤，但是这个步骤被剪枝操作剪掉了，直接用n%2和n%3代替掉了。

2023/1/15
一个简单题，回到家之后学习状态确实下降了很多，找个时间把昨天的hard给做了。

2023/1/16
又是没有思路的一天，题目给了两个字符串，只有字母和空格组成，要判断一个句子是否能由另外一个句子再加另外一个句子组成。这个题目先将两个句子直接分割，然后双指针，从前往后和从后往前扫描，统计相同的单词个数，最后判断相同的单词个数相加是否等于最短的单词个数就行了。

2023/1/31
终于从老家回来了，今天是一个中档题，给了一个二维正方形矩阵，要求判断二维正方形矩阵是否对角线上都不为0，非对角线元素都为0。一开始没有看数据大小，但是还是做出来了，用了一次循环，遍历所有对角线元素，看看有没有对角线元素为0，如果有对角线元素为0就返回false，然后将对角线元素加到sumGrid变量上。还有一个细节就是如果二维数组大小是奇数，比如3*3，5*5这种，最中间的元素会被多统计一次，在遍历完对角线元素之后要记得判断二维矩阵大小，如果是奇数就减中间元素。最后返回sum(sum(row) for row in grid)-sumGrid==0,虽然感觉python当中sum元素也是用了O(N^2)的时间复杂度但是还是做出来了。

2023/2/1
一个简单题。

2023/2/2
一个中档题，题目是要求判断0到N个节点当中，路径要交替的最短的距离，我能把方法看出来，但是写广度优先过程当中不知道怎么保证条件，最后还是看了题解。

2023/2/3
今天是一个中等题，关于图的遍历，本质就是计算一个给定的点，它会有三个区域，左儿子区域、右儿子区域和其他节点，分别统计这三个区域的节点数，看看有没有一个区域是超过了一半的节点个数，我当时也是这样想的但是我在写代码的时候与到一个问题就是不知道怎么统计第三个区域的个数(其他节点个数)，因为我只写了一个统计节点个数的函数，我看题解是在里面直接加了一个寻找是否为当前节点的if条件+nonlocal来标记，最后统计就行了。

2023/2/4
中等题，给出一个无序coins数组，随意取但不能重复取看能找出多少个最大连续整数。一开始我是想排序+动态规划做，但是在找递推公式的时候并没有找出来，我还以为是自己思路不对，后来题解也是这样做，但是题解是集合集合的判断。现在有整数集合[0,1]，然后coins[i]=1,将他们加起来，集合变成[1,2],这个集合是可以和前面没有加coin[i]集合拼接起来的，所有是可以，然后找到规律就是tail(上一个集合的最后一个数字)是否比coin-1小，如果小的话就可以拼接，最后将结果递归出来。

2023/2/8
一个中等题，删除一个列表当中的子文件夹。脑子抽筋没有做出来，不是没有想到排序，就是感觉做起来有点奇怪，看了题解半天，原来是要判否执行，因为我一直在想是子文件了怎么还要加到ans列表当中，结果就没有做出来。

2023/2/9
一个中等的数据结构题，其实主要就是运用哈希表，根据题意编写各个函数就行，一次AK。

2023/2/10
今天的每日一题害没有做，把之前周赛有一个不会做的题做了出来。就是给了一个x轴，x轴上有奖品的位置都放在了数组arr中(一个位置上可能有几个奖品)，然后给你两个长度相同且为k的线段，看看最多能有多少个奖品在线段上。其实这个题有点两数之和的意思，就是不断的枚举第二个线段，然后看看在第二个线段的左端点的左边，能覆盖的最多的点数。并且需要不断的维护左边最大的覆盖点数。    
for right, p in enumerate(prizePositions):
        while p - prizePositions[left] > k:
            left += 1
        ans = max(ans, right - left + 1 + pre[left])
        pre[right + 1] = max(pre[right], right - left + 1)
 精简的代码放在这里。

2023/2/11
一个简单题，草了没有做出来，因为有个分类讨论的情况，我没有分类出来，只考虑了大部分情况，有极端情况需要判断但是没有找出来。

2023/2/13
今天也是一个中等题，关于同向双指针，但是没有做出来，没有看出来方法而且主要没有找到题目解题关键“替换子串之外的任意字符的出现次数都不超过 m，那么可以通过替换，使s为平衡字符串，即每个字符的出现次数均为m”，主要是这里没看出来导致没有做出来。

2023/2/14
今天的中等题还是没有做出来，我一看求最长的距离还以为是双指针，结果是前缀和+单调栈。「劳累天数大于不劳累天数」等价于「劳累天数减去不劳累天数大于0」。那么把劳累的一天视作nums[i]=1，不劳累的一天视作nums[i]=−1，则问题变为：计算nums，nums的最长子数组，其元素和大于0。这时候记录一个递减的单调栈，从后往前找出大于栈顶的前缀和元素再记录就行。

2023/2/16
简单题，一次AK。

2023/2/17
今天是一个图类的问题，但是我以为是用的是深度优先，其实就是一个二维数组的前缀和，倒叙遍历最大的dist=min(row,col),遍历坐标(grid.length-dist,grid[0].length-dist),如果有全部都是1的直接返回dist*dist。

2023/2/19
今天是一个中等题，但是没有做出来。一开始我是通过数学公式来分析怎么样才能让整个分式变得最大，我想要通过增量来进行判断，但是通过增量来进行判断之后我就不知道该怎么样才能在比较简单的时间复杂度下面完成代码。看完题解之后题解也是通过增量来进行判断，但是采用大根堆，其次就是python类当中有个__It__的方法，用来进行比较复杂的比较，返回一个对象，这时候用大根堆当中的heapreplace来进行。

2023/2/20
今天一个简单题，使用python当中的any迭代工具可以方便的写出来。

2023/2/22
今天这个题感觉好像是之前做过但是没有做出来就放着了。没有用到要用后缀和来表示石子堆的数量，然后就是记忆化搜索。

2023/2/24
一个简答题，差点做复杂了，相当于消积木，判断他有几个台阶，如果有0台阶减1就行了.

2023/2/25
一个中等题，没有做出来，给定两个字符串s1和s2(只含有x和y并且只能在s1和s2字符串之间交换字符)，判断最少需要交换多少次。给定两个模式，s1[i]=y,s2[i]=x称为yx,反之称为xy。可以通过一次交换，使得xy或yx的值减少2。通过两次交换xy和yx的值各减少1。这样就能得到返回值了。

2023/2/26
今天是一个hard，第一眼感觉就该用回溯法，但是感觉代码有点写不出来，因为我看数据量比较小，最后果真是用回溯法，相比于中等题的回溯法，这个回溯法就用需要用到Counter，并且要判断每一个word是否能被减掉，如果能减掉的话呢就加上分数，减不掉就要撤销。

2023/2/27
寄，今天这个又没做出来。给你一个整数数组 nums，每次操作会从中选择一个元素并 将该元素的值减少 1，让整个数组成锯齿状。要考虑到先考虑单个偶数和单个奇数，是不会对最终结果有影响的，就考虑每一个元素在当前位置都是最大值，让左右两边元素减，减去的数加到返回值中，最后比较返回就行了。

2023/3/6
真是失败。今天这个中档题就是给定一个字符串，只包含ab，然后可以删除字符串，判断最少删除多少次能够让全部a在b的左侧。一开始我以为是通过defaultdict(list)来记录每一个a和b的位置然后找最大的a在b[0]的左边然后最大的b在a[0]的右边，但是这样会漏情况，因为有可能在左边要删除一些b在右边要删除一些a。题解是用枚举+前缀和，维护一个leftB和rightA，min(res，leftb+righta)。

2023/3/8
今天是一个中等题目，总感觉在哪里做过，一次AK。

2023/3/11
今天一个中等题没有做出来。给定的是一个list，里边装的是数字和字母，需要计算出最长的子数组，里面数字和字母的数量相等。用前缀和+哈希表。前缀和一开始为0，遇到数字就-1，需要字母就加1，这时候就把问题转化成了对于给定list，求相同首尾数字的最长的长度。

2023/3/15
一个中等题，我看数据没多少，直接把maps从给的列表当中分割出来，然后遍历每一对节点，返回res就行。

2023/3/19
关于搜索解的问题，想到了改用BFS但是BFS真心不会写，还要多多练习。

2023/3/20
数位DP太难了，虽然说有模板但是自己写还是写不出来，而且看到题也没有什么思路。

2023/3/23
今天一个中等题，给了一个arr和两个分别是lefts和rights的list，让你求[left,right]区间是否是等差数组。每次单个的查询我只能想到n^2*logn,但是用哈希表直接优化到O(n)，这样就不用进行排序了。因为等差数组每次对dist整除后都是0、1、2这种连续整数，只要在list当中就没法称为等差数列了，这样就可以了。

2023/3/25
今天一个中等题，给定一个无序数组，求删除最短元素使得数组有序。使用双指针，先让right找到一个位置，让arr[right-1]>arr[right],此时right和right-1就要分成两组了，然后不断枚举left，看看arr[left]<=arr[right],如果是的话就可以缩短一个位置，不然就right+1往后找，像一个有穷自动机一样慢慢给它找完。其实还挺复杂的，建议看一看题解1574。

2023/4/3
好久没有写题解了，今天做的是一个中等题，给定一个全是str类型的数字的arr，让你求交换下标i和j交换之后小于原数组字典序的最大排列。这个题就是要从逆序寻找a[i]>a[i+1]，这样可以保证小于原来的字典排序，然后从小于i到len(arr)之间找最大的数字，这样就可以保证最大排序，值得注意的是在保证最大排序的时候也要保证最左，就是arr[j]>=temp，如果只是>temp是没有保证最左的。

2023/4/6
今天也是一个进制转换，转为-2进制表示，和转为2进制不同的是，-2进制表示会出现余数0 1 和-1，出现-1的时候，要转为它的绝对值加到返回答案当中，此时n更新为n=n//(-2)+1，其他和正常转进制就行了。

2023/4/10
今天这个题看出来了是用单调栈，但是有点细节部分没有写对，每个返回值当中总是有几个值统计不对，最近实在太忙了就没研究直接看题解了。

2023/4/15
今天这个有点像给地图染色的问题，但是没有做出来，学会了一个小trick，就是python当中可以set相减来获得不一样的值，利用这个特性来选取颜色。

2023/5/5
好久没有写题解了，而且刚刚放完假，隔了好久终于写了一个题了，不过是一个简单题而且是以前做过的，easy。

2023/5/15
今天是一个中等题，题目简直字字珠玑，明明可以说翻转任何一个数字题目说每一列，我还以为要转就必须转每一列上的所有数字，虽然但是就算改了也可能做不出来，加油吧。

2023/5/17
一个简单题，对于时间的处理可以通过转换成数字处理，比如01:15==1*60+15这样就可以判断交集了。

2023/5/25
一个字符串的简单题，配合defaultdict就能写出来。

2023/5/30
今天是一个和树相关的题。题目大意是返回一个List[TreeNode]的列表，列表里面装的是原来Root头节点当中删除以后形成的森林，题目是1110，具体可以看看题目，一开始打算是用广度优先看看能否遍历出来，但是遇到一个问题，就是我广度优先不能添加每一个节点然后就卡住了，题解是用深度优先遍历，只加入删除的位置（其实就是新的头节点），当时就是这个点没有想通，其实用广度优先应该也能做出来。

2022/5/31
给定一个数组arr，里面存放的数字是一颗只有0儿子和2儿子组成的二叉树，相当于arr里面全部都是叶子节点的值，非叶子节点的值是由2个叶子节点的值相乘，问这棵树最小的非叶子节点和，这个题我一开始还以为是哈夫曼树，最后题解用的单调栈确实太妙了，单调栈是一个严格递减的stack，判断当前arr的x，先让stack出栈一个y，判断stack是否为空或者是否stack[-1]>x，如果大于x那么res+=y*x,否则的话就让stack[-1]=stack[-1]*y，然后y不要，因为此时y是stack[-1],x,y当中最大的数字，但是不管最后怎么样都是要把x添加到栈中，这样求出来一棵树，O(N)完成确实太妙了。

2023/6/1
今天这个题学会了一个二分查找的模板，以前写二分查找都是mid等于target，mid<target，mid>target，今天这个模板只有大于和小于mid==(left+right+1)，然后这个题转换一下就是给定一个数字k和一个数字，找出这个数组里面包含k个的子序列，这个子序列要任意两个数绝对值之差最小，用的是贪心+二分查找，具体的可以看2517。

2023/6/6
今天一个中等题，给定一个二维数组，判断二维数组中行数组与列数组到底有几个是相等的。其实用哈希表就可以做出来，只是做一点变换，把数组[1,2,3]变成"[1,2,3,]"就是简单的字符串拼接。

2023/6/7
今天一个中等题，给定了两个数组arr1，arr2，选择arr1中的k个，其他全部选择arr2，使得整体得分数最大。这个题我竟然做出来了，我的做法是，先计算他们两个得差值，找性价比最高，因为选了arr1的元素后就不能选arr2了，然后在对差值数组进行索引逆排序，这样取索引数组中的前K个，然后其他全部取arr2中的就能算出最大值了。

2023/6/11
今天这个题题解简直是绝妙我草，题是1171，题意是给定一个链表，然后反复删除掉链表里面相加等于0的节点。一开始我的想法也是用哈希表，但是我的想法仔细想了想完全不可取，然后就跑偏了。题解是用哈希表，不断存储前缀和和节点，建立map(val->node)的哈希表，然后第二次遍历的时候，直接不断地查找跟当前前缀和一样的节点就行了，比如说当前前缀和是2，然后节点是A，然后哈希表里存储的也有2然后节点是B，说明A->B中间这一段的链表里面加起来和都为0，所以直接A.next=B.next就行了，太妙了。

2023/6/14
今天是1375题，题意是给你一个数组，然后给你一个全为0的二进制数，按照数组arr里面的元素值进行二进制位的翻转，每当[0,L]全部翻转时，要返回的值+1。一开始我还以为是一个位运算，每次都把arr元素给他与到seen上，判断seen==2**index，但是没想到最后一个例子超时了。看完题解之后发现，原来是维护一个right变量，这个变量在每一次的遍历当中都要与arr[i]进行比较，保证right最大，然后不停的比较当前遍历的位置和right，如果相当返回值就+1。

2023/6/29
好久没有写题解了，今天是1253题，大致题意就是给你两个数字upper和lower还有一个一维数组colsum，然后让你返回一个二位数组（这个二维数组是2进制，只有1和0），然后upper和lower分别代表了第一行和第二行的1的个数，colsum是每一列的和，问你怎么才能把这个数组给推出来。这个题没想到我缝缝补补还过了，我就是用的贪心算法，colsum只会有3个值，分别为0，1，2。是0的时候非常好说，两个位置都应该填0，是2的时候也好说，两个位置都应该填1，但是是1的时候就要判断一下，让upper和lower当中大的那个数字先用，最后再做两个特判就能出来了。

2023/7/6
今天一个中等题没有做出来，就是给定一个整数，求出这个数字的偶数组和（就是一个数组里面全是偶数然后和是等于这个数字），如果这个数字找不出来就返回空数组。一开始我想用贪心，但是想了想会有贪心找不出来的情况，于是方向就歪了我就去写回溯果然超时了，后面看题解我发现我忽略了一个性质，就是贪心找到最后一个是数字，如果比他大，反正也是偶数直接加到数组最后一个数字这样他也满足了要求，这样做的话时间O(根号2)就做出来来。

2023/7/8
今天是一个中等题，就是给你一个非递减的数组，再给你一个target，要找到数组当中两个数字相加等于target，利用非递减的性质直接用双指针做出来。

2023/7/18
今天是一个困难题，已经很久没有碰过困难题了，今天是1851，给定一个二维数组[[left1,right1],[left2,right2],...[left_n,right_n]],然后再给定一个数组queries，查询queries当中在二维数组区间内最短的区间长度。用的是优先队列加缩影排序（也要对二维数组排序，按左端点排序），然后不停的判断是否在当前二维数组的左端点上，直到循环结束，然后再不停的剔除大于右端点的部分，最后按照索引给ans赋优先队列的第一个元素。

2023/7/27
真是笨了，今天一个简单题竟然没写出来，就是一个排序+最大值和就能做出来第2500题。

2023/7/31
今天是143题，重排链表将L1,L2,...,Ln排列成L1,LN,L2,LN-1,...这样，可以看灵山茶的视频，就是用快慢指针找中间节点然后反转中间节点后面的链表依次插入。

2023/8/1
今天是2681hard题目，给定一个无序的数组，要求求出数组所有的英雄力量和，英雄力量和是每个子序列最大值**2乘最小值得到，这样的话可以先将数组排序，排序后用一个数组记录每一次当前num[index]最为最大值，他的所有子序列的最小值的和，用O(N)的时间复杂度就能做出来。

2023/8/22
今天849题，题意其实大概就是男厕所选尿池的意思，找一个距离两边都最远的位置，但是一开始没有做出来，用双指针，每次都找两个坑位，然后找中间的位置和ans比较进行更新，最后就是要加入考虑一种边界情况就行。

2022/9/9
今天是207中等题，虽然我看出来了是搜索拓扑排序但是不知道怎么写，总算是学习了一下了，详解可以看207题解。

23/11/18
今天是2342题，一个中等题，用一个比较优雅的写法写了出来，O(N)+不断贪心就做出来了，以后还是别写题解了，感觉写了也没什么用，嘻嘻！
