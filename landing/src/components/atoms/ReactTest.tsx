import { useState } from "react";

export function ReactTest() {
  const [count, setCount] = useState(0);

  return (
    <div className="p-8 border-2 border-gray-300 rounded-lg text-center bg-gray-50 shadow-md">
      <h2 className="text-2xl font-semibold mb-4 text-gray-800">React is Ready!</h2>
      <p className="text-lg text-gray-600 mb-6 font-mono">Current count: <span className="text-blue-600 font-bold">{count}</span></p>
      <button 
        onClick={() => {
          console.log("Button clicked!");
          setCount(count + 1);
        }}
        className="px-6 py-3 text-lg font-medium text-white bg-blue-600 hover:bg-blue-700 active:bg-blue-800 rounded-lg cursor-pointer transition-colors duration-200"
      >
        Click me to increment
      </button>
    </div>
  );
}
