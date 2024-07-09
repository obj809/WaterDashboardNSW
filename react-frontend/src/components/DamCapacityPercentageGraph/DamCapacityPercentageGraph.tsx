// src/components/DamCapacityPercentageGraph/DamCapacityPercentageGraph.tsx

import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';
import './DamCapacityPercentageGraph.scss';

Chart.register(...registerables);

interface DamCapacityPercentageGraphProps {
    data: any[];
}

const getColor = (index: number) => {
    const colors = [
        '#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
        '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
        '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
        '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
        '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
        '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
        '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
        '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
        '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
        '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'
    ];
    return colors[index % colors.length];
};

const DamCapacityPercentageGraph: React.FC<DamCapacityPercentageGraphProps> = ({ data }) => {
    const labels = Array.from(new Set(data.map(d => d.date))).sort();
    const dams = Array.from(new Set(data.map(d => d.dam_id)));
    const damNamesMap = data.reduce((acc, curr) => {
        acc[curr.dam_id] = curr.dam_name;
        return acc;
    }, {} as Record<string, string>);

    const datasets = dams.map((dam_id, index) => {
        const damData = data.filter(d => d.dam_id === dam_id);
        return {
            label: damNamesMap[dam_id],
            data: labels.map(label => {
                const entry = damData.find(d => d.date === label);
                return entry ? entry.percentage_full : null;
            }),
            fill: false,
            borderColor: getColor(index),
            backgroundColor: getColor(index),
            tension: 0.1
        };
    });

    const chartData = {
        labels,
        datasets
    };

    const options = {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Date',
                    font: {
                        size: 18
                    }
                },
                ticks: {
                    maxRotation: 45,
                    minRotation: 45,
                    font: {
                        size: 14
                    }
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Percentage Full',
                    font: {
                        size: 18
                    }
                },
                ticks: {
                    beginAtZero: true,
                    font: {
                        size: 14
                    }
                }
            }
        },
        plugins: {
            title: {
                display: true,
                text: 'Dam Capacity Percentage Over Last 12 Months',
                font: {
                    size: 24
                }
            },
            legend: {
                display: true,
                position: 'top' as 'top',
                labels: {
                    font: {
                        size: 14
                    }
                }
            }
        },
        responsive: true,
        maintainAspectRatio: false
    };

    return (
        <div className="dam-capacity-percentage-graph-container">
            <Line data={chartData} options={options} />
        </div>
    );
};

export default DamCapacityPercentageGraph;
