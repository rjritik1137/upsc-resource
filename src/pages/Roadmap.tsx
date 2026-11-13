import { useMemo, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { pyqStats, useStore } from '../data'
import { Banner, Tag } from '../components'

export default function Roadmap() {
  const { id } = useParams()
  const s = useStore()
  const subject = s.subjects.find(x => x.id === id)
  const [stage, setStage] = useState<'all' | 'Prelims' | 'Mains'>('all')
  const [from, setFrom] = useState(1995)
  const [to, setTo] = useState(2026)
  const [onlyWithPyq, setOnlyWithPyq] = useState(false)

  const rows = useMemo(() => {
    return s.concepts.filter(c => c.subject === id).map(c => {
      const qs = (s.qByConcept.get(c.id) ?? []).filter(q => (stage === 'all' || q.stage === stage) && q.year >= from && q.year <= to)
      return { c, st: pyqStats(qs) }
    }).sort((a, b) => s.topoIndex.get(a.c.id)! - s.topoIndex.get(b.c.id)!)
  }, [s, id, stage, from, to])

  if (!subject) return <p>Unknown subject. <Link to="/">Home</Link></p>
  if (subject.status === 'not-started') return (<><h1>{subject.title}</h1><Banner>No concepts have been built for this subject yet (Phase D of the plan). Nothing is shown rather than placeholder content.</Banner></>)

  return (
    <>
      <h1>{subject.title}: roadmap</h1>
      {subject.status === 'partial' && <Banner>Only part of this subject is built (Ancient, Medieval, Modern History and Art & Culture). World History is not yet covered.</Banner>}
      <Banner tone="info">
        Concepts are listed <strong>prerequisite-first</strong> inside each group. “Direct PYQs” counts questions linked to the concept by <em>proposed</em> (unreviewed) rules; it describes the past
        papers supplied and does not predict future papers.
      </Banner>
      <fieldset className="filters">
        <legend>Filters</legend>
        <label>Stage <select value={stage} onChange={e => setStage(e.target.value as typeof stage)}><option value="all">Prelims + Mains</option><option>Prelims</option><option>Mains</option></select></label>
        <label>PYQ year from <input type="number" min={1995} max={2026} value={from} onChange={e => setFrom(+e.target.value)} /></label>
        <label>to <input type="number" min={1995} max={2026} value={to} onChange={e => setTo(+e.target.value)} /></label>
        <label><input type="checkbox" checked={onlyWithPyq} onChange={e => setOnlyWithPyq(e.target.checked)} /> only concepts with PYQs in this filter</label>
      </fieldset>
      {subject.groups!.map(g => {
        const items = rows.filter(r => r.c.group === g.id && (!onlyWithPyq || r.st.total > 0))
        if (!items.length) return null
        return (
          <section key={g.id}>
            <h2>{g.id}. {g.title}</h2>
            <ol className="roadmap">
              {items.map(({ c, st }) => (
                <li key={c.id}>
                  <Link to={`/concept/${c.id}`}>{c.title}</Link>
                  <div className="meta">
                    {c.prerequisites.length > 0 && <>Needs: {c.prerequisites.map(p => <Link key={p} className="chip" to={`/concept/${p}`}>{s.conceptById.get(p)?.title}</Link>)} </>}
                  </div>
                  <div className="meta">
                    <Tag tone="muted">Direct PYQs: {st.total}</Tag>
                    <Tag tone="muted">Prelims {st.prelims} · Mains {st.mains}</Tag>
                    <Tag tone="muted">{st.years} distinct year{st.years === 1 ? '' : 's'}{st.first ? ` (${st.first}–${st.last})` : ''}</Tag>
                    <Tag tone="muted">{c.syllabus_ids.length} syllabus point{c.syllabus_ids.length === 1 ? '' : 's'}</Tag>
                    <Tag tone="muted">~{c.effort_hours_editorial} h (editorial estimate)</Tag>
                  </div>
                </li>
              ))}
            </ol>
          </section>
        )
      })}
    </>
  )
}
