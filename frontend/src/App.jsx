import { useState } from 'react';
import ReviewInput from './components/ReviewInput';
import AnalysisResult from './components/AnalysisResult';

// In a real app, use env var.
// Default to standard local FastAPI port if not set.
// User must ensure backend is running.
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
  const [inputText, setInputText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    if (!inputText.trim()) return;

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
      });

      if (!response.ok) {
        throw new Error('Failed to analyze review');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      setError('Something went wrong. Please ensure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Review Insight</h1>
      
      <div className="input-card">
        <ReviewInput 
          value={inputText} 
          onChange={setInputText} 
          onAnalyze={handleAnalyze} 
          loading={loading}
        />
      </div>

      {error && (
        <div style={{ color: 'var(--topic-billing)', textAlign: 'center', fontWeight: 'bold' }}>
          {error}
        </div>
      )}

      {loading && (
        <div className="loading-spinner">
          Analyzing sentences using AI...
        </div>
      )}

      {result && (
        <AnalysisResult sentences={result.sentences} />
      )}
    </div>
  );
}

export default App;
