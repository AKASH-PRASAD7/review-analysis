
export interface Sentence {
  text: string;
  topic: string;
}


export interface AnalyzeRequest {
  text: string;
}

export interface AnalyzeResponse {
  sentences: Sentence[];
}


export interface ApiError {
  message: string;
  code?: string;
  details?: unknown;
}
