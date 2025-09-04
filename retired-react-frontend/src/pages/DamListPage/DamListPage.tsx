// src/pages/DamListPage/DamListPage.tsx

import React, { useEffect, useState } from 'react';
import { fetchDamNames } from '../../services/api';
import { useNavigate } from 'react-router-dom';
import './DamListPage.scss';

const DamListPage: React.FC = () => {
    const [damNames, setDamNames] = useState<string[]>([]);
    const navigate = useNavigate();

    useEffect(() => {
        const loadDamNames = async () => {
            try {
                const names = await fetchDamNames();
                setDamNames(names);
            } catch (error) {
                console.error('Error fetching dam names:', error);
            }
        };

        loadDamNames();
    }, []);

    const handleDamClick = async (damName: string) => {
        navigate('/dam', { state: { damName } });
    };

    const handleBackClick = () => {
        navigate('/');
    };

    const splitDamNames = () => {
        const third = Math.ceil(damNames.length / 3);
        const firstSection = damNames.slice(0, third);
        const secondSection = damNames.slice(third, third * 2);
        const thirdSection = damNames.slice(third * 2, damNames.length);
        return [firstSection, secondSection, thirdSection];
    };

    const [firstSection, secondSection, thirdSection] = splitDamNames();

    return (
        <div className="dam-list-page">
            <button className="back-button" onClick={handleBackClick}>Back</button>
            <h1>List of Dams</h1>
            <div className="dam-list-sections">
                <ul>
                    {firstSection.map((dam, index) => (
                        <li key={index} onClick={() => handleDamClick(dam)}>
                            {dam}
                        </li>
                    ))}
                </ul>
                <ul>
                    {secondSection.map((dam, index) => (
                        <li key={index} onClick={() => handleDamClick(dam)}>
                            {dam}
                        </li>
                    ))}
                </ul>
                <ul>
                    {thirdSection.map((dam, index) => (
                        <li key={index} onClick={() => handleDamClick(dam)}>
                            {dam}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default DamListPage;
