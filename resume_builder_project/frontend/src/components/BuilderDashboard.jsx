
import React from 'react';
import api from '../utils/api.jsx'; // Secure Axios instance

// --- 1. ResumeItem Component (The Card) ---
function ResumeItem({ resume, onDelete }) {
    const updatedAt = new Date(resume.updated_at).toLocaleDateString();

    return (
        <div className="dashboard-card"> 
            
            <div className="card-header-details">
                {/* Resume Name */}
                <h3>{resume.full_name || "Untitled Resume"}</h3>
                
                {/* Metadata List */}
                <ul>
                    <li className="with-icon"><strong>Title:</strong> {resume.title || "No Title Set"}</li>
                    <li className="with-icon"><strong>Last Updated:</strong> {updatedAt}</li>
                </ul>
            </div>
            
            <div className="resume-actions">
                {/* Link to Django Edit View */}
                <a href={`/resume/${resume.id}/edit/`} className="btn-submit edit-btn">
                    Edit Resume (Django Form)
                </a> 
                {/* Link to Django Detail View */}
                <a href={`/resume/${resume.id}/`} className="btn-submit view-btn">
                    View Details
                </a> 
                {/* Secure DELETE Button */}
                <button 
                    onClick={() => onDelete(resume.id)} 
                    className="btn-submit delete-btn" 
                >
                    Delete (API)
                </button>
            </div>
        </div>
    );
}

// --- 2. BuilderDashboard Component (The Layout and Logic) ---
function BuilderDashboard({ resumes, setResumes }) {
    
    // --- Delete Function ---
    const handleDelete = async (resumeId) => {
        if (window.confirm("Are you sure you want to delete this resume?")) {
            try {
                await api.delete(`resumes/${resumeId}/`); 
                setResumes(resumes.filter(r => r.id !== resumeId));
                alert("Resume deleted.");
            } catch (error) {
                console.error("API Error on Delete:", error.response || error);
                alert("Failed to delete. Check server logs.");
            }
        }
    };

    return (
        // Outer wrapper for vertical centering
        <div className="dashboard-vertical-wrapper"> 
            <div className="dashboard-container">
                
                {/* Dashboard Header */}
                <header className="dashboard-header">
                    <h2>Your Resumes ({resumes.length})</h2>
                    
                    {/* 🛑 FIX: Uses onClick to guarantee redirection to the form path 🛑 */}
                    <a href="#" 
                       onClick={(e) => { 
                           e.preventDefault(); 
                           window.location.href = '/resume/create/'; 
                       }}
                       className="btn-submit create-btn"
                    > 
                        + CREATE NEW RESUME
                    </a>
                </header>

                {/* Resume List Grid */}
                <div className="resume-list-grid">
                    {resumes.length > 0 ? (
                        resumes.map(resume => (
                            <ResumeItem 
                                key={resume.id} 
                                resume={resume} 
                                onDelete={handleDelete}
                            />
                        ))
                    ) : (
                        // Empty State Display
                        <div className="empty-state">
                             <i className="ri-file-add-line"></i>
                             <h3>No Resumes Found</h3>
                            <p>Click 'Create New Resume' to start building your professional portfolio.</p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

export default BuilderDashboard;