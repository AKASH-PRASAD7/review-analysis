import { ReactNode } from 'react';
import { cn } from '@/utils/cn';

export interface ContainerProps {
  children: ReactNode;
  className?: string;
}

export function Container({ children, className }: ContainerProps) {
  return <div className={cn('container', className)}>{children}</div>;
}
