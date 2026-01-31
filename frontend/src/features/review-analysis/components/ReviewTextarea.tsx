import type { ReviewTextareaProps } from '../types';

export function ReviewTextarea({
  value,
  onChange,
  disabled = false,
  placeholder = 'Paste customer review here...',
}: ReviewTextareaProps) {
  return (
    <textarea
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
      disabled={disabled}
      aria-label="Review text input"
      className="review-textarea"
    />
  );
}
