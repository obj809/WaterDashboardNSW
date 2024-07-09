// src/components/TextBox/TextBox.tsx

import React from 'react';
import './TextBox.scss';

const TextBox: React.FC = () => {
    return (
        <div className="text-box">
            <ul className="text-box-list">
                <li>Dams are invaluable to human society as they provide critical water storage for irrigation, hydroelectric power generation, flood control, and reliable access to freshwater, thereby supporting agriculture, energy production, and community resilience.</li>
                <li>Statement about Dams in NSW and use of the WaterNSW API</li>
                <li>How the app was build, tech stack and data analysis</li>
                <li>How to use the app</li>
                <li>How this affects the world and what people can do to help</li>
            </ul>
        </div>
    );
};

export default TextBox;
