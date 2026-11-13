import { useCallback, useEffect, useState } from 'react'

// Optional local state: studied concepts and bookmarked questions. Navigation never depends on it.
const KEY = 'upsc-guide-v1'
interface Saved { studied: string[]; bookmarks: string[] }
const read = (): Saved => {
  try { return { studied: [], bookmarks: [], ...JSON.parse(localStorage.getItem(KEY) ?? '{}') } } catch { return { studied: [], bookmarks: [] } }
}
const listeners = new Set<() => void>()
const write = (s: Saved) => { localStorage.setItem(KEY, JSON.stringify(s)); listeners.forEach(l => l()) }

export function useSaved() {
  const [s, setS] = useState<Saved>(read)
  useEffect(() => { const l = () => setS(read()); listeners.add(l); return () => { listeners.delete(l) } }, [])
  const toggle = useCallback((k: keyof Saved, id: string) => {
    const cur = read(); const set = new Set(cur[k])
    set.has(id) ? set.delete(id) : set.add(id)
    write({ ...cur, [k]: [...set] })
  }, [])
  const replace = useCallback((next: Saved) => write({ studied: next.studied ?? [], bookmarks: next.bookmarks ?? [] }), [])
  return { saved: s, toggle, replace }
}
