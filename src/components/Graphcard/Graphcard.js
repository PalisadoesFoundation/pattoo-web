/* React Imports */
import React from "react";
import { Line } from "react-chartjs-2"
import "../../styles/main.css";

//consider Apexcharts for graphs if chart.js presents problems
function GraphCard() {
    return (
       <div className="flex flex-col items-center rounded-md bg-white m-4 p-4 w-80 h-64 border shadow-lg">
            <Line
                data={{
                    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                    datasets:[{
                        label: "Number of Votes",
                        data: [12, 19, 3, 5, 2, 3],
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 2
                    }]
                }}
                height={500}
                width={600}
                options={{
                    maintainAspectRatio: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    },
                    legend:{
                        display: true,
                        labels:{
                            fontSize: 14
                        }
                    }
                }}
            
            />
       </div>
    );
}

export default GraphCard;