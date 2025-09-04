// src/graphs/DamCapacityGraph/DamCapacityGraph.tsx

import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

interface DamCapacityGraphProps {
    data: any[];
    damName: string;
}

const DamCapacityGraph: React.FC<DamCapacityGraphProps> = ({ data, damName }) => {
    const labels = data.map(d => d.date);
    const percentages = data.map(d => d.percentage_full);

    const chartData = {
        labels,
        datasets: [
            {
                label: 'Dam Capacity Percentage',
                data: percentages,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }
        ]
    };

    return (
        <div style={{ textAlign: 'center' }}>
            <h2>{damName} Capacity Percentage Over 12 Months</h2>
            <Line data={chartData} options={{ maintainAspectRatio: false }} />
        </div>
    );
};

export default DamCapacityGraph;
