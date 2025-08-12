import { DependencyList, useEffect } from 'react'
import { useAsyncAction } from './useAsyncAction'

export function useAsync<T>(
  action: () => Promise<T>,
  dependencies: DependencyList
) {
  const { error, data, loading, trigger } = useAsyncAction(action)

  useEffect(() => {
    trigger()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, dependencies)

  return { data, loading, error, reload: trigger }
}
