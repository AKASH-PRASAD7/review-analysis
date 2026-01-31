export const API_ENDPOINTS = {
  ANALYZE: '/analyze',
} as const;

export type ApiEndpoint = typeof API_ENDPOINTS[keyof typeof API_ENDPOINTS];
