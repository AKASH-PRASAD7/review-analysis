import type { Sentence } from '@/api/types';

interface TopicSummaryProps {
  sentences: Sentence[];
}

export function TopicSummary({ sentences }: TopicSummaryProps) {
  const counts = sentences.reduce((acc, sentence) => {
    const topic = sentence.topic;
    acc[topic] = (acc[topic] || 0) + 1;
    return acc;
  }, {} as Record<string, number>);

  return (
    <div className="topic-summary" style={{ marginBottom: '1rem', padding: '1rem', backgroundColor: '#f9fafb', borderRadius: '8px' }}>
      <h4 style={{ marginTop: 0, marginBottom: '0.5rem', fontSize: '0.9rem', color: 'var(--text-primary)' }}>Analysis Summary</h4>
      <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
        {Object.entries(counts).map(([topic, count]) => (
          <div key={topic} style={{ fontSize: '0.875rem' }}>
            <strong>{topic}:</strong> {count}
          </div>
        ))}
      </div>
    </div>
  );
}
