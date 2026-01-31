import { ReactNode } from 'react';
import { Button } from './Button';

export interface ErrorMessageProps {
  message: string;
  onRetry?: () => void;
  children?: ReactNode;
}

export function ErrorMessage({ message, onRetry, children }: ErrorMessageProps) {
  return (
    <div className="error-msg" role="alert">
      <p>{message}</p>
      {onRetry && (
        <Button variant="secondary" onClick={onRetry}>
          Retry
        </Button>
      )}
      {children}
    </div>
  );
}
