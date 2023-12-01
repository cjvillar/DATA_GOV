import React from "react";
import { PolarArea } from "react-chartjs-2";

function PolarAreaChart({ chartData }) {
  return (
    <div className="chart-container">
      <h2 style={{ textAlign: "center" }}>Doughnut Chart</h2>
      <PolarArea
        data={chartData}
        options={{
          plugins: {
            title: {
              display: true,
              text: "place holder text"
            }
          }
        }}
      />
    </div>
  );
}
export default PolarAreaChart;