// src/components/GoogleMapComponent/GoogleMapComponent.tsx

import React, { useEffect, useRef } from 'react';
import { Loader } from '@googlemaps/js-api-loader';

interface GoogleMapComponentProps {
    lat: number;
    lng: number;
}

const containerStyle = {
    width: '100%',
    height: '100%',
};

const GoogleMapComponent: React.FC<GoogleMapComponentProps> = ({ lat, lng }) => {
    const mapRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
        const loader = new Loader({
            apiKey: import.meta.env.VITE_GOOGLE_MAPS_API_KEY!,
            version: 'weekly',
        });

        loader.load().then(() => {
            if (mapRef.current && !isNaN(lat) && !isNaN(lng)) {
                const map = new google.maps.Map(mapRef.current, {
                    center: { lat, lng },
                    zoom: 10,
                });

                new google.maps.Marker({
                    position: { lat, lng },
                    map,
                });
            } else {
                console.error('Invalid coordinates:', { lat, lng });
            }
        }).catch(err => {
            console.error('Error loading Google Maps API:', err);
        });
    }, [lat, lng]);

    return <div ref={mapRef} style={containerStyle}></div>;
};

export default GoogleMapComponent;
