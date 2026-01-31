import { SentenceItem } from './SentenceItem';
import type { SentenceListProps } from '../types';

export function SentenceList({ sentences }: SentenceListProps) {
  if (!sentences || sentences.length === 0) {
    return null;
  }

  return (
    <div className="result-list">
      {sentences.map((sentence, index) => (
        <SentenceItem key={index} sentence={sentence} />
      ))}
    </div>
  );
}
