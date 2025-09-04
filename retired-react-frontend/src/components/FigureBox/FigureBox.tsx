// src/components/FigureBox/FigureBox.tsx

import React from 'react';
import './FigureBox.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSpinner } from '@fortawesome/free-solid-svg-icons';

const FigureBox: React.FC<{ title: string, data: string | null }> = ({ title, data }) => {
    return (
        <div className="figure-box">
            <div className="figure-box-title">{title}</div>
            <div className="figure-box-data">
                {data !== null ? data : <FontAwesomeIcon icon={faSpinner} spin />}
            </div>
        </div>
    );
};

export default FigureBox;
