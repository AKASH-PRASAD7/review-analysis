import { useState } from 'react';
import { useAnalyzeReview } from '@/api/queries';
import type { AnalyzeResponse, ApiError } from '@/api/types';

export interface UseReviewAnalysisReturn {
  // Input state
  inputText: string;
  setInputText: (text: string) => void;
  
  // Query state
  isPending: boolean;
  error: ApiError | null;
  data: AnalyzeResponse | undefined;
  
  // Actions
  handleAnalyze: () => void;
  reset: () => void;
  
  // Derived state
  isEmpty: boolean;
  canAnalyze: boolean;
  hasResults: boolean;
}

/**
 * Hook for managing review analysis state and logic
 */
export function useReviewAnalysis(): UseReviewAnalysisReturn {
  const [inputText, setInputText] = useState('');
  const { mutate, isPending, error, data, reset: resetMutation } = useAnalyzeReview();

  const handleAnalyze = () => {
    if (!inputText.trim()) return;
    mutate({ text: inputText });
  };

  const reset = () => {
    setInputText('');
    resetMutation();
  };

  // Derived state
  const isEmpty = inputText.trim().length === 0;
  const canAnalyze = !isEmpty && !isPending;
  const hasResults = !!data?.sentences && data.sentences.length > 0;

  return {
    inputText,
    setInputText,
    isPending,
    error,
    data,
    handleAnalyze,
    reset,
    isEmpty,
    canAnalyze,
    hasResults,
  };
}
