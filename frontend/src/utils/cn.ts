/**
 * Class Name Utility
 * 
 * Utility for conditionally joining class names together.
 */

type ClassValue = string | number | boolean | undefined | null;

/**
 * Combines class names, filtering out falsy values
 * 
 * @example
 * cn('btn', isActive && 'active', 'primary') // 'btn active primary'
 */
export function cn(...classes: ClassValue[]): string {
  return classes.filter(Boolean).join(' ');
}
