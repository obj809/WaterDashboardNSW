// src/pages/PageThree/PageThree.tsx

import React, { useState, useEffect } from 'react';
import { fetchDamData12Months } from '../../services/api';
import DamCapacityPercentageGraph from '../../components/DamCapacityPercentageGraph/DamCapacityPercentageGraph';
import DamGroupSelector from '../../components/DamGroupSelector/DamGroupSelector';
import './PageThree.scss';

const PageThree: React.FC = () => {
    const [groupDamData, setGroupDamData] = useState<any[]>([]);
    const [selectedGroup, setSelectedGroup] = useState<string>('sydney_dams');

    useEffect(() => {
        const loadGroupDamData = async () => {
            try {
                const data = await fetchDamData12Months(selectedGroup);
                setGroupDamData(data);
            } catch (error) {
                console.error('Error fetching group dam data:', error);
            }
        };

        loadGroupDamData();
    }, [selectedGroup]);

    return (
        <div className="page-three">
            <div className="header">
                <DamGroupSelector onSelectGroup={setSelectedGroup} />
            </div>
            <div className="content">
                <DamCapacityPercentageGraph data={groupDamData} />
            </div>
        </div>
    );
};

export default PageThree;
