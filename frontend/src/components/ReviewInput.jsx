import React from 'react';

const ReviewInput = ({ value, onChange, onAnalyze, loading }) => {
  return (
    <>
      <textarea
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Paste a customer review here (e.g. 'The app is great! But billing is confusing.')..."
        disabled={loading}
      />
      <button onClick={onAnalyze} disabled={loading || !value.trim()}>
        {loading ? 'Analyzing...' : 'Analyze Review'}
      </button>
    </>
  );
};

export default ReviewInput;
