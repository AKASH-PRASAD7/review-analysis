/**
 * Environment Configuration
 * 
 * Centralized access to environment variables with type safety and validation.
 */

interface EnvConfig {
  apiUrl: string;
  isDevelopment: boolean;
  isProduction: boolean;
}

/**
 * Get environment variable with fallback
 */
function getEnvVar(key: string, fallback: string): string {
  return import.meta.env[key] || fallback;
}

/**
 * Application environment configuration
 */
export const env: EnvConfig = {
  apiUrl: getEnvVar('VITE_API_URL', 'http://localhost:8000'),
  isDevelopment: import.meta.env.DEV,
  isProduction: import.meta.env.PROD,
};
