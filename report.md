# Assignment 1 - Big Data Systems

Ankur Goswami -- agoswami6@wisc.edu
Yunjia Zhang -- yunjia@cs.wisc.edu

## PageRank Analysis

### Task 1 Results

| Task    | Small | Large |
|---------|-------|-------|
| Runtime | 3.5m  | 1h6m  |

Our program is completed and looks to be correct. These will be our baselines speeds.

### Task 2 Small Results

| Partitions | 5    | 10   | 20   |
|------------|------|------|------|
| Runtime    | 3.5m | 3.4m | 2.2m |

We see that as we increase the partitions, we see a consistent speedup. The jump between 10 and 20 partitions
causes a speedup of 1.2 minutes, while the jump from 5 partitions to 10 partitions causes a 0.1 minute speedup.

Takeaway: For small data tasks, where the task graph is small, increasing partitions induces minimal overhead and
gives good speedups.

### Task 2 Large Results

| Partitions | 500  | 700   |
|------------|------|-------|
| Runtime    | 1h6m | 1h12m |

We see that increasing the partitions from 500 to 700 for the large data task gives us
a *slowdown* of 6 minutes.

Takeaway: For large data tasks, increasing partitions from an already high value to a higher value
can reduce execution speed because the task graph grows larger and there is larger
scheduler overhead.

### Task 3 Small Results

| In memory persistence | False | True |
|-----------------------|-------|------|
| Runtime               | 3.5m  | 2.9m |

### Task 3 Large Results

| In memory persistence | False | True |
|-----------------------|-------|------|
| Runtime               | 1h6m  | 56m  |

We see consistent results for both the small and large tasks. There is a 0.6 minute
speedup for the small task and a 10 minute speedup for the large task, suggesting
that persisting RDD objects in memory gives up to 17% speedup.

Takeaway: Persisting RDD objects in memory wherever possible leads to significant
speedups.

### Task 4 Small Results

| Killed Worker | False | True |
|---------------|-------|------|
| Runtime       | 3.5m  | 3.6m |

Only a 0.1 minute overhead is incurred by killing the worker. This is a very
small cost.

Takeaway: In small task graphs, not a lot of things need to be recomputed
if a worker dies, so the overhead from a worker dying is minimal.

### Task 4 Large Results

| Killed Worker | False | True  |
|---------------|-------|-------|
| Runtime       | 1h6m  | 1h12m |

We see that killing the worker causes a 6 minute slowdown. This is because
all operations on the partition loaded in the Worker must be recomputed. Still,
6 minutes is less than 10% of the total execution time, suggesting that
recovery overhead is not severe.

Takeaway: For large datasets with a large number of partitions, recovering
from a single killed worker can induce minimal overhead.

## Work allocation

Ankur wrote the code for Part 2. Yunjia wrote the code for Part 3. Ankur wrote the
analysis of results from Part 3.
