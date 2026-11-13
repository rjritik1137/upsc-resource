import { ChangeEvent } from 'react'
import { Link } from 'react-router-dom'
import { useStore } from '../data'
import { useSaved } from '../local'

export default function Progress() {
  const s = useStore()
  const { saved, replace } = useSaved()
  const exportJson = () => {
    const url = URL.createObjectURL(new Blob([JSON.stringify(saved, null, 1)], { type: 'application/json' }))
    const a = document.createElement('a'); a.href = url; a.download = 'upsc-guide-backup.json'; a.click(); URL.revokeObjectURL(url)
  }
  const importJson = async (e: ChangeEvent<HTMLInputElement>) => {
    const f = e.target.files?.[0]; if (!f) return
    try { const j = JSON.parse(await f.text()); replace({ studied: Array.isArray(j.studied) ? j.studied : [], bookmarks: Array.isArray(j.bookmarks) ? j.bookmarks : [] }) } catch { alert('Not a valid backup file') }
  }
  return (
    <>
      <h1>My checkmarks &amp; saved questions</h1>
      <p className="muted">Optional. Stored only in this browser (localStorage). Export a backup if you want to move devices. Nothing is sent anywhere.</p>
      <p><button onClick={exportJson}>Export JSON</button> <label className="inline">Import JSON <input type="file" accept="application/json" onChange={importJson} /></label></p>
      <h2>Studied concepts ({saved.studied.length})</h2>
      <ul>{saved.studied.map(id => <li key={id}><Link to={`/concept/${id}`}>{s.conceptById.get(id)?.title ?? id}</Link></li>)}</ul>
      <h2>Saved questions ({saved.bookmarks.length})</h2>
      <ul>{saved.bookmarks.map(id => { const q = s.questionById.get(id); return <li key={id}><Link to={`/pyq/${id}`}>{q ? `${q.year} · Q${q.number}: ${q.text.slice(0, 100)}…` : id}</Link></li> })}</ul>
    </>
  )
}
