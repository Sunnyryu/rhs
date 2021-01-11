import React, { useState } from "react";
import ReactDOM from "react-dom";

import "./index.css";

const content = [
  {
    tab: "Section 10",
    content: "I`m the content of the Section 1"
  },
  {
    tab: "Section 20",
    content: "I`m the content of the Section 2"
  }
];
const useTabs = (initialTab, allTabs) => {
  //console.log(allTabs)
  const [currentIndex, setCurrentIndex] = useState(initialTab);
  if (!allTabs || !Array.isArray(allTabs)) {
    return;
  }
  //console.log(initialTab)
  //console.log(allTabs)
  console.log(allTabs[currentIndex], initialTab)
  //console.log(currentIndex)
  return {
    currentItem: allTabs[currentIndex],
    changeItem: setCurrentIndex
  };
};

const App = () => {
  //console.log(content)
  const { currentItem, changeItem } = useTabs(1, content);
  //console.log(currentItem)
  console.log(changeItem)
  return (
    <div className="App">
      {content.map((section, index) => (
        <button onClick={() => changeItem(index)}>{section.tab}</button>
      ))}
      <div>{currentItem.content}</div>
    </div>
  );
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
