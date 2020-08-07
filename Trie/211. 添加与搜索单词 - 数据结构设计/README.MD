Trie是用来搜索word的方法

在Python中我们可以用dict来build Trie，

1. 首先建一个空的dict起名叫lookup
2. 然后在add中把字母依次放入trie中，如果当前layer没有这个字母，那么就造一个新的空dict， 然后把新的空dict赋予tree，如果tree中有这个字母，那么把tree[e]赋给tree，完成层与层的交接
3. 在最后建一个新的dict，key是#， 内容为空，表示结束
4. 在search中，用递归来寻找word，本质是DFS
5. 建一个helper方程，先看base case，也就是没有word，说明到已经找过了最后一个字母，现在要找的是是否有以最后一个字母结尾的word，那么必然在这一层有一个以#为key的dict，如果有，返回True，没有返回False
6. 如果第一个单词是., 表示wildcard，那么我们需要遍历当前tree的所有元素，因为这个点可以表示任意字母，然后用这个字母的下一层和word[1:]在下一层进行递归，如果有True就返回True
7. 如果第一个单词不是点，而是正常字母，那么就看这个字母在不在tree中，如果在，那么进行下一轮的字母和tree的search，如果不在，直接返回False

