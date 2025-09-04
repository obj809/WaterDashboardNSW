// src/components/TextBox/TextBox.tsx

import React from 'react';
import './TextBox.scss';

const TextBox: React.FC = () => {
    return (
        <div className="text-box">
            <ul className="text-box-list">
                <p>
                    🌊 Since ancient times, civilizations have relied on dams, which remain vital today for ensuring a stable water supply, generating hydroelectric power, and mitigating flood risks. Additionally, dams support environmental conservation by creating wetlands and improving water quality.
                </p>
                <p>
                    🌏 In New South Wales, dams are managed by WaterNSW and represent a critical stage in the delivery of clean, safe water to millions of residents and businesses in Greater Sydney. This project collects live and historical data about dams in NSW to support water management efforts and enhance public awareness.
                </p>
                <p>
                    🌐 This application is essentially a data dashboard website that collects and analyses live data from the WaterNSW API. It is built with a Flask backend, a dynamic React user interface, data processing with Spark and AWS for data pipeline creation and associated storage. More detailed information about how this application was created can be found on Github.
                </p>
                <p>
                    🔍 To use the application, a user can search for a dam or open a list to find specific data about a dam in NSW. On the main page of the application, the user will find a number of graphs that compare major dams in different groupings that can be changed dynamically with the click of a button.
                </p>
                <p>
                    🌱 People can get involved in water conservation efforts by staying informed, advocating for sustainable water practices, and supporting strong water infrastructure policies. This collective action enhances global water sustainability and resilience against environmental challenges.
                </p>
            </ul>
        </div>
    );
};

export default TextBox;  
