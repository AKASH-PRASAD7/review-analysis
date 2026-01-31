import { ReactNode } from 'react';

export interface CardProps {
  children: ReactNode;
  className?: string;
}

export interface CardHeaderProps {
  children: ReactNode;
}

export interface CardBodyProps {
  children: ReactNode;
}

export function Card({ children, className }: CardProps) {
  return <div className={`card ${className || ''}`}>{children}</div>;
}

export function CardHeader({ children }: CardHeaderProps) {
  return <div className="card-header">{children}</div>;
}

export function CardBody({ children }: CardBodyProps) {
  return <div className="card-body">{children}</div>;
}


Card.Header = CardHeader;
Card.Body = CardBody;
