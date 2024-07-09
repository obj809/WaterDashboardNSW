// src/pages/PageFour/PageFour.tsx

import React, { useEffect, useState } from 'react';
import FigureBox from '../../components/FigureBox/FigureBox';
import { fetchAvgPercentageFull12Months, fetchAvgPercentageFull5Years, fetchAvgPercentageFull20Years } from '../../services/api';
import './PageFour.scss';

const PageFour: React.FC = () => {
    const [avg12Months, setAvg12Months] = useState<string | null>(null);
    const [avg5Years, setAvg5Years] = useState<string | null>(null);
    const [avg20Years, setAvg20Years] = useState<string | null>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data12Months = await fetchAvgPercentageFull12Months();
                setAvg12Months(data12Months.toFixed(2) + '%');

                const data5Years = await fetchAvgPercentageFull5Years();
                setAvg5Years(data5Years.toFixed(2) + '%');

                const data20Years = await fetchAvgPercentageFull20Years();
                setAvg20Years(data20Years.toFixed(2) + '%');
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div className="page-four">
            <div className="figure-box-container">
                <FigureBox title="Average Percentage Full (12 Months)" data={avg12Months} />
                <FigureBox title="Average Percentage Full (5 Years)" data={avg5Years} />
                <FigureBox title="Average Percentage Full (20 Years)" data={avg20Years} />
            </div>
        </div>
    );
};

export default PageFour;
