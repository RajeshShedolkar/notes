<dl>
<dt>What useContext() Hook is?</dt>
    <dd>
        <div>
        <p>
        useContext is react hook. useContext is the way to manage state globally.
        </p>
        <p>
        Without useContext, sharing state can be achieved using the useState hook. However, the way the useState hook works is not optimal. For example, if there are multiple nested components using the same state, it must be passed from one component to the next via properties.
        </p>
        </div>
    </dd>
<dt> 
</dl>

```html
import { useState } from "react";
import ReactDOM from "react-dom/client";

function Component1() {
  const [user, setUser] = useState("Jesse Hall");

  return (
    <>
      <h1>{`Hello ${user}!`}</h1>
      <Component2 user={user} />
    </>
  );
}

function Component2({ user }) {
  return (
    <>
      <h1>Component 2</h1>
      <Component3 user={user} />
    </>
  );
}

function Component3({ user }) {
  return (
    <>
      <h1>Component 3</h1>
      <Component4 user={user} />
    </>
  );
}

function Component4({ user }) {
  return (
    <>
      <h1>Component 4</h1>
      <Component5 user={user} />
    </>
  );
}

function Component5({ user }) {
  return (
    <>
      <h1>Component 5</h1>
      <h2>{`Hello ${user} again!`}</h2>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Component1 />);

```

<p>
In order to maintain the The solution is to create context.
</p>
<p>
Next we'll use the Context Provider to wrap the tree of components that need the state Context.

Context Provider
<b>Wrap child components in the Context Provider and supply the state value.</b>
</p>

```html
import { useState, createContext } from "react";
import ReactDOM from "react-dom/client";

const CustomContext = createContext()

export useSocket = () => {
  useContext(CustomContext)
}

export function customContextProvider() {
  const [user, setUser] = useState("Jesse Hall");

  return (
    <UserContext.Provider value={user}>
      <h1>{`Hello ${user}!`}</h1>
      <Component2 user={user} />
    </UserContext.Provider>
  );
}
```


