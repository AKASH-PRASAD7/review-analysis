

export const queryKeys = {
  /**
   * All review-related queries
   */
  reviews: {
    all: ['reviews'] as const,
    analyze: (text: string) => [...queryKeys.reviews.all, 'analyze', text] as const,
  },
} as const;
