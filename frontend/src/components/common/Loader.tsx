import { cn } from '@/utils/cn';

export interface LoaderProps {
  size?: 'small' | 'medium' | 'large';
  className?: string;
  label?: string;
}

export function Loader({ size = 'medium', className, label = 'Loading...' }: LoaderProps) {
  return (
    <div
      className={cn('loader-container', className)}
      role="status"
      aria-label={label}
    >
      <div className={cn('loader', `loader-${size}`)} />
      <span className="loader-text">{label}</span>
    </div>
  );
}
