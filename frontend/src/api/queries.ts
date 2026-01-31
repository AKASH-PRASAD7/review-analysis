import { useMutation, UseMutationResult } from '@tanstack/react-query';
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
 * Hook for analyzing review text
 * 
 * @example
 * const { mutate, isPending, error, data } = useAnalyzeReview();
 * mutate({ text: 'Great product!' });
 */
export function useAnalyzeReview(): UseMutationResult<
  AnalyzeResponse,
  ApiError,
  AnalyzeRequest,
  unknown
> {
  return useMutation({
    mutationFn: analyzeReview,
    mutationKey: queryKeys.reviews.all,
  });
}
