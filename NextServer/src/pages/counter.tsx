import styles from '@/styles/counter/Counter.module.css'
import { useState } from 'react'; 
import { useAppDispatch, useAppSelector} from '@/hooks/useScript'
import { increment, decrement, 
     incrementAsync, selectCount } from '@/modules/counter/counter.slice'

export default function Counter() {
    
  
    return (
      <div>
        
        카운터
      </div>
    );
  }