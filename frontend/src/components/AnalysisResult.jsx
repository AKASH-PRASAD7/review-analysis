import React from 'react';

const AnalysisResult = ({ sentences }) => {
  if (!sentences || sentences.length === 0) return null;

  return (
    <div className="result-list">
      {sentences.map((s, idx) => (
        <div 
          key={idx} 
          className={`sentence-block block-${s.topic.toLowerCase()}`}
        >
          <div className="topic-badge-container">
            <span className="topic-badge">[{s.topic}]</span>
          </div>
          <div className="sentence-text">
            {s.text}
          </div>
        </div>
      ))}
    </div>
  );
};

export default AnalysisResult;
