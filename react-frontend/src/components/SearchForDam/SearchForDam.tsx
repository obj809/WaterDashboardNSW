// src/components/SearchForDam/SearchForDam.tsx

import React, { useState, useEffect, useRef } from 'react';
import { fetchDamNames, fetchDamDataByName } from '../../services/api';
import { useNavigate } from 'react-router-dom';
import './SearchForDam.scss';

const SearchForDam: React.FC = () => {
    const [searchQuery, setSearchQuery] = useState('');
    const [damNames, setDamNames] = useState<string[]>([]);
    const [filteredDams, setFilteredDams] = useState<string[]>([]);
    const [activeSuggestionIndex, setActiveSuggestionIndex] = useState<number>(-1);
    const suggestionsRef = useRef<HTMLUListElement>(null);
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

    useEffect(() => {
        if (searchQuery) {
            setFilteredDams(
                damNames.filter(dam =>
                    dam.toLowerCase().includes(searchQuery.toLowerCase())
                )
            );
        } else {
            setFilteredDams([]);
        }
    }, [searchQuery, damNames]);

    useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if (e.key === 'Escape') {
                setSearchQuery('');
                setFilteredDams([]);
                setActiveSuggestionIndex(-1);
            }
        };

        document.addEventListener('keydown', handleKeyDown);
        return () => {
            document.removeEventListener('keydown', handleKeyDown);
        };
    }, []);

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setSearchQuery(e.target.value);
        setActiveSuggestionIndex(-1);
    };

    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (filteredDams.length > 0) {
            if (e.key === 'ArrowDown') {
                setActiveSuggestionIndex((prevIndex) =>
                    prevIndex < filteredDams.length - 1 ? prevIndex + 1 : 0
                );
            } else if (e.key === 'ArrowUp') {
                setActiveSuggestionIndex((prevIndex) =>
                    prevIndex > 0 ? prevIndex - 1 : filteredDams.length - 1
                );
            } else if (e.key === 'Enter') {
                if (activeSuggestionIndex >= 0) {
                    const selectedDam = filteredDams[activeSuggestionIndex];
                    handleSuggestionClick(selectedDam);
                } else {
                    handleSubmit(e);
                }
            }
        }
    };

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement> | React.KeyboardEvent<HTMLInputElement>) => {
        e.preventDefault();
        if (searchQuery) {
            try {
                const data = await fetchDamDataByName(searchQuery);
                navigate('/dam', { state: { damData: data } });
            } catch (error) {
                console.error('Error fetching dam data:', error);
            }
        }
    };

    const handleSuggestionClick = async (damName: string) => {
        try {
            const data = await fetchDamDataByName(damName);
            navigate('/dam', { state: { damData: data } });
        } catch (error) {
            console.error('Error fetching dam data:', error);
        }
    };

    return (
        <div className="search-for-dam">
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={searchQuery}
                    onChange={handleInputChange}
                    onKeyDown={handleKeyDown}
                    placeholder="Search for a Dam"
                />
                <button type="submit">Search</button>
            </form>
            {filteredDams.length > 0 && (
                <ul className="suggestions-list" ref={suggestionsRef}>
                    {filteredDams.map((dam, index) => (
                        <li
                            key={index}
                            className={index === activeSuggestionIndex ? 'active' : ''}
                            onClick={() => handleSuggestionClick(dam)}
                        >
                            {dam}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default SearchForDam;

