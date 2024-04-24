The React useMemo Hook returns a memoized value.

Think of memoization as caching a value so that it does not need to be recalculated.


Performance
The useMemo Hook can be used to keep expensive, resource intensive functions from needlessly running.

we have an expensive function that runs on every render.

When changing the functionality, you will notice a delay in execution.

To fix this performance issue, we can use the useMemo Hook to memoize the expensive function. This will cause the function to only run when needed.

Syntax:
```
const fn = useMemo(() => expensiveCalculation(count), [count]);

fn()
```
useMemo will only recompute the memoized value when one of the deps has changed.

Note: The useMemo and useCallback Hooks are similar. The main difference is that useMemo returns a memoized value and useCallback returns a memoized function. You can learn more about useCallback 
