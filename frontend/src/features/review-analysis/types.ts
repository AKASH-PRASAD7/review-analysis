import type { Sentence } from '@/api/types';


export interface ReviewTextareaProps {
  value: string;
  onChange: (value: string) => void;
  disabled?: boolean;
  placeholder?: string;
}

/**
 * Props for SentenceList component
 */
export interface SentenceListProps {
  sentences: Sentence[];
}

/**
 * Props for SentenceItem component
 */
export interface SentenceItemProps {
  sentence: Sentence;
}
