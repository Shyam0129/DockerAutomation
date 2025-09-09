import React from 'react';
import '../style/about.css';

const About = () => {
  return (
    <div className="about-container">
      <div className="about-content">
        <h1>Shyam Balanagu</h1>
        <div className="contact-info">
          <p>
            <a href="tel:+919502731467">+91 9502731467</a> |{" "}
            <a href="mailto:shyambalanagu724@gmail.com">shyambalanagu724@gmail.com</a> |{" "}
            <a href="https://linkedin.com/in/shyambalanagu" target="_blank" rel="noopener noreferrer">LinkedIn</a> |{" "}
            <a href="https://github.com/Shyam0129" target="_blank" rel="noopener noreferrer">GitHub</a>
          </p>
        </div>

        <div className="objective-section">
          <h2>Objective</h2>
          <p>
            Passionate SDE with hands-on experience in full-stack development and AI workflow integration. 
            Skilled in building scalable backend systems using modern stacks like Docker, React, and LLMs, 
            with a track record in freelance projects, competitions, and internal tools. Driven by curiosity, 
            adaptability, and a focus on high-impact solutions.
          </p>
        </div>
      </div>
    </div>
  );
};

export default About;