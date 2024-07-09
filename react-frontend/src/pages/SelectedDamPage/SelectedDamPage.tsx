// src/pages/SelectedDamPage/SelectedDamPage.tsx

import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { 
    fetchDamDataByName, 
    fetchDamResources,
    fetchAvgPercentageFull12MonthsById,
    fetchAvgPercentageFull5YearsById,
    fetchAvgPercentageFull20YearsById
} from '../../services/api';
import DamContent from '../../components/DamContent/DamContent';
import GoogleMapComponent from '../../components/GoogleMapComponent/GoogleMapComponent';
import DamCapacityGraph from '../../components/DamCapacityGraph/DamCapacityGraph';
import NetInflowReleaseGraph from '../../components/NetInflowReleaseGraph/NetInflowReleaseGraph';
import './SelectedDamPage.scss';

const SelectedDamPage: React.FC = () => {
    const location = useLocation();
    const navigate = useNavigate();
    const [damData, setDamData] = useState<any>(location.state?.damData);
    const [damResources, setDamResources] = useState<any[]>([]);
    const [avgPercentageFull12Months, setAvgPercentageFull12Months] = useState<number | null>(null);
    const [avgPercentageFull5Years, setAvgPercentageFull5Years] = useState<number | null>(null);
    const [avgPercentageFull20Years, setAvgPercentageFull20Years] = useState<number | null>(null);

    useEffect(() => {
        if (!damData && location.state?.damName) {
            const loadDamData = async () => {
                try {
                    const data = await fetchDamDataByName(location.state.damName);
                    setDamData(data);
                } catch (error) {
                    console.error('Error fetching dam data:', error);
                }
            };

            loadDamData();
        }
    }, [damData, location.state?.damName]);

    useEffect(() => {
        if (damData) {
            const loadDamResources = async () => {
                try {
                    const resources = await fetchDamResources(damData.dam_id);
                    setDamResources(resources);
                } catch (error) {
                    console.error('Error fetching dam resources:', error);
                }
            };

            const loadAvgPercentageFullData = async () => {
                try {
                    const avg12Months = await fetchAvgPercentageFull12MonthsById(damData.dam_id);
                    setAvgPercentageFull12Months(avg12Months);

                    const avg5Years = await fetchAvgPercentageFull5YearsById(damData.dam_id);
                    setAvgPercentageFull5Years(avg5Years);

                    const avg20Years = await fetchAvgPercentageFull20YearsById(damData.dam_id);
                    setAvgPercentageFull20Years(avg20Years);
                } catch (error) {
                    console.error('Error fetching average percentage full data:', error);
                }
            };

            loadDamResources();
            loadAvgPercentageFullData();
        }
    }, [damData]);

    if (!damData) {
        return <div>Loading...</div>;
    }

    const handleBackClick = () => {
        navigate('/');
    };

    const latitude = parseFloat(damData.latitude);
    const longitude = parseFloat(damData.longitude);

    return (
        <div className="selected-dam-page">
            <button className="back-button" onClick={handleBackClick}>Back</button>
            <div className="dam-header">
                <h1>{damData.dam_name} Insights</h1>
            </div>
            <div className="content-row">
                <div className="dam-content">
                    <DamCapacityGraph data={damResources} />
                </div>
                <div className="dam-content">
                    <NetInflowReleaseGraph data={damResources} />
                </div>
            </div>
            <div className="content-row">
                <DamContent content="">
                    <div>
                        <p>Average Percentage Full Over 12 Months: {avgPercentageFull12Months !== null ? avgPercentageFull12Months.toFixed(2) + '%' : 'Loading...'}</p>
                        <p>Average Percentage Full Over 5 Years: {avgPercentageFull5Years !== null ? avgPercentageFull5Years.toFixed(2) + '%' : 'Loading...'}</p>
                        <p>Average Percentage Full Over 20 Years: {avgPercentageFull20Years !== null ? avgPercentageFull20Years.toFixed(2) + '%' : 'Loading...'}</p>
                    </div>
                </DamContent>
                <div className="dam-content">
                    <GoogleMapComponent lat={latitude} lng={longitude} />
                </div>
            </div>
        </div>
    );
};

export default SelectedDamPage;
