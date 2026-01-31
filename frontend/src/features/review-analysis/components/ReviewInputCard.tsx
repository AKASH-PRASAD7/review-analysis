import { Card, CardHeader, CardBody } from '@/components/layout/Card';
import { Button } from '@/components/common/Button';
import { ReviewTextarea } from './ReviewTextarea';

export interface ReviewInputCardProps {
  value: string;
  onChange: (value: string) => void;
  onAnalyze: () => void;
  isLoading: boolean;
  canAnalyze: boolean;
}

export function ReviewInputCard({
  value,
  onChange,
  onAnalyze,
  isLoading,
  canAnalyze,
}: ReviewInputCardProps) {
  return (
    <Card>
      <CardHeader>Customer Review</CardHeader>
      <CardBody>
        <ReviewTextarea
          value={value}
          onChange={onChange}
          disabled={isLoading}
        />
        <div className="button-container">
          <Button
            onClick={onAnalyze}
            disabled={!canAnalyze}
            isLoading={isLoading}
          >
            Analyze
          </Button>
        </div>
      </CardBody>
    </Card>
  );
}
