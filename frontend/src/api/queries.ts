import { useQuery, UseQueryResult } from '@tanstack/react-query';
import { apiClient } from './client';
import { API_ENDPOINTS } from './endpoints';
import { queryKeys } from './queryKeys';
import type { AnalyzeRequest, AnalyzeResponse, ApiError } from './types';

async function analyzeReview(request: AnalyzeRequest): Promise<AnalyzeResponse> {
  const response = await apiClient.post<AnalyzeResponse>(
    API_ENDPOINTS.ANALYZE,
    request
  );
  return response.data;
}

/**
 * Hook for analyzing review text with caching
 * 
 * @param text - The text to analyze. Query is disabled if empty.
 */
export function useReviewQuery(text: string): UseQueryResult<AnalyzeResponse, ApiError> {
  return useQuery({
    queryKey: queryKeys.reviews.analyze(text),
    queryFn: () => analyzeReview({ text }),
    enabled: !!text.trim(),
    staleTime: 1000 * 60 * 5, // Cache for 5 minutes
    retry: false,
  });
}
