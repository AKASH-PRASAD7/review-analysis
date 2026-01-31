import axios, { AxiosError, AxiosInstance } from 'axios';
import { env } from '@/utils/env';
import type { ApiError } from './types';


const createApiClient = (): AxiosInstance => {
  const client = axios.create({
    baseURL: env.apiUrl,
    headers: {
      'Content-Type': 'application/json',
    },
    timeout: 30000, // 30 seconds
  });

  // Request interceptor - add auth tokens, logging, etc.
  client.interceptors.request.use(
    (config) => {
      // Add any request modifications here (e.g., auth tokens)
      if (env.isDevelopment) {
        console.log(`[API] ${config.method?.toUpperCase()} ${config.url}`);
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  // Response interceptor - handle errors globally
  client.interceptors.response.use(
    (response) => {
      return response;
    },
    (error: AxiosError<ApiError>) => {
      // Centralized error handling
      if (env.isDevelopment) {
        console.error('[API Error]', error.response?.data || error.message);
      }

      // Transform error to consistent format
      const apiError: ApiError = {
        message: error.response?.data?.message || error.message || 'An unexpected error occurred',
        code: error.code,
        details: error.response?.data,
      };

      return Promise.reject(apiError);
    }
  );

  return client;
};

export const apiClient = createApiClient();
