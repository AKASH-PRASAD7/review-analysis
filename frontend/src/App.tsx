import { Container } from '@/components/layout/Container';
import {
  ReviewInputCard,
  AnalysisResultCard,
  useReviewAnalysis,
} from '@/features/review-analysis';
import './App.css';

function App() {
  const {
    inputText,
    setInputText,
    isPending,
    error,
    data,
    handleAnalyze,
    canAnalyze,
  } = useReviewAnalysis();

  return (
    <Container>
      <ReviewInputCard
        value={inputText}
        onChange={setInputText}
        onAnalyze={handleAnalyze}
        isLoading={isPending}
        canAnalyze={canAnalyze}
      />

      <AnalysisResultCard
        isLoading={isPending}
        error={error}
        sentences={data?.sentences}
        onRetry={handleAnalyze}
      />
    </Container>
  );
}

export default App;
