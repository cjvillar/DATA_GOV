import Chart from "chart.js/auto";
import { CategoryScale } from "chart.js";
import { useState } from "react";
import PieChart from "./PieChart";
import { BarChart } from "./BarChart";
import LineChart from "./LineChart";
import DoughnutChart from "./DoughnutChart";
import PolarAreaChart from "./PolarChart";
import Data from "./shark_incidents.json";

import "./style.css";

Chart.register(CategoryScale);

//get keys in json
const allKeys = Data.reduce((keys, entry) => {
  Object.keys(entry).forEach(key => {
    if (!keys.includes(key)) {
      keys.push(key);
    }
  });
  return keys;
}, []);

//produce random hex code
function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

export default function App() {
  const [selectedKey, setSelectedKey] = useState(allKeys[5]); //set default key for shark data use index 5
  const [counts, setCounts] = useState({});
  const [chartData, setChartData] = useState({
    labels:  Object.keys(counts),
    datasets: [
      {
        label: 'Data',
        data: Object.values(counts),
        backgroundColor: [],
        borderColor: 'black',
        borderWidth: 2,
      },
    ],
  });

  const handleSelectionChange = (event) => {
    const newSelectedKey = event.target.value;

    //update selected key
    setSelectedKey(newSelectedKey);

    //recalculate counts based on the new selected key
    const newCounts = {};
    Data.forEach(function (item) {
      const dataKey = item[newSelectedKey];
      newCounts[dataKey] = (newCounts[dataKey] || 0) + 1;
    });

    //update counts state
    setCounts(newCounts);

    // update chart data
    const newBackgroundColors = Array.from({ length: Object.keys(newCounts).length }, () =>
      getRandomColor()
    );

    setChartData({
      labels: Object.keys(newCounts),
      datasets: [
        {
          label: 'Data',
          data: Object.values(newCounts),
          backgroundColor: newBackgroundColors,
          borderColor: 'black',
          borderWidth: 2,
        },
      ],
    });
  };

  return (
    <div className="App">
      <div classNAme="dataSelection">
        <select className="dataKeys" onChange={handleSelectionChange} value={selectedKey}>
          {allKeys.map((key, index) => (
            <option className="data-items" key={index} value={key}>
              {key}
            </option>
          ))}
        </select>
      </div>
      <PolarAreaChart chartData={chartData} />
      <DoughnutChart chartData={chartData} />
      <PieChart chartData={chartData} />
      <BarChart chartData={chartData} />
      <LineChart chartData={chartData} />
    </div>
  );
}