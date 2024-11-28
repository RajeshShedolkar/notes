useCallback is a hook that memoizes a function, preventing it from being recreated on every render. Here’s an example in two lines:

```
const memoizedCallback = useCallback(() => { doSomething(a, b); }, [a, b]);
```
In this code, memoizedCallback will only change if a or b changes, helping to optimize performance by avoiding unnecessary re-creations of doSomething.
