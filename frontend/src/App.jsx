import { useState } from 'react';
import ReviewInput from './components/ReviewInput';
import AnalysisResult from './components/AnalysisResult';

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
      {/* Customer Review Card */}
      <div className="card">
        <div className="card-header">
          Customer Review
        </div>
        <div className="card-body">
          <ReviewInput 
            value={inputText} 
            onChange={setInputText} 
            onAnalyze={handleAnalyze} 
            loading={loading}
          />
        </div>
      </div>

      {error && (
        <div className="error-msg">
          {error}
        </div>
      )}

      {/* Analysis Result Card */}
      {(result || loading) && (
        <div className="card">
          <div className="card-header">
            Analysis Result
          </div>
          <div className="card-body">
            {loading ? (
              <div style={{ textAlign: 'center', color: 'var(--text-secondary)' }}>
                Analyzing...
              </div>
            ) : (
              <AnalysisResult sentences={result.sentences} />
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
