import { useCallback, useEffect, useRef, useState } from 'react'

export function useAsyncAction<Params extends any[], Result>( // eslint-disable-line
  action: (...args: Params) => Promise<Result>
) {
  const [error, setError] = useState<unknown>()
  const [loading, setLoading] = useState(false)
  const [data, setData] = useState<Result>()

  const actionRef = useRef(action)
  actionRef.current = action

  const requestId = useRef(0)

  const perform = useCallback(async (...args: Params) => {
    requestId.current++
    const currentId = requestId.current

    setLoading(true)
    try {
      const result = await actionRef.current(...args)

      if (currentId === requestId.current) {
        setData(result)
        setError(undefined)
      }

      return result
    } catch (error) {
      if (currentId === requestId.current) {
        setError(error)
        setData(undefined)
      }

      throw error
    } finally {
      setLoading(false)
    }
  }, [])

  const trigger = useCallback((...args: Params) => {
    perform(...args).catch(() => {})
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  useEffect(() => {
    return () => {
      // eslint-disable-next-line react-hooks/exhaustive-deps
      requestId.current++
    }
  }, [])

  return { perform, trigger, data, error, loading }
}
