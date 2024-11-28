The useEffect hook in React allows you to perform side effects in function components, like data fetching or setting up a subscription.  
```
import React, { useEffect } from 'react';

useEffect(() => {
  console.log("Component mounted or updated");
  return () => console.log("Cleanup on unmount or dependencies change");
}, []);

```

Explanation
The callback inside useEffect runs when the component mounts or when dependencies (the array after the comma) change.
[] as the dependency array makes it run only once on mount.
The function returned from useEffect is called when the component unmounts or dependencies change, making it ideal for cleanup.
