import { FormEvent, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useStore } from '../data'
import { Banner } from '../components'

export default function Home() {
  const s = useStore()
  const nav = useNavigate()
  const [q, setQ] = useState('')
  const submit = (e: FormEvent) => { e.preventDefault(); if (q.trim()) nav(`/search?q=${encodeURIComponent(q.trim())}`) }
  const start = [...s.concepts].sort((a, b) => s.topoIndex.get(a.id)! - s.topoIndex.get(b.id)!).filter(c => c.prerequisites.length === 0)
  // syllabus coverage = which syllabus points have at least one authored concept (a fact about this app's content, not about the learner)
  const covered = new Set(s.concepts.flatMap(c => c.syllabus_ids))
  const papers = ['Prelims', 'Mains']
  const bySection = new Map<string, { total: number; covered: number }>()
  s.syllabus.forEach(i => {
    const k = `${i.stage} ${i.paper}`
    const v = bySection.get(k) ?? { total: 0, covered: 0 }
    v.total++; if (covered.has(i.id)) v.covered++
    bySection.set(k, v)
  })
  void papers
  return (
    <>
      <h1>UPSC GS Static Study Guide</h1>
      <p className="lead">What to study, how to study it, where to study it, and why it matters — traced to previous-year questions and the syllabus.</p>
      <form className="search" onSubmit={submit} role="search">
        <input aria-label="Search concepts and questions" placeholder="Search concepts and PYQs, e.g. “Article 356”, “Money Bill”, “Governor”" value={q} onChange={e => setQ(e.target.value)} autoFocus />
        <button type="submit">Search</button>
      </form>
      <Banner tone="info">
        <strong>Status:</strong> {s.concepts.length} concepts across {s.subjects.filter(x => x.status !== 'not-started').length} subjects. All are draft and unreviewed. Every GS subject now has concepts; coverage within each is selective, not exhaustive.
        All PYQ↔concept links are <em>proposed</em> by keyword rules and have not been reviewed. See <Link to="/coverage">Sources &amp; Coverage</Link>.
      </Banner>

      <h2>Subjects</h2>
      <div className="grid">
        {s.subjects.map(sub => (
          <div className="card" key={sub.id}>
            <h3>{sub.status !== 'not-started' ? <Link to={`/subject/${sub.id}`}>{sub.title}</Link> : sub.title}</h3>
            <p className="muted">{sub.papers.join(' · ')}</p>
            <p>{sub.status !== 'not-started' ? <>{s.concepts.filter(c => c.subject === sub.id).length} concepts{sub.status === 'partial' ? <span className="tag muted">World History not built</span> : null}</> : <span className="tag muted">not built yet</span>}</p>
          </div>
        ))}
      </div>

      <h2>Recommended start sequence</h2>
      <p className="muted">Concepts with no prerequisites, by subject. Open one, then follow “Next concepts” on each page. Order is by prerequisites, not by exam importance.</p>
      {s.subjects.filter(x => x.status !== 'not-started').map(sub => <div key={sub.id}><h3>{sub.title}</h3><ol>{start.filter(c => c.subject === sub.id).map(c => <li key={c.id}><Link to={`/concept/${c.id}`}>{c.title}</Link></li>)}</ol></div>)}

      <h2>Syllabus coverage in this app</h2>
      <p className="muted">Number of syllabus points (from the supplied syllabus.pdf) that at least one authored concept points to. This is content coverage, not your progress.</p>
      <table>
        <thead><tr><th>Syllabus section</th><th>Points</th><th>With ≥1 concept</th></tr></thead>
        <tbody>{[...bySection].map(([k, v]) => <tr key={k}><td>{k}</td><td>{v.total}</td><td>{v.covered}</td></tr>)}</tbody>
      </table>
    </>
  )
}
