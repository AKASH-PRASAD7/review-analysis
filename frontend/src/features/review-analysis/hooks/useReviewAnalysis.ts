import { useState } from 'react';
import { useReviewQuery } from '@/api/queries';
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
  const [queryText, setQueryText] = useState('');

  const { isLoading, isFetching, error, data } = useReviewQuery(queryText);

  // Consider it pending if loading (first time) or fetching (refetching/background)
  // BUT for UX we might only want to show big loader on initial load or manual trigger
  const isPending = isLoading || (isFetching && !!queryText);

  const handleAnalyze = () => {
    if (!inputText.trim()) return;
    setQueryText(inputText);
  };

  const reset = () => {
    setInputText('');
    setQueryText('');
  };

  // Derived state
  const isEmpty = inputText.trim().length === 0;
  
  // Can analyze if input is not empty AND (we are not pending OR input is different from last query)
  const canAnalyze = !isEmpty; 

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
