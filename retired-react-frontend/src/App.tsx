// src/App.tsx

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage/HomePage';
import SelectedDamPage from './pages/SelectedDamPage/SelectedDamPage';
import DamListPage from './pages/DamListPage/DamListPage';
import PageTwo from './pages/PageTwo/PageTwo';
import PageThree from './pages/PageThree/PageThree';
import PageFour from './pages/PageFour/PageFour';
import PageFive from './pages/PageFive/PageFive';
import Footer from './components/Footer/Footer';
import './App.scss';

const App: React.FC = () => {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={
                        <div className="stacked-pages">
                            <HomePage />
                            <PageTwo />
                            <PageThree />
                            <PageFour />
                            <PageFive />
                            <Footer />
                        </div>
                    } />
                    <Route path="/dam" element={<SelectedDamPage />} />
                    <Route path="/damlist" element={<DamListPage />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
