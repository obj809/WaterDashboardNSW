// src/components/DamGroupSelector/DamGroupSelector.tsx

import React, { useState } from 'react';
import './DamGroupSelector.scss';

interface DamGroupSelectorProps {
    onSelectGroup: (group: string) => void;
}

const groups = [
    { value: 'sydney_dams', label: 'Sydney Dams' },
    { value: 'popular_dams', label: 'Popular Dams' },
    { value: 'large_dams', label: 'Large Dams' },
    { value: 'small_dams', label: 'Small Dams' },
    { value: 'greatest_released', label: 'Highest flow' },
];

const DamGroupSelector: React.FC<DamGroupSelectorProps> = ({ onSelectGroup }) => {
    const [currentGroup, setCurrentGroup] = useState(groups[0]);

    const handleClick = () => {
        const currentIndex = groups.findIndex(group => group.value === currentGroup.value);
        const nextIndex = (currentIndex + 1) % groups.length;
        const nextGroup = groups[nextIndex];
        setCurrentGroup(nextGroup);
        onSelectGroup(nextGroup.value);
    };

    return (
        <div className="dam-group-selector">
            <button onClick={handleClick}>{currentGroup.label}</button>
        </div>
    );
};

export default DamGroupSelector;
