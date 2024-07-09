// src/components/DamContent/DamContent.tsx

import React from 'react';
import './DamContent.scss';

interface DamContentProps {
    content: string;
    children?: React.ReactNode;
}

const DamContent: React.FC<DamContentProps> = ({ children }) => {
    return (
        <div className="dam-content">
            {children}
        </div>
    );
};

export default DamContent;
