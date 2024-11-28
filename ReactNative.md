# React Native Core Concepts

## 1. **Components**
   - Components are the building blocks of a React Native app.
   - They are reusable pieces of UI, like buttons or text fields, that make up your app's interface.
   - There are two types:
     - **Functional Components**: Written as functions, often simpler and easier to read.
     - **Class Components**: Written as ES6 classes, used when you need more features like lifecycle methods.

## 2. **JSX (JavaScript XML)**
   - A syntax extension that allows you to write HTML-like code directly in JavaScript.
   - Makes it easier to visualize and design the UI.
   - Example:
     ```javascript
     <Text>Hello, World!</Text>
     ```

## 3. **State**
   - An object that holds data for a component.
   - Changing a component's state will re-render the component with updated data.
   - Example: If a button is clicked, the state can be updated to show a new message.

## 4. **Props (Properties)**
   - Data passed from one component to another.
   - Allows components to communicate with each other.
   - Example: A parent component can pass user data as props to a child component for display.

## 5. **Styling**
   - Styling in React Native uses a syntax similar to CSS but is defined in JavaScript objects.
   - Common styles like `flex`, `padding`, and `color` are available to design layouts.

## 6. **Navigation**
   - Handles moving between different screens in an app.
   - Common libraries like React Navigation provide pre-built navigators (e.g., Stack, Tab).

## 7. **APIs and Fetching Data**
   - React Native apps can use APIs to interact with external data sources.
   - Fetching data is often done with the `fetch()` function or libraries like Axios.

## 8. **Lifecycle Methods (for Class Components)**
   - Specific methods that run at different stages of a component's existence.
   - Examples include `componentDidMount()` (runs after component mounts) and `componentWillUnmount()` (runs before it is removed).

## 9. **Hooks (for Functional Components)**
   - Special functions like `useState` and `useEffect` that allow functional components to manage state and lifecycle events.
   - `useState` creates state in functional components.
   - `useEffect` runs code at specific times, like when a component mounts or a variable changes.

## 10. **Native Modules**
   - Allow you to use native code (Java, Swift, etc.) within a React Native app for platform-specific features.
   - Useful for accessing hardware features like the camera or sensors.
