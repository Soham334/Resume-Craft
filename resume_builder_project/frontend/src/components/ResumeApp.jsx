// frontend/src/components/ResumeApp.jsx
import api from '../utils/api.jsx'; // Add .jsx extension
import React, { useState, useEffect } from 'react';
import LandingPage from './LandingPage.jsx';
import BuilderDashboard from './BuilderDashboard.jsx';
function ResumeApp() {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [resumes, setResumes] = useState([]);
    const [loading, setLoading] = useState(true);

    // Function to check user status and fetch initial data
    useEffect(() => {
        // Hitting the secure DRF endpoint checks session authentication
        api.get('resumes/') 
            .then(response => {
                // Success: User is logged in
                setIsAuthenticated(true);
                setResumes(response.data);
            })
            .catch(error => {
                // Failure (401/403): User is not logged in
                setIsAuthenticated(false);
            })
            .finally(() => {
                setLoading(false);
            });
    }, []);

    if (loading) {
        // Display a loading state until the authentication check is done
        return <div className="loading-screen"><h1>Loading Resume Builder...</h1></div>;
    }

    return (
        <>
            {/* The primary logic for displaying the application content */}
            {isAuthenticated ? (
                // User is logged in, show their dashboard
                <BuilderDashboard resumes={resumes} setResumes={setResumes} />
            ) : (
                // User is logged out, show the landing page
                <LandingPage />
            )}
        </>
    );
}

export default ResumeApp;