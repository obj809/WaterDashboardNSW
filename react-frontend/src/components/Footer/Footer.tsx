// src/components/Footer/Footer.tsx

import React from 'react';
import './Footer.scss';

const Footer: React.FC = () => {
    const currentYear = new Date().getFullYear();

    return (
        <div className="footer">
            <div className="footer-left">
                <p>© {currentYear} Sydney Dam Monitoring</p>
            </div>
            <div className="footer-right">
                <a href="https://api.nsw.gov.au/Product/Index/26" target="_blank" rel="noopener noreferrer">
                    <i className="fa-solid fa-link"></i>
                </a>
                <a href="https://www.waternsw.com.au/" target="_blank" rel="noopener noreferrer">
                    <i className="fa-solid fa-globe"></i>
                </a>
                <a href="https://github.com/cyberforge1" target="_blank" rel="noopener noreferrer">
                    <i className="fa-brands fa-github"></i>
                </a>
            </div>
        </div>
    );
};

export default Footer;
