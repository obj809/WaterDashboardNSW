// src/pages/HomePage/HomePage.tsx

import React, { useState, useEffect } from 'react';
import TopDamsPieCharts from '../../containers/TopDamsPieCharts/TopDamsPieCharts';
import DamGroupSelector from '../../components/DamGroupSelector/DamGroupSelector';
import SearchForDam from '../../components/SearchForDam/SearchForDam';
import OpenListOfDams from '../../components/OpenListOfDams/OpenListOfDams';
import { fetchDamsDataByGroup } from '../../services/api';
import './HomePage.scss';

const HomePage: React.FC = () => {
    const [selectedGroup, setSelectedGroup] = useState<string>('sydney_dams');
    const [damData, setDamData] = useState<any[]>([]);

    useEffect(() => {
        const fetchDamData = async () => {
            const data = await fetchDamsDataByGroup(selectedGroup);
            setDamData(data);
        };

        fetchDamData();
    }, [selectedGroup]);

    return (
        <div className="homepage">
            <div className="header">
                <h1>Sydney Dam Monitoring</h1>
                <p>This website tracks live and historic data from the dams across NSW, Australia</p>
            </div>
            <div className="controls">
                <OpenListOfDams />
                <SearchForDam />
                <DamGroupSelector onSelectGroup={setSelectedGroup} />
            </div>
            <div className="top-dams-pie-charts-container">
                <TopDamsPieCharts damData={damData} />
            </div>
        </div>
    );
};

export default HomePage;
