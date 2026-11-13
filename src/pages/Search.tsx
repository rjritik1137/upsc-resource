import { Link, useSearchParams } from 'react-router-dom'
import { useStore } from '../data'
import { paperLabel } from '../components'

export default function Search() {
  const s = useStore()
  const [sp] = useSearchParams()
  const q = (sp.get('q') ?? '').trim()
  const norm = (t: string) => t.toLowerCase().replace(/\barticles?\b/g, 'art')
  const nterms = norm(q).split(/\s+/).filter(Boolean)
  const hit = (t: string) => { const n = norm(t); return nterms.every(w => n.includes(w)) }
  const concepts = s.concepts.filter(c => hit([c.title, c.definition, ...c.subconcepts, ...c.distinctions].join(' ')))
  const qs = s.questions.filter(x => hit(x.text + ' ' + (x.options ?? []).map(o => o.text).join(' ')))
  return (
    <>
      <h1>Search: “{q}”</h1>
      <h2>Concepts ({concepts.length})</h2>
      {concepts.length ? <ul>{concepts.map(c => <li key={c.id}><Link to={`/concept/${c.id}`}>{c.title}</Link></li>)}</ul> : <p className="muted">No concept matches.</p>}
      <h2>Questions ({qs.length})</h2>
      <ul className="pyqs">{qs.slice(0, 40).map(x => <li key={x.id}><Link to={`/pyq/${x.id}`}>{x.year} · {paperLabel(x)} · Q{x.number}</Link>: {x.text.slice(0, 200)}{x.text.length > 200 ? '…' : ''}</li>)}</ul>
      {qs.length > 40 && <p><Link to={`/pyq?q=${encodeURIComponent(q)}`}>See all {qs.length} in the PYQ explorer →</Link></p>}
    </>
  )
}
