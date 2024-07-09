// src/components/NetInflowReleaseGraph/NetInflowReleaseGraph.tsx

import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

interface NetInflowReleaseGraphProps {
    data: any[];
}

const NetInflowReleaseGraph: React.FC<NetInflowReleaseGraphProps> = ({ data }) => {
    const labels = data.map(d => d.date);
    const inflows = data.map(d => d.storage_inflow);
    const releases = data.map(d => d.storage_release);
    const netFlows = inflows.map((inflow, index) => inflow - releases[index]);

    const chartData = {
        labels,
        datasets: [
            {
                label: 'Net Inflow/Release',
                data: netFlows,
                fill: false,
                borderColor: 'rgb(255, 99, 132)',
                tension: 0.1
            }
        ]
    };

    return (
        <div>
            <h2>Net Inflow or Release Over 12 Months</h2>
            <Line data={chartData} />
        </div>
    );
};

export default NetInflowReleaseGraph;
