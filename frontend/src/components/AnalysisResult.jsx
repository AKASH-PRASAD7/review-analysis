import React from 'react';

const AnalysisResult = ({ sentences }) => {
  if (!sentences || sentences.length === 0) return null;

  return (
    <div className="result-container">
      {sentences.map((s, idx) => (
        <div 
          key={idx} 
          className={`sentence-block topic-${s.topic.toLowerCase()}`}
        >
          <span className="sentence-text">{s.text}</span>
          <span className="topic-badge">{s.topic}</span>
        </div>
      ))}
    </div>
  );
};

export default AnalysisResult;
