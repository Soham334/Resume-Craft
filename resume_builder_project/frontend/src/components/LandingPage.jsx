// frontend/src/components/LandingPage.jsx (CORRECTED for Image Paths)

import React from 'react';

function LandingPage() {
    // NOTE: This component is rendered when the user is LOGGED OUT
    return (
        <div id="page1" className="landing-hero"> 
            
            {/* 1. LARGE, ANIMATED HERO HEADING */}
            <h1>
                CRAFT YOUR FUTURE{' '}
                <span>
                    {/* SVG content is fine as standard XML */}
                    <svg fill="none" viewBox="0 0 131 136">
                        <path fill="#fff" d="M48 77.457v7.224h7.224l21.307-21.306-7.224-7.225L48 77.457Zm34.118-19.67a1.919 1.919 0 0 0 0-2.716l-4.508-4.508a1.919 1.919 0 0 0-2.716 0l-3.526 3.526 7.224 7.224 3.526-3.525Z" />
                    </svg>
                </span>
            </h1>
            <h1>RESUME PLATFORM</h1>
            
            <p>
                We partner with ambitious professionals, guiding them to stand out with our modern design and ATS-optimized structure.
            </p>
            
            {/* 2. TAGS/CALLOUTS */}
            <div id="page1-something">
                <h4>ATS Optimized</h4>
                <h4>User Experience</h4>
                <h4>and</h4>
                <h4>Professional Design</h4>.
            </div>
            

            {/* 3. ANIMATED MOVING DIV (Ticker effect) */}
            <div id="moving-div">
                <div id="blur-left"></div>
                
                {/* Ticker Content Set 1 (Must use the exact filenames) */}
                <div className="move">
                    <img src="/static/resumesite/forbes-logo-svgrepo-com.svg" alt="Forbes Logo"/>
                    <img src="/static/resumesite/google-icon-logo-svgrepo-com.svg" alt="Google Logo"/>
                    <img src="/static/resumesite/ethereum-logo-svgrepo-com.svg" alt="Ethereum Logo"/>
                    <img src="/static/resumesite/creative-cloud-cc-logo-svgrepo-com.svg" alt="Creative Cloud Logo"/>
                    <img src="/static/resumesite/facebook-2-logo-svgrepo-com.svg" alt="Facebook Logo"/>
                </div>

                {/* CRITICAL FIX: Ticker Content Set 2 (Duplicates Set 1 for seamless loop) */}
                <div className="move">
                    <img src="/static/resumesite/forbes-logo-svgrepo-com.svg" alt="Forbes Logo"/>
                    <img src="/static/resumesite/google-icon-logo-svgrepo-com.svg" alt="Google Logo"/>
                    <img src="/static/resumesite/ethereum-logo-svgrepo-com.svg" alt="Ethereum Logo"/>
                    <img src="/static/resumesite/creative-cloud-cc-logo-svgrepo-com.svg" alt="Creative Cloud Logo"/>
                    <img src="/static/resumesite/facebook-2-logo-svgrepo-com.svg" alt="Facebook Logo"/>
                </div>
                
                <div id="blur-right"></div>
            </div>
        </div>
    );
}

export default LandingPage;