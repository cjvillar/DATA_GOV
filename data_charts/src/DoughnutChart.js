import React from "react";
import { Doughnut } from "react-chartjs-2";

function DoughnutChart({ chartData }) {
  return (
    <div className="chart-container">
      <h2 style={{ textAlign: "center" }}>Doughnut Chart</h2>
      <Doughnut
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
export default DoughnutChart;