// src/components/OpenListOfDams/OpenListOfDams.tsx

import React from 'react';
import { useNavigate } from 'react-router-dom';
import './OpenListOfDams.scss';

const OpenListOfDams: React.FC = () => {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/damlist');
    };

    return (
        <div className="open-list-of-dams">
            <button onClick={handleClick}>Open list of Dams</button>
        </div>
    );
};

export default OpenListOfDams;
