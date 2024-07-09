// src/graphs/DamStorageGraph/DamStorageGraph.tsx

import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';
import './DamStorageGraph.scss';

Chart.register(...registerables);

interface DamStorageGraphProps {
    data: any[];
}

const DamStorageGraph: React.FC<DamStorageGraphProps> = ({ data }) => {
    const labels = data.map(d => d.dam_name);
    const storageVolumes = data.map(d => d.storage_volume);

    const chartData = {
        labels,
        datasets: [
            {
                label: 'Storage Volume (ML)',
                data: storageVolumes,
                backgroundColor: '#5274EA',
                borderColor: 'rgb(54, 162, 235)',
                borderWidth: 1
            }
        ]
    };

    const options = {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Dam Name',
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
                    text: 'Storage Volume (ML)',
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
                text: 'Dam Storage Capacity',
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
        <div className="dam-storage-graph-container">
            <Bar data={chartData} options={options} />
        </div>
    );
};

export default DamStorageGraph;
