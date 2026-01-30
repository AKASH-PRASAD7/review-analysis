import React from 'react';

const ReviewInput = ({ value, onChange, onAnalyze, loading }) => {
  return (
    <>
      <textarea
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Paste customer review here..."
        disabled={loading}
      />
      <div className="button-container">
        <button onClick={onAnalyze} disabled={loading || !value.trim()}>
          {loading ? 'Analyzing...' : 'Analyze'}
        </button>
      </div>
    </>
  );
};

export default ReviewInput;
