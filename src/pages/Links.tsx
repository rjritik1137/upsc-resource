import { useMemo, useState } from 'react'
import { Link, useSearchParams } from 'react-router-dom'
import { useStore } from '../data'
import { Banner, Tag } from '../components'

export default function Links() {
  const s = useStore()
  const [sp, setSp] = useSearchParams()
  const [filter, setFilter] = useState('')
  const cid = sp.get('concept') ?? s.concepts[0].id
  const c = s.conceptById.get(cid)!
  const name = (id: string) => s.conceptById.get(id)?.title ?? s.stubById.get(id)?.title ?? s.syllabusById.get(id)?.text ?? id

  const mine = s.conceptLinks.filter(l => l.source === cid || l.target === cid)
  const related = mine.filter(l => l.relation === 'related')
  const coTested = useMemo(() => {
    const mineQ = new Set((s.qByConcept.get(cid) ?? []).map(q => q.id))
    const cnt = new Map<string, number>()
    s.qLinks.forEach(l => { if (l.concept_id !== cid && mineQ.has(l.question_id)) cnt.set(l.concept_id, (cnt.get(l.concept_id) ?? 0) + 1) })
    return [...cnt].sort((a, b) => b[1] - a[1]).slice(0, 8)
  }, [s, cid])
  const all = s.conceptLinks.filter(l => l.relation === 'related' && (name(l.source) + ' ' + name(l.target) + ' ' + l.rationale).toLowerCase().includes(filter.toLowerCase()))

  return (
    <>
      <h1>Interlinkage explorer</h1>
      <Banner tone="info">Links come from two places: <strong>authored</strong> (prerequisites and related-concept links with a rationale, unreviewed) and <strong>derived</strong> (concepts that share linked questions, computed from <em>proposed</em> question links). A graph view is not part of the MVP.</Banner>
      <label>Concept{' '}
        <select value={cid} onChange={e => setSp({ concept: e.target.value })}>
          {s.subjects.filter(sb => s.concepts.some(x => x.subject === sb.id)).map(sb => <optgroup key={sb.id} label={sb.title}>{s.concepts.filter(x => x.subject === sb.id).map(x => <option key={x.id} value={x.id}>{x.title}</option>)}</optgroup>)}
        </select>
      </label>
      <h2><Link to={`/concept/${c.id}`}>{c.title}</Link></h2>
      <div className="grid">
        <div className="card"><h3>Builds on (prerequisites)</h3>{c.prerequisites.length ? <ul>{c.prerequisites.map(p => <li key={p}><Link to={`/links?concept=${p}`}>{name(p)}</Link></li>)}</ul> : <p className="muted">None: a starting concept.</p>}</div>
        <div className="card"><h3>Leads to</h3>{(s.dependents.get(cid) ?? []).length ? <ul>{(s.dependents.get(cid) ?? []).map(p => <li key={p}><Link to={`/links?concept=${p}`}>{name(p)}</Link></li>)}</ul> : <p className="muted">Nothing depends on it yet.</p>}</div>
      </div>
      <h3>Related, with rationale</h3>
      {related.length ? <ul>{related.map(l => { const o = l.source === cid ? l.target : l.source; return <li key={l.id}>{s.conceptById.has(o) ? <Link to={`/links?concept=${o}`}>{name(o)}</Link> : <>{name(o)} <Tag tone="muted">other subject, not authored</Tag></>}<div className="meta">{l.rationale} <em>({l.evidence})</em></div></li> })}</ul> : <p className="muted">None recorded.</p>}
      <h3>Concepts that share linked questions (derived)</h3>
      {coTested.length ? <ul>{coTested.map(([id, n]) => <li key={id}><Link to={`/links?concept=${id}`}>{name(id)}</Link> <Tag tone="muted">{n} shared question{n === 1 ? '' : 's'}</Tag></li>)}</ul> : <p className="muted">No shared questions.</p>}

      <h2>Cross-subject themes (planned)</h2>
      <p className="muted">Targets in other subjects that Polity concepts point to. Their pages are not authored yet.</p>
      <ul>{s.stubs.map(st => <li key={st.id}><Link to={`/concept/${st.id}`}>{st.title}</Link> ← {s.concepts.filter(x => x.cross_subject.includes(st.id)).map(x => x.title).join('; ')}</li>)}</ul>

      <h2>All related-concept links</h2>
      <label>Filter <input value={filter} onChange={e => setFilter(e.target.value)} placeholder="text" /></label>
      <table><thead><tr><th>From</th><th>To</th><th>Rationale</th></tr></thead>
        <tbody>{all.map(l => <tr key={l.id}><td><Link to={`/links?concept=${l.source}`}>{name(l.source)}</Link></td><td>{s.conceptById.has(l.target) ? <Link to={`/links?concept=${l.target}`}>{name(l.target)}</Link> : name(l.target)}</td><td>{l.rationale}</td></tr>)}</tbody></table>
    </>
  )
}
