import { useMemo } from 'react';

export function TopicLegend() {
  const topics = useMemo(() => [
    { name: 'Billing', color: 'var(--badge-billing)' },
    { name: 'Performance', color: 'var(--badge-performance)' },
    { name: 'Support', color: 'var(--badge-support)' },
    { name: 'UX', color: 'var(--badge-ux)' },
    { name: 'Account', color: 'var(--badge-account)' },
    { name: 'Other', color: 'var(--badge-other)' },
  ], []);

  return (
    <div className="topic-legend" style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', padding: '0.5rem 0' }}>
      {topics.map((topic) => (
        <div key={topic.name} style={{ display: 'flex', items: 'center', gap: '0.25rem' }}>
          <span
            style={{
              width: '12px',
              height: '12px',
              backgroundColor: topic.color,
              borderRadius: '50%',
              display: 'inline-block',
            }}
          />
          <span style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>{topic.name}</span>
        </div>
      ))}
    </div>
  );
}
