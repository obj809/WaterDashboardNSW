// src/pages/PageTwo/PageTwo.tsx

import React, { useState, useEffect } from 'react';
import { fetchDamsDataByGroup } from '../../services/api';
import DamStorageGraph from '../../components/DamStorageGraph/DamStorageGraph';
import DamGroupSelector from '../../components/DamGroupSelector/DamGroupSelector';
import './PageTwo.scss';

const PageTwo: React.FC = () => {
    const [groupDamData, setGroupDamData] = useState<any[]>([]);
    const [selectedGroup, setSelectedGroup] = useState<string>('sydney_dams');

    useEffect(() => {
        const loadGroupDamData = async () => {
            try {
                const data = await fetchDamsDataByGroup(selectedGroup);
                setGroupDamData(data);
            } catch (error) {
                console.error('Error fetching group dam data:', error);
            }
        };

        loadGroupDamData();
    }, [selectedGroup]);

    return (
        <div className="page-two">
            <div className="header">
                <DamGroupSelector onSelectGroup={setSelectedGroup} />
            </div>
            <div className="content">
                <DamStorageGraph data={groupDamData} />
            </div>
        </div>
    );
};

export default PageTwo;
