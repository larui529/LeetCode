## Backtracking — quick interview cheat-sheet

Goal: enumerate combinations/permutations/subsets/paths using a small, repeatable pattern you can recall in an interview.

Core pattern (fast checklist):
- Create `res = []` to collect answers.
- Create a working container `path` (or `selected`) to hold the current partial solution.
- Write a helper `bk` / `dfs` that takes a position parameter (usually `start` or indices/counts).
- Base case: when the stopping condition is met, append a copy of `path` (or the constructed string) to `res` and return.
- Loop/Choices: iterate possible next choices; for each choice:
	1. append the choice to `path` (or mark used)
	2. recurse (`bk(next_index, ...)`)
	3. pop/unmark to restore state
- Call `bk(0, ...)` (or `bk(initial_state)`) and return `res`.

One-line memory mantra: "res, path, bk(start) — append, recurse, pop." Say it once and implement it.

Uniform Python template (standard variable names you can reuse):

```python
def solve(nums):
		res = []
		path = []

		def bk(start: int) -> None:
				# record current answer (copy)
				res.append(path.copy())
				for i in range(start, len(nums)):
						path.append(nums[i])
						bk(i + 1)          # or bk(i) if reuse allowed (e.g. combinationSum)
						path.pop()

		bk(0)
		return res
```

Common small variations (be ready to adapt):
- Reuse allowed (infinite picks): call `bk(i)` instead of `bk(i+1)`.
- Permutations: track `used = [False]*n`, iterate all indices, skip used ones.
- Fixed-length combinations: use `if len(path) == k: res.append(path.copy()); return`.
- Constructed strings (e.g. parentheses): keep `path` as a list of chars and `res.append(''.join(path))`.
- Grid/word DFS: helper `dfs(r,c,i)` with in-place mark or `visited` set; return boolean if any path finds the target.

Edge tips for interviews:
- Verbally state your invariant: what `path` means and why you append/pop.
- Mention pruning: sort input to early-break when sum/limit exceeded.
- Reuse the same variable names (`res`, `path`, `bk`/`dfs`, `start`) across problems so your mental template is stable.
- For performance, explain complexity briefly (output size often dominates).

Minimal checklist to run through after writing code:
1. Did I append a copy of `path` (not `path`) to `res`?  
2. Did I restore state after recursion (pop/unmark)?  
3. Are base conditions correct (len/path/indices)?  
4. Any needed pruning or sorting?

Keep this README short — practice writing the template from memory until it becomes second nature.