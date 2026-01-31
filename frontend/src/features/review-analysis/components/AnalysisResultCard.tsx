import { Card, CardHeader, CardBody } from '@/components/layout/Card';
import { Loader } from '@/components/common/Loader';
import { ErrorMessage } from '@/components/common/ErrorMessage';
import { SentenceList } from './SentenceList';
import type { Sentence, ApiError } from '@/api/types';

export interface AnalysisResultCardProps {
  isLoading: boolean;
  error: ApiError | null;
  sentences?: Sentence[];
  onRetry?: () => void;
}

export function AnalysisResultCard({
  isLoading,
  error,
  sentences,
  onRetry,
}: AnalysisResultCardProps) {
  // Don't show card if no loading, error, or results
  if (!isLoading && !error && !sentences) {
    return null;
  }

  return (
    <Card>
      <CardHeader>Analysis Result</CardHeader>
      <CardBody>
        {isLoading && <Loader label="Analyzing..." />}
        
        {error && (
          <ErrorMessage
            message={error.message || 'Failed to analyze review'}
            onRetry={onRetry}
          />
        )}
        
        {!isLoading && !error && sentences && (
          <SentenceList sentences={sentences} />
        )}
      </CardBody>
    </Card>
  );
}
