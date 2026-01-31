import type { SentenceItemProps } from '../types';

export function SentenceItem({ sentence }: SentenceItemProps) {
  return (
    <div className={`sentence-block block-${sentence.topic.toLowerCase()}`}>
      <div className="topic-badge-container">
        <span className="topic-badge">[{sentence.topic}]</span>
      </div>
      <div className="sentence-text">{sentence.text}</div>
    </div>
  );
}
