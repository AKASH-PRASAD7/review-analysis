export const API_ENDPOINTS = {
  ANALYZE: '/api/v1/analyze',
} as const;

export type ApiEndpoint = typeof API_ENDPOINTS[keyof typeof API_ENDPOINTS];
