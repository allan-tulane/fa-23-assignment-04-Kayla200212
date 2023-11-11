# CMPS 2200 Assignment 4
## Answers

**Name:**_kayla willis________________________


Place all written answers from `assignment-04.md` here for easier grading.

1a) To produce as few coins as possible to add to N, a greedy algorithm would have to constantly choose the largest option without exceeding N, like many examples we have seen in class the greedy algorithm will generally prefer the largest operation to perform as few operations as possible (or here, make as few coins). 

1b) For the greedy choice property to be true, the locally chosen solutions contribute and result in the globally optimal solution. The optimal substructure is proven true if we can show that the optimal solution also has optimal subproblems. Since we always pick the largest possible coin at each step, we are guaranteed to be reduced to a smaller subproblem and thus solve each subproblem optimally. This proves both properties to be true for this algorithm.

1c) Both work and span are O(logN) because each subproblem reduces N, our total, by a factor of 2. The algorithm continuously divides N by 2 so the times we go through the loop depends on how many times N can be divided by 2 and each step is constant work.

2a) The greedy algorithm wouldn't guarantee the smallest number of coins (or the most optimal solution) mainly because there is not a guaranteed even division of the currency conversion. example: if we have coins worth 1, 2, 7, and 8 and we had N=21, the greedy solution would do the following: 
21-8-8-2-2-1 giving us 2 coins of 8, 2 coins of 2, and 1 coin of 1 when the most optimal would be 3 coins of 7.

2b) a proof for this can be represented by c(n) for the min coins to make N. we use D_0, D_1...D_k for our denominations of the conversions so that we can know that the last coin is either the highest or not the highest denomination. If it's the highest, we have N-D_k remaining. If not, we check the next highest. this shows that the algorithm considers the optimal solution based on the optimal subproblems. 

2c) If we used memoization, we would simplify down to the worst case depending on N and the different conversion rates. The subproblems would be based on N, our total to be converted, multiplied by k, the conversion rates. The steps are independent in that once it completes a step, the total N is different and is put through the next step. This gives both a work and span of O(N*K) linear and dependent on the conversions we are given.