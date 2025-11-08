// frontend/src/index.js

import React from 'react';
import ReactDOM from 'react-dom/client';
import ResumeApp from './components/ResumeApp'; 

const container = document.getElementById('react-root');
if (container) {
    const root = ReactDOM.createRoot(container);
    root.render(
        <React.StrictMode>
            {/* The main component that manages auth and routing */}
            <ResumeApp />
        </React.StrictMode>
    );
} else {
    console.error("Critical Error: The <div id='react-root'> element was not found in the HTML.");
}